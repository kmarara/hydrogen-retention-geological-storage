# arXiv Submission Package for Hydrogen Storage Site Selection Paper

## Files
- `paper.tex` - Main LaTeX source file
- `references.bib` - Bibliography (BibTeX)
- `figures/week11_full_integration.png` - Main figure (integrated decision map)
- `figures/pinn_training_v3.png` - PINN training history figure

## Compilation (local)

```bash
# Install TeX Live (if not already installed)
# Ubuntu/Debian: sudo apt-get install texlive-full
# macOS: brew install --cask mactex
# Windows: install MiKTeX or TeX Live

cd paper/

# Compile with bibtex
pdflatex paper.tex
bibtex paper.aux
pdflatex paper.tex
pdflatex paper.tex

# Output: paper.pdf
```

## arXiv Submission

1. Go to https://arxiv.org/submit
2. Create/log in to your account
3. Start a new submission
4. Select category: `physics.geo-ph` (Geophysics) or `cs.GE` (Geoscience)
   - Alternative: `stat.ML` (Machine Learning) if emphasizing the PINN aspect
5. Upload files:
   - `paper.tex`
   - `references.bib` (optional; can inline bibliography instead)
   - `figures/week11_full_integration.png`
   - `figures/pinn_training_v3.png`
6. Enter metadata:
   - Title: A Decision-Support Framework for Subsurface Green Hydrogen Storage Site Selection: A Physics-Informed Multi-Objective Optimization Approach
   - Author: Kudakwashe Douglas Marara
   - Abstract: (copy from paper.tex abstract)
   - Subjects: Physics > Geophysics (physics.geo-ph)
7. Submit

## Journal Submission Path (after arXiv)

**Primary target:** Applied Energy (Elsevier)
- URL: https://www.journals.elsevier.com/applied-energy
- Impact Factor: ~11.4
- Accepts: Energy systems, decision support, geospatial optimization, PINNs
- Timeline: ~8-12 weeks first decision

**Backup targets:**
- International Journal of Hydrogen Energy (Elsevier) - hydrogen-specific
- Journal of Energy Storage (Elsevier) - storage-focused
- Energy (Elsevier) - broader energy scope, faster review

## Submission Checklist
- [ ] LaTeX compiles without errors
- [ ] All figures embedded and referenced
- [ ] References formatted correctly
- [ ] arXiv category selected (physics.geo-ph recommended)
- [ ] ORCID iD obtained (optional but recommended)
- [ ] Journal cover letter drafted
- [ ] Journal-specific formatting checked (Elsevier uses elsarticle class typically)
