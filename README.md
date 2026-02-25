# 🏏 IPL Match Win Probability Predictor

A Machine Learning powered web application that predicts the winning probability of an IPL team during a live match situation.

🌐 **Live Demo:**  
https://ipl-match-win-probability-predictor-1.onrender.com/

---

## 📌 Project Overview

This project uses historical IPL match data to predict the probability of a team winning based on real-time match conditions such as runs left, balls left, wickets remaining, and run rates.

The model is integrated into a Flask web application and deployed on Render for public access.

---

## 🚀 Features

- Predicts **Win Probability (%)**
- Predicts **Loss Probability (%)**
- Real-time input-based prediction
- Clean and responsive UI
- Cloud deployed

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **Pandas**
- **Scikit-learn**
- **HTML/CSS**
- **Render (Deployment)**

---

## 📊 Input Parameters

The model takes the following inputs:

- Batting Team
- Bowling Team
- City
- Runs Left
- Balls Left
- Wickets Remaining
- Total Target Runs
- Current Run Rate (CRR)
- Required Run Rate (RRR)

---

## 🧠 Machine Learning Workflow

1. Data Collection & Cleaning  
2. Feature Engineering  
3. Model Training (Classification)  
4. Probability Prediction using `predict_proba()`  
5. Flask Integration  
6. Cloud Deployment  

---

## 💻 Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/krashal02/IPL-Match-Win-Probability-Predictor
cd IPL-Match-Win-Probability-Predictor

``` 

### Install dependencies
pip install -r requirements.txt

### Run the application
python app.py

Open in browser:
http://127.0.0.1:5000/

## 👨‍💻 Author

### Krashal Yaduvanshi


Machine Learning Engineer
