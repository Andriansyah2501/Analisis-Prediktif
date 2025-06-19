import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model dan scaler
model = joblib.load("model_rf_telco.pkl")
scaler = joblib.load("scaler_telco.pkl")

st.title("📉 Prediksi Churn Pelanggan Telco")

st.markdown("""
Aplikasi ini memprediksi kemungkinan pelanggan akan **berhenti berlangganan** berdasarkan informasi pelanggan yang dimasukkan.  
Model yang digunakan adalah **Random Forest** yang telah dilatih dari dataset pelanggan Telco.
""")

# Fungsi input user
def user_input():
    tenure = st.slider("Lama Berlangganan (bulan)", 0, 72, 12)
    monthly_charges = st.slider("Biaya Bulanan", 0.0, 150.0, 70.0)
    total_charges = st.slider("Total Biaya", 0.0, 10000.0, 1000.0)
    contract = st.selectbox("Jenis Kontrak", ["Month-to-month", "One year", "Two year"])
    internet = st.selectbox("Jenis Internet", ["DSL", "Fiber optic", "No"])
    paperless = st.selectbox("Tagihan Tanpa Kertas?", ["Yes", "No"])
    tech_support = st.selectbox("Dukungan Teknis Aktif?", ["Yes", "No"])
    online_security = st.selectbox("Online Security Aktif?", ["Yes", "No"])

    # Encoding manual fitur one-hot
    data = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "Contract_One year": 1 if contract == "One year" else 0,
        "Contract_Two year": 1 if contract == "Two year" else 0,
        "InternetService_Fiber optic": 1 if internet == "Fiber optic" else 0,
        "InternetService_No": 1 if internet == "No" else 0,
        "OnlineSecurity_Yes": 1 if online_security == "Yes" else 0,
        "TechSupport_Yes": 1 if tech_support == "Yes" else 0,
        "PaperlessBilling_Yes": 1 if paperless == "Yes" else 0,
    }

    return pd.DataFrame([data])

# Ambil input user
input_df = user_input()

# Normalisasi & prediksi
scaled_input = scaler.transform(input_df)
prediction = model.predict(scaled_input)
prob = model.predict_proba(scaled_input)[0][1]

# Tampilkan hasil
st.subheader("Hasil Prediksi:")
if prediction[0] == 1:
    st.error(f"Pelanggan **berisiko churn** dengan probabilitas {prob:.2%}")
else:
    st.success(f"Pelanggan **tidak berisiko churn** dengan probabilitas churn {prob:.2%}")
