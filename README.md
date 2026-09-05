# Application of Deep Learning in the Classification of Basal Cell Carcinoma and Squamous Cell Carcinoma Skin Cancers

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Framework](https://img.shields.io/badge/Framework-TensorFlow%20%2F%20Keras-orange)](https://tensorflow.org)
[![Status](https://img.shields.io/badge/Status-Research%20in%20Progress-blue)](#)

This repository contains the evaluation results, visualization, and abstract for our research project on **automated classification of Basal Cell Carcinoma (BCC) and Squamous Cell Carcinoma (SCC)** using deep convolutional neural network architectures.

> ⚠️ **Note:** The full source code and model checkpoints are currently restricted as the accompanying research paper is under peer review. The complete implementation will be made publicly available upon formal publication.

---

## 📌 Abstract & Overview

Non-melanoma skin cancers, specifically **Basal Cell Carcinoma (BCC)** and **Squamous Cell Carcinoma (SCC)**, represent a major healthcare burden worldwide. Early and accurate automated diagnosis via deep learning can significantly reduce clinical workloads and assist dermatologists.

In this work, we employ a fine-tuned **Xception** architecture integrated with custom focal loss functions, class-weighting mechanisms, and specialized data augmentation techniques to handle class imbalance effectively. Model evaluation is conducted using a Stratified 5-Fold Cross-Validation strategy.

---

## 📊 Experimental Results

Our optimal model based on the **Xception** backbone demonstrated superior performance across key evaluation metrics (Accuracy, Sensitivity, Specificity, AUC-ROC, and F1-Score).

### Performance Evaluation & ROC Curve
Below are the Receiver Operating Characteristic (ROC) curve and Confusion Matrix for our best-performing fold/model:

| ROC Curve | Confusion Matrix |
| :---: | :---: |
| ![ROC Curve](assets/roc_curve.png) | ![Confusion Matrix](assets/confusion_matrix.png) |

---

## 🔍 Model Interpretability (Grad-CAM / Heatmaps)

To ensure clinical trustworthiness and verify that the deep neural network focuses on clinically relevant lesion patterns rather than background artifacts, we applied Grad-CAM activation mapping.

| Original Lesion Image | Heatmap Overlay |
| :---: | :---: |
| ![Original Lesion](assets/heatmap_sample.png) | *(Visual explanation showing regions of high focus)* |

---

## 🏥 Real-World Clinical Data Collection

We are actively expanding our research through real-world clinical data acquisition:
* **Clinical Partner:** Razi Hospital, Tehran, Iran.
* **Lead Supervisor:** [Dr. Maryam Nasimi](https://scholar.google.com/citations?user=MPwW1YwAAAAJ&hl=en)
* **Status:** In progress (Collecting high-quality annotated BCC and SCC clinical cases).
* **Data Release:** This clinical dataset will be curated, anonymized, and made **publicly available** to the scientific community in the near future.

---

## 🚀 Ongoing & Future Work

* **EfficientNetV3 Assessment:** Evaluation of the newly proposed **EfficientNetV3** architecture on our benchmark and clinical datasets is currently underway to evaluate potential trade-offs in computational efficiency and diagnostic precision.
* **Full Codebase Release:** Complete training and evaluation scripts, along with pre-trained weights, will be published here post-publication.

---

## ✒️ Citation & Contact

If you have questions regarding this ongoing project, feel free to reach out or open an issue.
