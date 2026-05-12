# 🏋️ Gym Churn Prediction System

An end-to-end Machine Learning project for predicting gym customer churn using advanced feature engineering, exploratory data analysis, hyperparameter tuning, SMOTE balancing, and Flask deployment.

---

# 📌 Project Overview

Customer churn is one of the biggest challenges for gyms and fitness businesses. Retaining existing members is significantly more cost-effective than acquiring new customers.

This project builds a complete churn prediction pipeline that helps gyms:

- Predict customers likely to churn
- Identify high-risk members early
- Improve customer retention strategies
- Understand behavioral patterns affecting churn

The project includes:

- ✅ Exploratory Data Analysis (EDA)
- ✅ Feature Engineering
- ✅ Outlier Handling
- ✅ SMOTE Balancing
- ✅ Hyperparameter Tuning
- ✅ Model Comparison
- ✅ XGBoost-Based Churn Prediction
- ✅ Flask Deployment
- ✅ Pickle Model Export

---

# 📂 Repository Structure

```bash
├── data/
│   └── gym_members_dataset.csv
│
├── notebooks/
│   └── gym_churn_analysis.ipynb
│
├── models/
│   └── gym_churn_model.pkl
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── Gym_Churn_EDA_Presentation.pptx
```

---

# 🎯 Problem Statement

Gym businesses often struggle with customer retention. Many members stop attending after a short period due to:

- Low engagement
- Inconsistent workout habits
- Seasonal motivation
- Weak membership commitment

The objective of this project is to predict whether a customer will churn using behavioral and demographic data.

### Target Variable

```python
Churn
```

- `Yes` → Customer likely to leave
- `No` → Customer likely to stay

---

# 📊 Exploratory Data Analysis (EDA)

The project includes extensive EDA to understand customer behavior and churn patterns.

## Key EDA Analyses

- Churn Distribution
- Age Group vs Churn
- Membership Type vs Churn
- Joining Month vs Churn
- Workout Engagement vs Churn
- Correlation Heatmap
- Feature Importance Analysis

---

# 📌 Key Findings

- Customers with higher gym engagement are less likely to churn.
- Frequent monthly visits strongly reduce churn.
- Premium memberships show better retention.
- Young adults show higher churn probability.
- Long-term members are more likely to stay.

---

# 📑 EDA Results & Findings

Detailed visualizations, findings, and business insights are available in:

```bash
Gym_Churn_EDA_Presentation.pptx
```

inside this repository.

---

# ⚙️ Machine Learning Pipeline

```text
Data Cleaning
      ↓
Feature Engineering
      ↓
EDA & Visualization
      ↓
Outlier Handling
      ↓
Preprocessing
      ↓
Train-Test Split
      ↓
SMOTE Balancing
      ↓
Hyperparameter Tuning
      ↓
Model Selection
      ↓
Final Model Training
      ↓
Pickle Export
      ↓
Flask Deployment
```

---

# 🧠 Feature Engineering

Several new features were engineered to improve churn prediction performance.

## Engineered Features

### 1. Membership Duration

:contentReference[oaicite:0]{index=0}

Measures customer retention duration.

---

### 2. Workout Engagement Score

:contentReference[oaicite:1]{index=1}

Captures overall gym engagement.

---

### 3. Calories Per Visit

:contentReference[oaicite:2]{index=2}

Measures workout efficiency.

---

### 4. Joining Season

Customers were grouped by joining season:

- Winter
- Summer
- Monsoon
- Autumn

---

### 5. Age Group

Customers were segmented into:

- Teenagers
- Young Adults
- Adults
- Middle Age
- Senior Citizens

---

# 🧹 Data Preprocessing

The preprocessing pipeline includes:

- Missing Value Imputation
- Standard Scaling
- One-Hot Encoding
- Feature Selection

Implemented using:

- `ColumnTransformer`
- `Pipeline`
- `StandardScaler`
- `OneHotEncoder`

---

# ⚖️ Handling Imbalanced Data

The dataset had class imbalance:

```python
No  -> Majority Class
Yes -> Minority Class
```

To address this:

```python
SMOTE (Synthetic Minority Oversampling Technique)
```

was used to generate synthetic minority samples.

This improved:

- Recall
- ROC-AUC
- Minority class prediction

---

# 🤖 Models Used

| Model | Purpose |
|---|---|
| Logistic Regression | Baseline Linear Model |
| Random Forest | Ensemble Tree Model |
| Gradient Boosting | Sequential Boosting |
| SVM | Margin-Based Classification |
| XGBoost | Advanced Gradient Boosting |

---

# 🔍 Hyperparameter Tuning

Hyperparameter tuning was performed using:

```python
GridSearchCV
```

Evaluation Metric:

```python
ROC-AUC
```

Cross Validation:

```python
Stratified K-Fold Cross Validation
```

---

# 🏆 Best Model

The best-performing model was:

```python
XGBoost Classifier
```

## Why XGBoost?

- Handles nonlinear relationships well
- Performs strongly on structured/tabular data
- Works effectively with SMOTE-balanced datasets
- Provides strong predictive capability
- Better generalization on churn problems

---

# 📈 Model Evaluation

The final model was evaluated using:

- Accuracy
- ROC-AUC Score
- Classification Report
- Confusion Matrix
- Feature Importance

---

# 💾 Model Export

The trained model is exported as:

```bash
gym_churn_model.pkl
```

using:

```python
pickle
```

---

# 🚀 Flask Deployment

A production-ready Flask web application was built for churn prediction.

The app allows users to:

- Enter customer information
- Predict churn probability
- View retention predictions instantly

---

# ▶️ How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run the Notebook FIRST

Before running the Flask app, you MUST run:

```bash
gym_churn_analysis.ipynb
```

This step:

- trains the model
- performs hyperparameter tuning
- generates the pickle file

```bash
gym_churn_model.pkl
```

Without the pickle file, the Flask application will not work.

---

## 4️⃣ Run Flask Application

After generating the pickle file:

```bash
python app.py
```

---

## 5️⃣ Open Browser

```bash
http://127.0.0.1:5000/
```

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Data Analysis

- Pandas
- NumPy

## Visualization

- Matplotlib
- Seaborn

## Machine Learning

- Scikit-learn
- XGBoost
- Imbalanced-learn

## Deployment

- Flask

---

# 📌 Future Improvements

Possible future enhancements:

- Deploy on Render / AWS / Heroku
- Use SHAP for explainability
- Add Deep Learning models
- Build real-time dashboards
- Integrate with CRM systems
- Automated retention campaigns

---

# 📜 License

This project is open-source and available for educational and research purposes.

---

# 👨‍💻 Author

Developed as an end-to-end Machine Learning and Flask deployment project for Gym Customer Churn Prediction.
