

# 🌸 Iris Flower Classifier & Student Exam Predictor (Streamlit + Pickle)

An interactive web app to **classify iris flowers** and **predict student exam outcomes** using machine learning.
The app performs EDA, trains a **Decision Tree Classifier**, evaluates metrics, and provides predictions via a Streamlit interface.

---

## ⚡ Live Demo

Try the app instantly: [Iris Flower & Exam Predictor](https://svm--decision-tree-task-pkzbnhnkqpnpi48c74kqwv.streamlit.app/) 🚀

---

## 📂 Project Structure

```
iris_exam_app/
│── app.py              # Streamlit app entrypoint
│── train.py            # Train the Decision Tree model
│── model.pkl           # Saved Decision Tree model after training
│── requirements.txt    # Dependencies for Streamlit & ML
│── data/
│     ├── iris.csv       # Sample Iris dataset
│     └── student.csv    # Student exam dataset
```

---

## 🛠️ Setup Locally

```bash
# Clone repository
git clone https://github.com/yourusername/iris-exam-app
cd iris-exam-app

# (Optional) Create virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🎯 Train the Model

```bash
python train.py
```

This will:

* Generate `model.pkl`
* Perform **EDA** for both datasets
* Train a **Decision Tree Classifier** on:

  * Features for student exam: `hours_studied`, `sleep_hours`, `class_attendance`
  * Target: `Pass (1)` / `Fail (0)`
* Evaluate metrics: **Accuracy, Precision, Recall, F1 Score**
* Visualize the decision tree

Example prediction:

```python
# Predict if a student with hours_studied=8, sleep_hours=6, attendance=80% passes
```

---

## 🌐 Run the Streamlit App

```bash
streamlit run app.py
```

The app allows you to:

* Input iris flower features → predict species
* Input student data → predict exam pass/fail
* View interactive charts and decision tree visualization

---

## 📊 Features

* **Data Exploration:** Automated EDA on datasets
* **Decision Tree Classifier:** Predicts student outcomes
* **Iris Classification:** Simple, accurate flower predictor
* **Streamlit UI:** Easy-to-use, interactive interface
* **Pickle Model:** Load and save trained models efficiently

---

## 📈 Evaluation

* Confusion Matrix
* Accuracy, Precision, Recall, F1
* Decision Tree visualization

---

## 🧰 Tech Stack

* Python 3.x
* Pandas, NumPy, Matplotlib, Seaborn
* Scikit-learn
* Streamlit
* Pickle

---

## 🚀 Next Steps

* Add **hyperparameter tuning** for better model performance
* Include more **ML algorithms** for comparison
* Deploy on **Hugging Face Spaces** or **Streamlit Cloud**

---


