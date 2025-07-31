# Loan Approval Prediction (Synthetic Label)  

> A beginner-friendly machine learning project that builds a loan approval model using tabular data.  
> Since the provided dataset lacks a real approval/rejection label, a synthetic target is created using simple business rules.  

## 🚀 Project Overview  

This project teaches a machine learning model to decide whether a loan should be approved or rejected based on applicant data.  
Because the original CSV (`fraud.csv`) does **not** contain an actual `Loan_Status` column, we generate a **synthetic approval label** using heuristic rules (i.e., a rule-based "ground truth") and then train models to mimic that decision process.

## 📦 Dataset  

- File expected: `fraud.csv`  
- Columns used (input features):
  - `Loan_ID` (dropped during training)
  - `Gender`
  - `Married`
  - `Dependents`
  - `Education`
  - `Self_Employed`
  - `ApplicantIncome`
  - `CoapplicantIncome`
  - `LoanAmount`
  - `Loan_Amount_Term`
  - `Credit_History`
  - `Property_Area`
- **Synthetic target (`Loan_Status`)** is created with the rule:
  - Credit history must be good (`Credit_History == 1`)  
  - Loan amount to total income ratio < 0.4  
  - Loan term at least 180 months  
  - If all met → approved (`1`), else rejected (`0`)

## 🛠️ Key Steps in the Pipeline  

1. **Data loading & cleaning**  
   - Read `fraud.csv`, strip spaces from column names.  
   - Fill missing numerical values (e.g., median or zero) and missing credit history conservatively.  

2. **Synthetic label creation**  
   - Build `Loan_Status` based on heuristic business rules (as above).  

3. **Feature preparation**  
   - Separate numerical features and categorical features.  
   - Numeric: impute missing values and scale (standardization).  
   - Categorical: impute missing with most frequent and apply one-hot encoding.  

4. **Modeling**  
   - Train two models:
     - Logistic Regression (baseline)  
     - Random Forest (stronger, ensemble)  
   - Use pipelines so preprocessing + model is combined.  

5. **Evaluation**  
   - Train/test split with stratification.  
   - Cross-validation (5-fold ROC AUC) on training data.  
   - Report metrics: accuracy, precision, recall, F1, ROC AUC, confusion matrix.  
   - Extract and display feature importances from Random Forest.  

6. **Prediction**  
   - Show example predictions with probability/confidence.  

7. **Persistence**  
   - Save the trained best pipeline to disk (`.pkl`) for reuse.

## 📈 Metrics Reported  

- Accuracy  
- Precision  
- Recall  
- F1 Score  
- ROC AUC  
- Confusion Matrix  
- Feature Importance (from Random Forest)

## 🧪 Example Usage  

```bash
# Requirements (install once)
pip install pandas scikit-learn matplotlib joblib

# Run your main script (e.g., python loan_approval_pipeline.py)
python loan_approval_pipeline.py
