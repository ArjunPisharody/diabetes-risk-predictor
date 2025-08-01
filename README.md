# diabetes-risk-predictor
# 🩺 Diabetes Risk Prediction App

A simple and interactive Streamlit web app that predicts whether a person is at risk of diabetes based on medical inputs. The model is trained using the popular Pima Indians Diabetes Dataset.

---

## 🔍 Features

- Input fields for 8 key medical parameters
- Predicts **High Risk** or **Low Risk** of diabetes using a trained Random Forest model
- Clean and responsive Streamlit UI
- Easy to run locally or deploy online

---

## 📊 Dataset

- **Source:** [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- `diabetes.csv` contains:
  - Pregnancies
  - Glucose
  - BloodPressure
  - SkinThickness
  - Insulin
  - BMI
  - DiabetesPedigreeFunction
  - Age
  - Outcome (0 = No Diabetes, 1 = Diabetes)

---

## 🧠 Model Used

- **Algorithm:** Random Forest Classifier (from `scikit-learn`)
- **Trained using:** `train_model.py`
- **Saved model:** `model.pkl`



