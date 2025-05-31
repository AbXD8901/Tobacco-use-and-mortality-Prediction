

# 🚬 Tobacco Use and Mortality Prediction

This project aims to model and analyze the relationship between **tobacco consumption patterns** and **mortality** using machine learning. The goal is to predict whether an individual is likely to face mortality based on key tobacco-related factors and associated health data.

---

## 📘 Project Overview

Tobacco use is one of the leading causes of preventable death worldwide. This project leverages structured historical data to:

* Analyze the effect of tobacco and related behaviors on health outcomes.
* Build a classification model to **predict mortality (Yes/No)**.
* Provide insights that support **public health interventions** and awareness campaigns.

---

## 📊 Dataset Description

The dataset contains individual-level or aggregated demographic records. Some fields were derived or filtered from broader datasets for analysis. Key features include:

| Feature              | Description                                        |
| -------------------- | -------------------------------------------------- |
| `Age`                | Age of the individual                              |
| `Sex`                | Male/Female                                        |
| `Year`               | Year of record                                     |
| `Cigarettes Per Day` | Average daily cigarette use                        |
| `Tobacco Type`       | E.g., Cigarettes, Bidis, Chewing Tobacco           |
| `Smoker Category`    | Never, Former, Current                             |
| `Chronic Conditions` | Presence of chronic illnesses (binary/categorical) |
| `Mortality`          | **Target** – whether the individual died (Yes/No)  |

---

## 🧪 Methodology

### 1. Data Preprocessing

* Merged relevant datasets and filtered for valid mortality information.
* Handled missing values and encoded categorical features.
* Normalized numeric variables where necessary.

### 2. Exploratory Data Analysis (EDA)

* Trend analysis of smoking habits across years.
* Correlation between tobacco usage and mortality.
* Gender- and age-wise breakdown of smoking effects.

### 3. Modeling

* **Classification task**: Predict `Mortality` (Yes/No)
* Models tested:

  * Logistic Regression
  * Random Forest
  * XGBoost
* Evaluation metrics:

  * Accuracy
  * Precision, Recall, F1-Score
  * ROC-AUC
  * Confusion Matrix

---

## 📈 Results

* **Best performing model**: Random Forest (or XGBoost if applicable)
* Achieved accuracy of **X%**, with strong recall on mortality cases.
* Important features:

  * Cigarette use intensity
  * Age and chronic conditions
  * Smoker status

---

## 🧠 Insights

* A strong positive correlation was observed between long-term tobacco use and mortality.
* Former smokers showed lower mortality risk than current users, supporting cessation benefits.
* Public health strategies should focus on reducing high-risk categories (current heavy smokers, older adults).

---

## 📁 Project Structure

```
tobacco-mortality-prediction/
│
├── data/                   # Raw and cleaned datasets
├── notebooks/              # EDA and modeling notebooks
├── models/                 # Trained models
├── scripts/                # Data processing and training scripts
├── plots/                  # Visualizations
├── main.py                 # Main pipeline to run everything
├── requirements.txt        # Python dependencies
└── README.md               # Documentation
```

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/tobacco-mortality-prediction.git
cd tobacco-mortality-prediction
pip install -r requirements.txt
```

---

## 🛠 Technologies Used

* Python (Pandas, NumPy, Scikit-learn)
* XGBoost, Random Forest
* Matplotlib, Seaborn
* Jupyter for EDA and prototyping

---
