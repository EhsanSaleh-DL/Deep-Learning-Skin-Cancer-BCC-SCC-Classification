---

## 📁 Repository Structure & Assets

To provide full transparency on our model's performance and clinical interpretability prior to full code release, the `assets/` directory contains key experimental visualizations and evaluation metrics generated during our experiments:

```text
assets/
├── roc_curve.png          # ROC-AUC performance curves across cross-validation folds
├── confusion_matrix.png   # Confusion matrix showcasing BCC vs. SCC diagnostic precision
├── heatmap_sample.png     # Grad-CAM visual explanations (heatmaps) highlighting lesion ROI
