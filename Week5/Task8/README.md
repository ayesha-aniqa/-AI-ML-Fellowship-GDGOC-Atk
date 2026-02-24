# Logistic Regression Implementation
## (From Scratch + Scikit-Learn)

---

## Task

- Implement Logistic Regression (From Scratch + Scikit-Learn)
- Math behind Model

---

## Concepts Covered

- Supervised Learning
- Binary Classification
- Sigmoid Function
- Binary Cross-Entropy (Log Loss)
- Gradient Descent Optimization
- Decision Boundary
- Model Evaluation (Accuracy, Confusion Matrix)

---

## Implementation

### 1. Logistic Regression from Scratch

The scratch implementation includes:

- Manual implementation of the sigmoid function
- Binary cross-entropy loss calculation
- Gradient descent optimization
- Weight and bias updates
- Custom prediction function

Mathematical model:

z = w^T x + b  
ŷ = 1 / (1 + e^-z)

Update rule:

w = w - α (1/m) X^T (ŷ - y)  
b = b - α (1/m) Σ (ŷ - y)

---

### 2. Logistic Regression using Scikit-Learn

Implemented using:

```python
from sklearn.linear_model import LogisticRegression
```

Used for:

- Performance comparison
- Validation of scratch implementation
- Efficient optimized training

---

## Author

Ayesha Aniqa - AI/ML Fellowship
