# Application of Deep Learning in the Classification of Basal Cell Carcinoma and Squamous Cell Carcinoma Skin Cancers

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Framework](https://img.shields.io/badge/Framework-PyTorch%20%7C%20TensorFlow-orange)](https://pytorch.org)
[![Status](https://img.shields.io/badge/Status-Research%20in%20Progress-blue)](#)

This repository contains the evaluation results, visual interpretability, and methodology overview for our research project on **automated classification of Basal Cell Carcinoma (BCC) and Squamous Cell Carcinoma (SCC)** using deep convolutional neural network (CNN) architectures.

> ⚠️ **Note:** The full source code and model checkpoints are currently restricted as the accompanying research paper is under peer review. The complete implementation will be made publicly available upon formal publication.

---

## 📌 Abstract & Overview

Non-melanoma skin cancers, specifically **Basal Cell Carcinoma (BCC)** and **Squamous Cell Carcinoma (SCC)**, represent a major healthcare burden worldwide. Early and accurate automated diagnosis via deep learning can significantly reduce clinical workloads and assist dermatologists in diagnostic decision-making.

This project presents an end-to-end deep learning framework designed to classify medical skin lesion images into BCC and SCC categories. The pipeline addresses core challenges in medical computer vision, including severe class imbalance, fine-grained visual features between non-melanoma lesions, and model interpretability.

---

## 🛠️ Methodological Highlights

* **Architectures:** Fine-tuning and comparative evaluation of deep CNN backbones (featuring **Xception** and custom feature extractors).
* **Frameworks:** Implemented using **PyTorch** and **TensorFlow / Keras** for robust model training, preprocessing, and metrics computation.
* **Class Imbalance Mitigation:** Integration of custom focal loss formulations, class-weight balancing, and specialized data augmentation routines.
* **Validation Scheme:** Evaluated via a **Stratified 5-Fold Cross-Validation** strategy to guarantee robust and unbiased generalization.

---

## 📊 Experimental Results

Our optimal fine-tuned backbone demonstrated superior diagnostic performance across key quantitative evaluation metrics (Accuracy, Sensitivity, Specificity, AUC-ROC, and F1-Score).

### Performance Evaluation & ROC Curve
Below are the Receiver Operating Characteristic (ROC) curve and Confusion Matrix for our best-performing model setup:

| ROC Curve | Confusion Matrix |
| :---: | :---: |
| ![ROC Curve](assets/ROC.png) | ![Confusion Matrix](assets/Confusion_Matrix.png) |

---

## 🔍 Model Interpretability (Grad-CAM / Heatmaps)

To verify clinical trustworthiness and ensure the neural network focuses on actual dermoscopic lesion attributes rather than image artifacts, we utilized **Grad-CAM (Gradient-weighted Class Activation Mapping)**.

| Original Lesion Image | Grad-CAM Heatmap Overlay |
| :---: | :---: |
| ![Original Lesion](assets/ISIC_0054935.jpg) | ![Grad-CAM Heatmap](assets/ISIC_0054935_cam.jpg) |

---

## 🏥 Real-World Clinical Data Collection

We are actively expanding our research through real-world clinical data acquisition:
* **Clinical Partner:** Razi Hospital, Tehran, Iran.
* **Lead Supervisor:** [Dr. Maryam Nasimi](https://scholar.google.com/citations?user=MPwW1YwAAAAJ&hl=en)
* **Status:** In progress (Collecting high-quality annotated BCC and SCC clinical cases).
* **Data Release:** This clinical dataset will be curated, anonymized, and made **publicly available** to the scientific community in the near future.

---

## 🚀 Ongoing & Future Work

* **EfficientNetV3 Assessment:** Evaluation of advanced deep learning frameworks (such as **EfficientNetV3**) on both benchmark datasets and incoming clinical cohorts.
* **Full Codebase Release:** End-to-end training, preprocessing scripts, and pre-trained model weights will be released post-publication.

---

## ✒️ Citation & Contact

If you have questions regarding this ongoing project or collaboration inquiries, feel free to reach out or open an issue.
