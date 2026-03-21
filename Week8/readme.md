# 🧠 Deep Learning Foundations: From Math to Vision

This repository contains a step-by-step journey through Deep Learning, starting from a "from-scratch" implementation of backpropagation to building high-performance Convolutional Neural Networks (CNNs).

---

## 🛠️ Technical Deep Dive

### 1. ANN for Handwritten Digit Recognition
Using the **MNIST dataset**, this module focuses on data preprocessing and standard Artificial Neural Network (ANN) architecture.
* **Preprocessing:** Normalizing pixel values (0-255 to 0-1) for faster convergence.
* **Architecture:** Includes `Flatten`, `Dense` layers with `ReLU` activation, and `Dropout` to prevent overfitting.
* **Output:** 10 neurons with `Softmax` for multi-class classification.

### 2. Backpropagation from Scratch (NumPy)
To understand the "Black Box" of AI, I implemented a 3-layer network to solve the **XOR Problem**. 
* **Forward Pass:** Input -> Hidden Layer (Sigmoid) -> Output Layer.
* **Backward Pass:** Calculating gradients manually using the **Chain Rule** to update weights.
* **Goal:** Demonstrating how a model minimizes error over thousands of iterations (epochs) without high-level libraries.

### 3. Convolutional Neural Networks (CNN)
The final evolution of this project uses CNNs to achieve superior accuracy by preserving the spatial structure of images.
* **Conv2D Layers:** Automatically detects features like edges and textures.
* **Pooling:** Uses `MaxPooling2D` to reduce spatial dimensions while keeping critical info.
* **Result:** Significantly higher accuracy than standard ANN on image data.

---

## 📊 Visualizing Results
The project includes a visualization script using **Matplotlib** to display:
* Training Loss & Accuracy curves.
* Sample Predictions (viewing the digit image vs. the model's guess).

---
