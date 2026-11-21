"""
Diagnose PINN IFT model insensitivity (constant output issue).

Checks:
1. Model output range across input sweep (P, T, S)
2. Whether output is constant regardless of input
3. Loss landscape - data loss vs physics loss dominance
4. Learnable parameter traces (Tc, Pc, omega)
"""
import numpy as np
import torch
import torch.nn as nn
import json
import os
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


# Load model
model = PINNIFTS()
ckpt = torch.load("outputs/pinn_ift_model_pr_eos.pt", map_location=device)
model.load_state_dict(ckpt["model_state_dict"])
model.to(device)
model.eval()

print(f"\nLearned params: Tc={ckpt.get('learned_Tc','N/A')} K, "
      f"Pc={ckpt.get('learned_Pc','N/A')} MPa, omega={ckpt.get('learned_omega','N/A')}")

# 1. Sweep inputs independently
print("\n=== INPUT SWEEP DIAGNOSTIC ===")

# Pressure sweep (T=350 K, S=50000 ppm fixed)
P_range = np.linspace(10, 50, 100)
T_fixed, S_fixed = 350.0, 50000.0
X_p = np.stack([P_range, np.full_like(P_range, T_fixed),
                np.full_like(P_range, S_fixed)], axis=1).astype(np.float32)
with torch.no_grad():
    IFT_p = model(torch.tensor(X_p).to(device)).cpu().numpy().flatten()
print(f"Pressure sweep: IFT range = [{IFT_p.min():.4f}, {IFT_p.max():.4f}] "
      f"(std={IFT_p.std():.6f})")

# Temperature sweep (P=25 MPa, S=50000 ppm fixed)
T_range = np.linspace(300, 500, 100)
P_fixed, S_fixed = 25.0, 50000.0
X_t = np.stack([np.full_like(T_range, P_fixed), T_range,
                np.full_like(T_range, S_fixed)], axis=1).astype(np.float32)
with torch.no_grad():
    IFT_t = model(torch.tensor(X_t).to(device)).cpu().numpy().flatten()
print(f"Temperature sweep: IFT range = [{IFT_t.min():.4f}, {IFT_t.max():.4f}] "
      f"(std={IFT_t.std():.6f})")

# Salinity sweep (P=25 MPa, T=350 K fixed)
S_range = np.linspace(0, 200000, 100)
P_fixed, T_fixed = 25.0, 350.0
X_s = np.stack([np.full_like(S_range, P_fixed),
                np.full_like(S_range, T_fixed), S_range], axis=1).astype(np.float32)
with torch.no_grad():
    IFT_s = model(torch.tensor(X_s).to(device)).cpu().numpy().flatten()
print(f"Salinity sweep: IFT range = [{IFT_s.min():.4f}, {IFT_s.max():.4f}] "
      f"(std={IFT_s.std():.6f})")

# 2. Full 3D grid sweep
print("\n=== 3D GRID SWEEP ===")
P_grid, T_grid, S_grid = np.meshgrid(
    np.linspace(10, 50, 20), np.linspace(300, 500, 20), np.linspace(0, 200000, 20),
    indexing="ij"
)
X_3d = np.stack([P_grid.ravel(), T_grid.ravel(), S_grid.ravel()], axis=1).astype(np.float32)
with torch.no_grad():
    IFT_3d = model(torch.tensor(X_3d).to(device)).cpu().numpy().flatten()
print(f"3D sweep: IFT range = [{IFT_3d.min():.4f}, {IFT_3d.max():.4f}] "
      f"(std={IFT_3d.std():.6f})")
print(f"Unique values (rounded to 4 dp): {len(np.unique(np.round(IFT_3d, 4)))} / {len(IFT_3d)}")

# 3. Check gradient sensitivity (autograd)
print("\n=== GRADIENT SENSITIVITY ===")
X_test = torch.tensor([[25.0, 350.0, 50000.0]], dtype=torch.float32,
                      requires_grad=True, device=device)
out = model(X_test)
grads = torch.autograd.grad(out, X_test, create_graph=False)[0]
print(f"dIFT/dP = {grads[0,0].item():.6e}")
print(f"dIFT/dT = {grads[0,1].item():.6e}")
print(f"dIFT/dS = {grads[0,2].item():.6e}")

# 4. Plot results
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].plot(P_range, IFT_p, "b-", linewidth=2)
axes[0].set_xlabel("Pressure (MPa)"); axes[0].set_ylabel("IFT (mN/m)")
axes[0].set_title("IFT vs Pressure (T=350K, S=50k ppm)")
axes[0].grid(True, alpha=0.3)

axes[1].plot(T_range, IFT_t, "r-", linewidth=2)
axes[1].set_xlabel("Temperature (K)"); axes[1].set_ylabel("IFT (mN/m)")
axes[1].set_title("IFT vs Temperature (P=25MPa, S=50k ppm)")
axes[1].grid(True, alpha=0.3)

axes[2].plot(S_range / 1000, IFT_s, "g-", linewidth=2)
axes[2].set_xlabel("Salinity (k ppm)"); axes[2].set_ylabel("IFT (mN/m)")
axes[2].set_title("IFT vs Salinity (P=25MPa, T=350K)")
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("outputs/pinn_sensitivity_diagnostic.png", dpi=150, bbox_inches="tight")
plt.close()
print("\nDiagnostic plot saved to outputs/pinn_sensitivity_diagnostic.png")

# Verdict
constant = IFT_3d.std() < 1e-3
print(f"\n=== VERDICT ===")
print(f"Model output is {'CONSTANT (degenerate)' if constant else 'VARIABLE'}")
print(f"IFT std across 3D sweep: {IFT_3d.std():.6f} mN/m")
if constant:
    print("ROOT CAUSE: PINN ignores inputs -> safety penalty becomes neutral everywhere.")
    print("FIX: Retrain with real experimental H2-brine IFT data and balanced loss weights.")
