# Model Evaluation Activity  
## Linear Regression & Logistic Regression

This project demonstrates the understanding and practical implementation of:

- Regression & its evaluation techniques  
- Classification & its evaluation techniques  
- Bias–Variance tradeoff  
- Underfitting vs Overfitting  

Both models are implemented **from scratch** and using **Scikit-Learn**, followed by detailed performance evaluation.

---

# 1. Understanding Regression Evaluation Techniques
## Evaluation Techniques Used

To evaluate regression models, the following metrics were applied:

- **MAE (Mean Absolute Error)**  
- **MSE (Mean Squared Error)**  
- **RMSE (Root Mean Squared Error)**  
- **R² Score**  
- **Train vs Test Score Comparison**

### Working of Evaluation Metrics

- **MAE** → Measures average absolute error between actual and predicted values.  
- **MSE** → Penalizes larger errors by squaring them.  
- **RMSE** → Square root of MSE (interpretable in original unit).  
- **R² Score** → Measures how well the model explains variance (0 to 1).  
- **Train vs Test Comparison** → Helps detect overfitting or underfitting.  

---

## Overfitting & Underfitting in Regression

- **Overfitting** → High training score, low testing score (High Variance)  
- **Underfitting** → Low training & testing score (High Bias)  
- **Balanced Model** → Similar and high train & test performance  

---

## Regression Notebook

Colab Notebook:  
**[(https://colab.research.google.com/drive/1i2zPwQeAXmEZRDrc_fSQzpYWKd6b_YJ1?usp=sharing)]**

---

# 2️. Understanding Classification & Its Evaluation Techniques
## Evaluation Techniques Used

To evaluate classification models, the following metrics were applied:

- **Accuracy**  
- **Precision**  
- **Recall**  
- **F1 Score**  
- **Confusion Matrix**  
- **Train vs Test Accuracy Comparison**

---

## Working of Evaluation Metrics

- **Accuracy** → Correct predictions / Total predictions  
- **Precision** → Out of predicted positives, how many were correct  
- **Recall** → Out of actual positives, how many were correctly predicted  
- **F1 Score** → Harmonic mean of Precision and Recall  
- **Confusion Matrix** → Displays TP, TN, FP, FN values  

---

## Bias–Variance in Classification

- **High Bias (Underfitting)** → Model too simple, poor performance  
- **High Variance (Overfitting)** → Model memorizes training data  
- **Balanced Model** → Good generalization on unseen data  

---

## Classification Notebook

Colab Notebook:  
 **[https://colab.research.google.com/drive/1D0ARNMHM8fGV6cnkDxG4XN-2WAbtMpss?usp=sharing]**

---

# 🚀 Conclusion

This activity strengthened understanding of:

- Regression & Classification evaluation techniques  
- Practical metric comparison  
- Bias–Variance tradeoff  
- Identifying underfitting and overfitting  
- Model performance analysis using multiple algorithms  

