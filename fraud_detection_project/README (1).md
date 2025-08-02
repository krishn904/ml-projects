# 💳 Fraud Detection Machine Learning App

## 📌 Overview
A **Machine Learning-powered Fraud Detection System** that predicts whether a given transaction is fraudulent or legitimate. Built with a pre-trained model (`fraud_detection_model.pkl`) and an interactive **Streamlit** web app (`fraud_detection.py`) for real-time inference.

## ⚙️ Features
- Interactive UI using Streamlit  
- Custom transaction inputs: type, amount, sender/receiver balances  
- Instant prediction: Fraud (1) vs Legitimate (0)  
- Pre-trained model for quick deployment  

## 🧠 Model Details
- **Algorithm**: (e.g., RandomForestClassifier — replace with actual used model)  
- **Target Variable**: `isFraud` (`1` = Fraud, `0` = Legitimate)  
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1 Score (see notebook for details)  

## 🛠️ Installation & Setup

### Clone & enter project
```bash
git clone https://github.com/your-username/fraud-detection-app.git
cd fraud-detection-app
```

### (Optional) Virtual environment
```bash
python -m venv .venv
# Activate:
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

### Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### Example `requirements.txt`
```
streamlit
pandas
joblib
scikit-learn
```

## 🚀 Running the App
```bash
streamlit run fraud_detection.py
```
Then open the browser at `http://localhost:8501` to interact.

## 📊 Usage
1. Choose **Transaction Type** (Payment, Transfer, Cash_out, Deposit)  
2. Input:
   - Amount  
   - Sender old/new balance  
   - Receiver old/new balance  
3. Click **Predict**  
   - Shows fraud alert if prediction is `1`  
   - Shows safe confirmation if prediction is `0`  

## 📈 Model Training
Full preprocessing, feature engineering, training, tuning, and evaluation lives in the Jupyter notebook: `project_ai_mi_fraud_detection.ipynb`.

## 📌 Example Prediction
| Type     | Amount | Old Sender Balance | New Sender Balance | Prediction |
|----------|--------|--------------------|--------------------|------------|
| Transfer | 5000   | 10000              | 5000               | Fraud (1)  |

## 📜 License
MIT License

## 🙌 Acknowledgements
- Streamlit for the UI  
- Pandas for data handling  
- Scikit-learn (or used framework) for model training  
