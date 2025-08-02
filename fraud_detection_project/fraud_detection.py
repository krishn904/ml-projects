# Install required packages using the terminal, not inside the Python script
# import pip  # Only needed for programmatic installs, not recommended here
from pyexpat import model
import streamlit as st
import pandas as pd 
import joblib
model = joblib.load('fraud_detection_model.pkl')
st.title('Fraud Detection App')
st.markdown('Enter the transaction details and use the predict button to check')

st.divider()
transaction_type = st.selectbox('Transaction Type', ['Payment', 'Transfer', 'Cash_out', 'Deposit'])

amount= st.number_input('Transaction Amount', min_value=1000.0)
oldbalanceOrg= st.number_input('Old Balance (sender)', min_value=0.0, value=10000.0)
newbalanceOrig= st.number_input('New Balance (sender)', min_value=0.0, value=9000.0)
oldbalanceDest= st.number_input('Old Balance (receiver)', min_value=0.0, value=0.0)
newbalanceDest= st.number_input('New Balance (receiver)', min_value=0.0, value=0.0)

if st.button('Predict'):
    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })
    # Make predictions
    prediction = model.predict(input_data)[0]
    st.subheader(f"prediction:{int(prediction)}")
    if prediction == 1:
        st.error("This transaction is likely fraudulent.")
    else:
        st.success("This transaction is likely legitimate.")    
