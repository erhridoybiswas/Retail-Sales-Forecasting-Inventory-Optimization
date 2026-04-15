# 🛒 Retail Sales Forecasting & Inventory Optimization System

## 📌 Overview
This project is a full-stack data science application that forecasts product demand and optimizes inventory decisions for retail businesses. 
It combines Machine Learning with business logic to simulate real-world retail analytics.

---

## 🎯 Problem Statement
Retail companies often struggle with:
- ❌ Stockouts (lost sales)
- ❌ Overstock (high holding cost)
- ❌ Poor demand planning

This system solves these issues using forecasting and inventory optimization.

---

## 🚀 Key Features
- 📊 Sales Forecasting using Machine Learning
- 📦 Inventory Optimization (Safety Stock, ROP, EOQ)
- 🌐 Web Dashboard (Flask)
- 📈 Interactive Charts (Chart.js)
- 🔄 Real-time predictions

---

## 🧠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Flask
- HTML, CSS
- Chart.js

---

## 🏗️ Architecture
Data → Preprocessing → Feature Engineering → Model → Forecast → Inventory Logic → Dashboard

---

## 📁 Project Structure

Retail-WebApp/
├── app.py
├── data/
├── models/
├── src/
├── templates/
├── static/
└── requirements.txt


---

## ⚙️ Installation
```bash
pip install -r requirements.txt
▶️ Run the Project
python src/generate_data.py
python src/data_prep.py
python src/train_model.py
python app.py

Open browser:
http://127.0.0.1:5000

📊 Output
Forecast Graph 📈
Sales Table
Inventory Recommendation:
Safety Stock
Reorder Point
EOQ
Order Quantity

💼 Business Value
Improves demand planning
Reduces stockouts
Optimizes inventory cost
Helps decision-making

🎓 Learning Outcomes
End-to-end ML pipeline
Forecasting techniques
Inventory optimization logic
Full-stack deployment

👨‍💻 Author
*Hridoy Biswas*
