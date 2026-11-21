"""
Retrain PINN for H2-brine IFT using real experimental data.

Physics loss enforces:
- IFT -> 0 at critical temperature Tc
- dIFT/dP < 0 (IFT decreases with pressure)
- dIFT/dT < 0 (IFT decreases with temperature)
- dIFT/dS > 0 (IFT increases with salinity)
- Learnable parameters constrained to literature values
"""
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import os
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Device: {device}")


class PINNIFTS(nn.Module):
    def __init__(self, input_dim=3, hidden_dim=64, output_dim=1, n_hidden_layers=4):
        super().__init__()
        layers = [nn.Linear(input_dim, hidden_dim), nn.Tanh()]
        for _ in range(n_hidden_layers - 1):
            layers += [nn.Linear(hidden_dim, hidden_dim), nn.Tanh()]
        layers += [nn.Linear(hidden_dim, output_dim)]
        self.net = nn.Sequential(*layers)
        # Learnable PR-EOS parameters (constrained to literature)
        self.log_Tc = nn.Parameter(torch.log(torch.tensor(33.2)))
        self.log_Pc = nn.Parameter(torch.log(torch.tensor(1.30)))
        self.omega = nn.Parameter(torch.tensor(-0.216))

    @property
    def Tc(self):
        return torch.exp(self.log_Tc)

    @property
    def Pc(self):
        return torch.exp(self.log_Pc)

    def forward(self, x):
        return self.net(x)


# Load experimental data
print("Loading experimental H2-brine IFT data...")
data = []
with open("data/raw/ift_experimental.csv", "r") as f:
    header = f.readline()  # skip header
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(",")
        P = float(parts[0])
        T = float(parts[1])
        S = float(parts[2])
        IFT = float(parts[3])
        data.append([P, T, S, IFT])

data = np.array(data, dtype=np.float32)
P_data = data[:, 0]
T_data = data[:, 1]
S_data = data[:, 2]
IFT_data = data[:, 3]

print(f"Loaded {len(data)} experimental data points")
print(f"P range: [{P_data.min():.1f}, {P_data.max():.1f}] MPa")
print(f"T range: [{T_data.min():.1f}, {T_data.max():.1f}] K")
print(f"S range: [{S_data.min():.0f}, {S_data.max():.0f}] ppm")
print(f"IFT range: [{IFT_data.min():.2f}, {IFT_data.max():.2f}] mN/m")

# Normalize inputs for training stability
P_mean, P_std = P_data.mean(), P_data.std()
T_mean, T_std = T_data.mean(), T_data.std()
S_mean, S_std = S_data.mean(), S_data.std()
IFT_mean, IFT_std = IFT_data.mean(), IFT_data.std()

P_n = (P_data - P_mean) / P_std
T_n = (T_data - T_mean) / T_std
S_n = (S_data - S_mean) / S_std
IFT_n = (IFT_data - IFT_mean) / IFT_std

X = np.stack([P_n, T_n, S_n], axis=1)
y = IFT_n.reshape(-1, 1)

# Train/validation split (80/20)
n_train = int(0.8 * len(X))
indices = np.random.permutation(len(X))
train_idx, val_idx = indices[:n_train], indices[n_train:]

X_train = torch.tensor(X[train_idx], dtype=torch.float32).to(device)
y_train = torch.tensor(y[train_idx], dtype=torch.float32).to(device)
X_val = torch.tensor(X[val_idx], dtype=torch.float32).to(device)
y_val = torch.tensor(y[val_idx], dtype=torch.float32).to(device)

# Physics constraint points (for enforcing gradients)
n_physics = 500
P_phys = np.random.uniform(10, 50, n_physics)
T_phys = np.random.uniform(300, 500, n_physics)
S_phys = np.random.uniform(0, 300000, n_physics)
X_phys_n = np.stack([
    (P_phys - P_mean) / P_std,
    (T_phys - T_mean) / T_std,
    (S_phys - S_mean) / S_std,
], axis=1)
X_phys = torch.tensor(X_phys_n, dtype=torch.float32, requires_grad=True).to(device)

# Model, optimizer, scheduler
model = PINNIFTS().to(device)
optimizer = optim.Adam(model.parameters(), lr=1e-3)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode="min",
                                                  factor=0.5, patience=200)

