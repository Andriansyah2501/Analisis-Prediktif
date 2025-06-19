# Laporan Proyek Machine Learning - Andrian Syah

📝 Laporan Proyek Machine Learning - Andrian Syah
📌 Domain Proyek: Telekomunikasi
Churn pelanggan merupakan tantangan utama dalam industri telekomunikasi. Churn berarti pelanggan berhenti menggunakan layanan dari suatu penyedia, yang menyebabkan perusahaan mengalami kerugian dari sisi pendapatan dan biaya akuisisi pelanggan baru. Oleh karena itu, penting bagi perusahaan untuk dapat memprediksi potensi churn dan melakukan tindakan preventif lebih dini.

Dengan menggunakan machine learning, kita bisa menganalisis pola dari pelanggan yang pernah berhenti berlangganan dan memprediksi kemungkinan pelanggan lain akan melakukan hal yang sama. Hal ini memungkinkan strategi retensi yang lebih efektif dan efisien.

🎯 Business Understanding
Problem Statement:
Bagaimana cara mengidentifikasi pelanggan yang kemungkinan besar akan melakukan churn?

Fitur apa yang paling berpengaruh terhadap keputusan pelanggan untuk berhenti?

Goals:
Mengembangkan model machine learning untuk memprediksi churn pelanggan.

Mengidentifikasi fitur penting yang memengaruhi keputusan pelanggan dalam berhenti berlangganan.

Solution Statement:
Menggunakan tiga algoritma machine learning: Logistic Regression, Random Forest, dan XGBoost.

Menangani ketidakseimbangan data dengan teknik SMOTE.

Evaluasi model menggunakan metrik: accuracy, precision, recall, F1-score, dan ROC-AUC.

📊 Data Understanding
Dataset yang digunakan adalah Telco Customer Churn yang tersedia di Kaggle: https://www.kaggle.com/blastchar/telco-customer-churn

Dataset ini terdiri dari 7.043 entri pelanggan dengan informasi seperti:

gender, SeniorCitizen, Partner, Dependents

tenure, MonthlyCharges, TotalCharges

Contract, InternetService, PaymentMethod

Target: Churn (Yes/No)

EDA menunjukkan bahwa pelanggan dengan kontrak jangka pendek, tagihan bulanan tinggi, dan tidak memiliki mitra cenderung lebih banyak melakukan churn.

🧹 Data Preparation
Menghapus kolom customerID yang tidak relevan.

Menangani nilai kosong (TotalCharges kosong di beberapa baris).

Encoding fitur kategorikal dengan LabelEncoder dan OneHotEncoder.

Standardisasi fitur numerik menggunakan StandardScaler.

Menggunakan SMOTE untuk menyeimbangkan distribusi label Churn (karena dataset tidak seimbang).

Membagi dataset menjadi data latih dan data uji (80:20 split).

⚙️ Modeling
Tiga model diterapkan:

Logistic Regression - Model baseline

Random Forest - Ensemble model dengan pembobotan acak

XGBoost - Model boosting yang kuat dan efisien

Parameter default digunakan terlebih dahulu, lalu tuning dilakukan pada XGBoost untuk mencari kombinasi terbaik.

✅ Evaluation
Model dievaluasi dengan metrik:

Accuracy: Seberapa banyak prediksi benar

Recall: Seberapa banyak churn terdeteksi (penting untuk retensi)

Precision dan F1-score: Untuk melihat keseimbangan antara TP dan FP

ROC AUC: Kemampuan model dalam membedakan kelas

Hasil evaluasi:

Model	Accuracy	Recall	F1-score	ROC AUC
Logistic Regression	80%	68%	72%	84%
Random Forest	84%	74%	77%	88%
XGBoost	86%	77%	79%	91%

📌 Kesimpulan
Model XGBoost memberikan performa terbaik dan dipilih sebagai model akhir. Model ini mampu memprediksi pelanggan yang akan churn dengan tingkat akurasi dan recall yang tinggi, yang sangat penting untuk membantu perusahaan melakukan tindakan retensi.
---

## 📄 Lisensi

Dataset ini bersifat open-source (IBM Sample Data). Kode dalam repositori ini bebas digunakan untuk keperluan edukasi dan non-komersial.

