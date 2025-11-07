# 🌿 Plant Disease Prediction System

A deep learning-based web application that detects and classifies plant leaf diseases using **Convolutional Neural Networks (CNNs)** built with **TensorFlow**.  
Developed as part of an academic internship at **ORMVA Tafilalet (2024)**.

---

## 🚀 Project Overview

This project aims to assist farmers and researchers by providing an intelligent tool to identify plant diseases early through image recognition.  
Users can upload a leaf image, and the system will predict whether it is **healthy** or affected by a **specific disease**.

---

## 🧠 Key Features

- 🪴 **CNN Model:** Custom TensorFlow architecture for image classification  
- 🧼 **Preprocessing:** Image normalization, resizing, and data augmentation  
- 🧪 **Evaluation:** Accuracy, loss, confusion matrix  
- 🌐 **Web App:** User interface built with **Django**, supporting login and prediction views  
- 💾 **Database:** Stores user uploads and prediction results  

---

## 🛠️ Technologies Used

| Category | Tools / Libraries |
|-----------|-------------------|
| Deep Learning | TensorFlow, Keras |
| Web Framework | Django |
| Data Processing | NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |
| Image Handling | OpenCV |
| Deployment | PythonAnywhere / Localhost |

---

## 📊 Model Performance

| Metric | Result |
|--------|---------|
| Accuracy | ~93% |
| Validation Loss | 0.21 |
| Dataset Size | 10,000+ labeled images |

---

## 🧩 Dataset

The model was trained on a public dataset containing images of **healthy and diseased plant leaves**, including multiple species such as tomato, corn, and potato.  
Each image is labeled by disease category.

Dataset examples can be found on [Kaggle - Plant Village Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease).

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/zineb3103/Pr-diction-des-maladies-des-plantes.git
cd plant-disease-prediction