# Loss weights
w_data = 1.0      # MSE on experimental data
w_phys_p = 0.5    # dIFT/dP < 0 constraint
w_phys_t = 0.5    # dIFT/dT < 0 constraint
w_phys_s = 0.5    # dIFT/dS > 0 constraint
w_phys_tc = 0.1   # IFT -> 0 at Tc
w_param = 0.01    # Parameter regularization toward literature

n_epochs = 5000
history = {"train_loss": [], "val_loss": [], "data_loss": [], "phys_loss": []}

print(f"\nTraining for {n_epochs} epochs...")
print(f"Weights: data={w_data}, phys_P={w_phys_p}, phys_T={w_phys_t}, "
      f"phys_S={w_phys_s}, phys_Tc={w_phys_tc}, param={w_param}")

for epoch in range(n_epochs):
    model.train()
    optimizer.zero_grad()

    # Data loss
    pred_train = model(X_train)
    loss_data = nn.MSELoss()(pred_train, y_train)

    # Physics loss: gradient constraints at physics points
    pred_phys = model(X_phys)
    grads = torch.autograd.grad(pred_phys, X_phys, grad_outputs=torch.ones_like(pred_phys),
                                create_graph=True)[0]
    # grads[:,0] = dIFT/dP, grads[:,1] = dIFT/dT, grads[:,2] = dIFT/dS (in normalized space)
    # Need to convert to physical units: dIFT/dP_phys = dIFT/dP_n * (IFT_std / P_std)
    dIFT_dP = grads[:, 0] * (IFT_std / P_std)
    dIFT_dT = grads[:, 1] * (IFT_std / T_std)
    dIFT_dS = grads[:, 2] * (IFT_std / S_std)

    # Enforce dIFT/dP < 0, dIFT/dT < 0, dIFT/dS > 0 (relu on violations)
    loss_phys_p = torch.mean(torch.relu(dIFT_dP))      # penalize positive dIFT/dP
    loss_phys_t = torch.mean(torch.relu(dIFT_dT))      # penalize positive dIFT/dT
    loss_phys_s = torch.mean(torch.relu(-dIFT_dS))     # penalize negative dIFT/dS

    # Critical behavior: IFT -> 0 near Tc
    X_tc = torch.tensor([[(30 - P_mean) / P_std, (33.2 - T_mean) / T_std,
                          (50000 - S_mean) / S_std]], dtype=torch.float32).to(device)
    IFT_tc = model(X_tc)
    loss_phys_tc = IFT_tc.pow(2).mean()

    # Parameter regularization toward literature values
    loss_param = ((model.log_Tc - torch.log(torch.tensor(33.2))).pow(2) +
                  (model.log_Pc - torch.log(torch.tensor(1.30))).pow(2) +
                  (model.omega - torch.tensor(-0.216)).pow(2))

    loss = (w_data * loss_data +
            w_phys_p * loss_phys_p +
            w_phys_t * loss_phys_t +
            w_phys_s * loss_phys_s +
            w_phys_tc * loss_phys_tc +
            w_param * loss_param)

    loss.backward()
    optimizer.step()
    scheduler.step(loss)

    # Validation
    model.eval()
    with torch.no_grad():
        pred_val = model(X_val)
        loss_val = nn.MSELoss()(pred_val, y_val).item()

    history["train_loss"].append(loss.item())
    history["val_loss"].append(loss_val)
    history["data_loss"].append(loss_data.item())
    history["phys_loss"].append((loss_phys_p + loss_phys_t + loss_phys_s).item())

    if (epoch + 1) % 500 == 0:
        print(f"Epoch {epoch+1}/{n_epochs}: "
              f"train={loss.item():.6f}, val={loss_val:.6f}, "
              f"data={loss_data.item():.6f}, "
              f"phys_P={loss_phys_p.item():.6f}, phys_T={loss_phys_t.item():.6f}, "
              f"phys_S={loss_phys_s.item():.6f}")

# Final evaluation
model.eval()
with torch.no_grad():
    pred_train = model(X_train)
    pred_val = model(X_val)
    train_rmse = torch.sqrt(nn.MSELoss()(pred_train, y_train)).item() * IFT_std
    val_rmse = torch.sqrt(nn.MSELoss()(pred_val, y_val)).item() * IFT_std

print(f"\n=== TRAINING COMPLETE ===")
print(f"Train RMSE: {train_rmse:.3f} mN/m")
print(f"Val RMSE:   {val_rmse:.3f} mN/m")
print(f"Learned Tc: {model.Tc.item():.2f} K (lit: 33.2 K)")
print(f"Learned Pc: {model.Pc.item():.2f} MPa (lit: 1.30 MPa)")
print(f"Learned omega: {model.omega.item():.4f} (lit: -0.216)")

