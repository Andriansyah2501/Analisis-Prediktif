# Laporan Proyek Machine Learning Terapan - Andrian Syah

## 1. Domain Proyek

Industri telekomunikasi menghadapi tantangan besar dalam mempertahankan pelanggan di tengah persaingan yang ketat. Salah satu isu utama adalah **churn**, yaitu ketika pelanggan berhenti menggunakan layanan dari perusahaan. Hal ini berdampak langsung pada penurunan pendapatan dan meningkatkan biaya untuk mendapatkan pelanggan baru.

Dengan memanfaatkan machine learning, perusahaan dapat memprediksi pelanggan yang kemungkinan besar akan melakukan churn. Prediksi ini membantu perusahaan dalam menyusun strategi retensi dan peningkatan kepuasan pelanggan secara proaktif.

## 2. Business Understanding

### 2.1 Problem Statements
1. Bagaimana cara mengidentifikasi pelanggan yang kemungkinan besar akan melakukan churn?
2. Fitur apa yang paling berpengaruh terhadap keputusan pelanggan untuk berhenti berlangganan?

### 2.2 Goals
1. Membangun model machine learning yang mampu memprediksi pelanggan yang akan melakukan churn.
2. Mengidentifikasi fitur penting yang berpengaruh terhadap churn agar perusahaan dapat merancang strategi retensi yang efektif.

### 2.3 Solution Statements
- Menerapkan algoritma klasifikasi: **Logistic Regression**, **Random Forest**, dan **XGBoost**.
- Menangani ketidakseimbangan kelas dengan **SMOTE (Synthetic Minority Over-sampling Technique)**.
- Melakukan evaluasi dengan metrik yang relevan seperti: **accuracy**, **precision**, **recall**, **F1-score**, dan **ROC-AUC**.

## 3. Data Understanding

Dataset yang digunakan adalah [Telco Customer Churn Dataset dari Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn) yang terdiri dari 7.043 data pelanggan dengan 21 fitur, termasuk:

- `gender`, `SeniorCitizen`, `Partner`, `Dependents`
- `tenure`, `MonthlyCharges`, `TotalCharges`
- `Contract`, `InternetService`, `PaymentMethod`
- `Churn`: Label target (Yes/No)

Hasil analisis awal menunjukkan bahwa pelanggan yang menggunakan kontrak jangka pendek, memiliki tagihan bulanan tinggi, dan tidak memiliki pasangan, lebih cenderung melakukan churn.

## 4. Data Preparation

Langkah-langkah yang dilakukan:
- Menghapus kolom `customerID` karena tidak memberikan informasi relevan.
- Menghapus nilai kosong dan mengonversi `TotalCharges` menjadi numerik.
- Mengubah data kategorikal menggunakan **LabelEncoder** dan **OneHotEncoder**.
- Melakukan normalisasi terhadap data numerik menggunakan **StandardScaler**.
- Membagi data menjadi data latih dan data uji (80:20).
- Menyeimbangkan jumlah kelas menggunakan **SMOTE** karena jumlah pelanggan churn lebih sedikit.

## 5. Modeling

Tiga model digunakan untuk melakukan prediksi churn:

1. **Logistic Regression**
   - Model baseline yang digunakan untuk klasifikasi biner.

2. **Random Forest Classifier**
   - Model ensemble berbasis pohon keputusan dengan teknik bootstrapping.

3. **XGBoost Classifier**
   - Model boosting yang unggul dalam menangani ketidakseimbangan data dan memberikan performa tinggi.

Semua model dilatih menggunakan data hasil preprocessing dan disesuaikan untuk memaksimalkan recall.

## 6. Evaluation

Evaluasi dilakukan menggunakan metrik:
- **Accuracy**: Proporsi prediksi yang benar.
- **Precision**: Proporsi pelanggan yang diprediksi churn dan benar-benar churn.
- **Recall**: Proporsi churn yang berhasil dideteksi (sangat penting).
- **F1-Score**: Harmonik dari precision dan recall.
- **ROC-AUC**: Mengukur kemampuan model membedakan kelas churn dan tidak churn.

Hasil evaluasi model:

| Model               | Accuracy | Recall | F1-score | ROC AUC |
|--------------------|----------|--------|----------|---------|
| Logistic Regression| 80%      | 68%    | 72%      | 84%     |
| Random Forest      | 84%      | 74%    | 77%      | 88%     |
| XGBoost            | **86%**  | **77%**| **79%**  | **91%** |

Model **XGBoost** menghasilkan performa terbaik dan dipilih sebagai model final.

## 7. Kesimpulan

- Model machine learning dapat secara efektif digunakan untuk memprediksi pelanggan yang kemungkinan besar akan melakukan churn.
- Model **XGBoost** menunjukkan performa terbaik dan dipilih karena memiliki skor recall dan ROC-AUC tertinggi.
- Fitur-fitur seperti `tenure`, `MonthlyCharges`, dan `Contract` terbukti sangat memengaruhi keputusan churn pelanggan.
- Dengan informasi ini, perusahaan dapat menargetkan pelanggan berisiko tinggi dengan promosi atau penawaran khusus untuk meningkatkan loyalitas dan retensi.

