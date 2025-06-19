# Laporan Proyek Machine Learning - Andrian Syah

# 📊 Telco Customer Churn Prediction (Real Dataset)

Notebook ini bertujuan untuk memprediksi pelanggan yang kemungkinan besar akan berhenti berlangganan (churn) dari layanan telekomunikasi menggunakan data nyata dari IBM Telco Customer Churn dataset.

---

## 🧠 Tujuan Proyek

- Membangun model machine learning untuk memprediksi pelanggan yang akan churn
- Mengidentifikasi fitur penting yang menyebabkan churn
- Menyediakan visualisasi performa model dan interpretasi prediktor

---

## 🗂 Dataset

- **Sumber:** IBM Sample Dataset  
- **Link Dataset:** [WA_Fn-UseC_-Telco-Customer-Churn.csv](https://raw.githubusercontent.com/treselle-systems/customer_churn_analysis/master/WA_Fn-UseC_-Telco-Customer-Churn.csv)  
- **Jumlah Data:** 7.043 baris dan 21 kolom
- **Target:** `Churn` (Yes/No)

---

## ⚙️ Tahapan Analisis

### 1. Import Library
Digunakan library standar seperti Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn.

### 2. Load dan Eksplorasi Dataset
Dataset diunduh langsung dari GitHub dan ditampilkan untuk eksplorasi awal.

### 3. Data Cleaning
- Konversi kolom `TotalCharges` ke tipe numerik
- Hapus data kosong
- Hapus kolom ID yang tidak relevan

### 4. Feature Engineering
- Menambahkan fitur baru `AvgChargesPerTenure` = TotalCharges / Tenure

### 5. Encoding dan Normalisasi
- One-hot encoding untuk variabel kategorikal
- StandardScaler untuk normalisasi fitur numerik

### 6. Split Data
- Split ke dalam data latih dan data uji (80:20)

### 7. Model Training
- Menggunakan **Random Forest Classifier** sebagai model utama

### 8. Evaluasi Model
- Classification Report (Accuracy, Precision, Recall, F1-score)
- Confusion Matrix
- ROC Curve dan nilai AUC

### 9. Interpretasi Fitur
- Menampilkan 10 fitur terpenting berdasarkan feature importance Random Forest

---

## 📈 Hasil Singkat

- **Akurasi:** ~80% (bergantung pada model dan data split)
- **AUC ROC:** ~0.83
- **Fitur Penting:** Tenure, MonthlyCharges, Contract Type, TechSupport

---

## 💻 Cara Menjalankan Notebook

1. **Download file:**  
   `real_telco_churn_prediction.ipynb`

2. **Buka di Google Colab:**  
   [colab.research.google.com](https://colab.research.google.com/) dan upload notebook

3. **Jalankan sel secara berurutan** untuk melihat preprocessing, modeling, dan evaluasi

---

## 🔍 Saran Pengembangan Lanjutan

- Tambahkan **SMOTE** untuk mengatasi data imbalance
- Gunakan **GridSearchCV** untuk tuning model
- Implementasi **XGBoost** atau **LightGBM**
- Tambahkan interpretasi lebih lanjut menggunakan **SHAP values**
- Buat aplikasi prediksi real-time dengan **Streamlit**

---

## 📄 Lisensi

Dataset ini bersifat open-source (IBM Sample Data). Kode dalam repositori ini bebas digunakan untuk keperluan edukasi dan non-komersial.