# Sensitivity check on retrained model
print("\n=== SENSITIVITY CHECK ===")
P_range = np.linspace(10, 50, 50)
T_fixed, S_fixed = 350.0, 100000.0
X_p = np.stack([P_range, np.full_like(P_range, T_fixed),
                np.full_like(P_range, S_fixed)], axis=1)
X_p_n = (X_p - np.array([P_mean, T_mean, S_mean])) / np.array([P_std, T_std, S_std])
with torch.no_grad():
    IFT_p = model(torch.tensor(X_p_n, dtype=torch.float32).to(device)).cpu().numpy().flatten()
IFT_p = IFT_p * IFT_std + IFT_mean
print(f"Pressure sweep: IFT range = [{IFT_p.min():.2f}, {IFT_p.max():.2f}] mN/m")

T_range = np.linspace(300, 500, 50)
P_fixed, S_fixed = 25.0, 100000.0
X_t = np.stack([np.full_like(T_range, P_fixed), T_range,
                np.full_like(T_range, S_fixed)], axis=1)
X_t_n = (X_t - np.array([P_mean, T_mean, S_mean])) / np.array([P_std, T_std, S_std])
with torch.no_grad():
    IFT_t = model(torch.tensor(X_t_n, dtype=torch.float32).to(device)).cpu().numpy().flatten()
IFT_t = IFT_t * IFT_std + IFT_mean
print(f"Temperature sweep: IFT range = [{IFT_t.min():.2f}, {IFT_t.max():.2f}] mN/m")

S_range = np.linspace(0, 200000, 50)
P_fixed, T_fixed = 25.0, 350.0
X_s = np.stack([np.full_like(S_range, P_fixed),
                np.full_like(S_range, T_fixed), S_range], axis=1)
X_s_n = (X_s - np.array([P_mean, T_mean, S_mean])) / np.array([P_std, T_std, S_std])
with torch.no_grad():
    IFT_s = model(torch.tensor(X_s_n, dtype=torch.float32).to(device)).cpu().numpy().flatten()
IFT_s = IFT_s * IFT_std + IFT_mean
print(f"Salinity sweep: IFT range = [{IFT_s.min():.2f}, {IFT_s.max():.2f}] mN/m")

# Save model
checkpoint = {
    "model_state_dict": model.state_dict(),
    "P_mean": P_mean, "P_std": P_std,
    "T_mean": T_mean, "T_std": T_std,
    "S_mean": S_mean, "S_std": S_std,
    "IFT_mean": IFT_mean, "IFT_std": IFT_std,
    "learned_Tc": model.Tc.item(),
    "learned_Pc": model.Pc.item(),
    "learned_omega": model.omega.item(),
    "train_rmse": train_rmse,
    "val_rmse": val_rmse,
    "n_data_points": len(data),
    "history": history,
}
torch.save(checkpoint, "outputs/pinn_ift_model_v3.pt")
print("\nModel saved to outputs/pinn_ift_model_v3.pt")

# Save normalization stats for inference
norm_stats = {
    "P_mean": float(P_mean), "P_std": float(P_std),
    "T_mean": float(T_mean), "T_std": float(T_std),
    "S_mean": float(S_mean), "S_std": float(S_std),
    "IFT_mean": float(IFT_mean), "IFT_std": float(IFT_std),
}
with open("outputs/pinn_norm_stats_v3.json", "w") as f:
    json.dump(norm_stats, f, indent=2)

# Plot training history
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(history["train_loss"], label="Train", linewidth=2)
axes[0].plot(history["val_loss"], label="Val", linewidth=2)
axes[0].set_xlabel("Epoch"); axes[0].set_ylabel("Total Loss")
axes[0].set_title("Training History"); axes[0].legend(); axes[0].grid(True, alpha=0.3)

axes[1].plot(history["data_loss"], label="Data Loss", linewidth=2)
axes[1].plot(history["phys_loss"], label="Physics Loss", linewidth=2)
axes[1].set_xlabel("Epoch"); axes[1].set_ylabel("Loss")
axes[1].set_title("Loss Components"); axes[1].legend(); axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("outputs/pinn_training_v3.png", dpi=150, bbox_inches="tight")
plt.close()
print("Training plot saved to outputs/pinn_training_v3.png")
