
# 💳 Credit Risk Prediction System

An end-to-end Machine Learning application that predicts whether a loan applicant is **Low Risk** or **High Risk** based on customer financial and demographic information. The project uses a **Logistic Regression** model trained on the German Credit Dataset and provides an interactive interface built with **Streamlit** for real-time predictions.

---

## 🚀 Features

- Predict customer credit risk in real time
- Interactive Streamlit web application
- Confidence score for each prediction
- User-friendly dashboard
- Clean and responsive interface
- Pre-trained Logistic Regression model

---

## 🖥️ Demo

Run the application locally:

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
Credit_risk_prediction/
│
├── app.py                  # Streamlit UI
├── model.pkl               # Trained ML model
├── columns.pkl             # Feature columns
├── german_credit_data.csv  # Dataset
├── credit-scoring-with-fairness.ipynb
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 📊 Machine Learning Workflow

1. Data preprocessing
2. Feature engineering
3. One-hot encoding
4. Model training using Logistic Regression
5. Model serialization using Joblib
6. Interactive prediction using Streamlit

---

## 📸 Application Preview

> Add screenshots of your application here.

Example:

```
screenshots/home.png
screenshots/prediction.png
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AkashLavudya/Credit_risk_prediction.git
```

Navigate to the project directory:

```bash
cd Credit_risk_prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📈 Model

- **Algorithm:** Logistic Regression
- **Problem Type:** Binary Classification
- **Dataset:** German Credit Dataset

---

## 🎯 Future Improvements

- Compare multiple machine learning models
- Explain predictions using SHAP values
- Deploy the application on Streamlit Community Cloud
- Add advanced risk analytics dashboard
- Support batch prediction using CSV upload

---

## 👨‍💻 Author

**Akash Lavudya**

GitHub: https://github.com/AkashLavudya

LinkedIn: *(Add your LinkedIn profile here)*

---

## 📄 License

This project is intended for educational and portfolio purposes.

