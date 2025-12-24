<p align="center">
  <img src="https://img.icons8.com/color/96/fish.png" width="90"/>
</p>

<h1 align="center">🐟 Dashboard Klasifikasi Jenis Ikan</h1>

<p align="center">
  <b>Deep Learning-Based Fish Classification using CNN, EfficientNetB0, and MobileNetV2</b><br>
  Streamlit Web Dashboard for Real-Time Image Prediction
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Deep%20Learning-TensorFlow-orange"/>
  <img src="https://img.shields.io/badge/Web%20App-Streamlit-red"/>
  <img src="https://img.shields.io/badge/Image%20Classification-CNN-blue"/>
</p>

---

## 📌 Deskripsi proyek

Proyek ini mengembangkan sistem klasifikasi citra ikan berbasis deep learning yang diimplementasikan dalam bentuk dashboard web interaktif menggunakan Streamlit. Sistem menerima input gambar ikan dan menghasilkan prediksi spesies ikan secara real-time.

Pada proyek ini dilakukan perbandingan performa tiga arsitektur model, yaitu CNN custom, EfficientNetB0, dan MobileNetV2, untuk mengetahui model yang paling optimal dari sisi akurasi dan efisiensi. Selain prediksi kelas, sistem juga menampilkan confidence score dan probabilitas tiap kelas, sehingga hasil prediksi dapat dipahami dengan lebih baik.

Proyek ini bertujuan sebagai studi komparatif model CNN serta contoh penerapan klasifikasi citra dalam aplikasi berbasis web..

🎯 **Tujuan utama proyek:**
- Mengklasifikasikan citra ikan ke dalam beberapa spesies
- Membandingkan performa tiga arsitektur CNN
- Menyediakan sistem prediksi real-time berbasis web

---

## 🧠 Ringkasan Kinerja Model

| Model | Validation Accuracy | Analysis |
|------|--------------------|---------|
| **CNN (Custom)** | **80%** | Model baseline dengan performa cukup baik, namun kesulitan membedakan kelas ikan yang memiliki kemiripan visual tinggi. |
| **EfficientNetB0** | **99%** | Performa terbaik dengan generalisasi sangat kuat berkat transfer learning dari ImageNet. |
| **MobileNetV2** | **99%** | Akurasi tinggi dengan keunggulan efisiensi dan kecepatan inferensi. |

---

## 📂 Deskripsi Dataset

sumber:
```
https://drive.google.com/drive/folders/1ivFJopBNevEjzg3-QdEMEzjHu3WxVNpG?usp=sharing
```

Dataset yang digunakan adalah Fish Image Dataset yang berisi citra ikan dari 8 kelas berbeda, yaitu Catfish, Glass Perchlet, Goby, Gourami, Grass Carp, Knifefish, Silver Barb, dan Tilapia.
Dataset disusun dalam struktur direktori yang terpisah antara data latih (train), data validasi (val), dan data uji (test) untuk mendukung proses pelatihan dan evaluasi model.

Setiap kelas direpresentasikan oleh ratusan citra dengan variasi sudut pandang, ukuran, dan kondisi pencahayaan.
Dataset yang digunakan adalah **Fish Image Dataset** yang dibagi menjadi:
```
FishImgDataset/
├── train/
│   ├── class_1/
│   ├── class_2/
│   └── ...
├── val/
│   ├── class_1/
│   ├── class_2/
│   └── ...
└── test/
    ├── class_1/
    ├── class_2/
    └── ...
```

---


### 🐠 Kelas
- Catfish
- Glass Perchlet
- Goby
- Gourami
- Grass Carp
- Knifefish
- Silver Barb
- Tilapia

---

## ⚙️ Data Preprocessing

Tahapan preprocessing disesuaikan dengan karakteristik masing-masing model deep learning yang digunakan, sebagai berikut:

## 🔹 1. CNN (Custom)
Preprocessing pada model CNN custom dilakukan secara sederhana untuk memastikan kestabilan proses pelatihan, meliputi:
- Resize gambar ke ukuran 224×224 piksel
- Normalisasi piksel dengan skala 1./255
- Data augmentation pada data latih:
    - Rotasi gambar
    - Zoom
    - Horizontal flip
      
Pendekatan ini bertujuan untuk meningkatkan variasi data dan membantu model mempelajari pola visual dasar dari citra ikan.

## 🔹 2. EfficientNetB0
EfficientNetB0 menggunakan preprocessing khusus yang sesuai dengan model pretrained ImageNet, yaitu:
- Resize gambar ke ukuran 224×224 piksel
- Preprocessing menggunakan preprocess_input EfficientNet
- Data augmentation ringan, seperti rotasi kecil dan zoom

  Preprocessing ini memastikan distribusi data input sesuai dengan data yang digunakan saat pretraining, sehingga transfer learning dapat bekerja secara optimal.

## 🔹 3. MobileNetV2
Preprocessing untuk MobileNetV2 dirancang agar tetap ringan dan efisien, meliputi:
- Resize gambar ke ukuran 224×224 piksel
- Normalisasi piksel dengan skala 1./255
- Data augmentation pada data latih:
      - Rotasi
      - Zoom
      - Horizontal flip
  
Pendekatan ini mendukung performa tinggi MobileNetV2 dengan tetap menjaga efisiensi komputasi.

---

## 🏗️ Arsitektur Model

### 🔹 CNN (Custom)
- Convolution + MaxPooling
- Fully Connected Layer
- Dropout
- Digunakan sebagai **baseline model**

---

### 🔹 EfficientNetB0
- Transfer Learning (ImageNet)
- Global Average Pooling
- Dense + Dropout
- **Akurasi tertinggi**

---

### 🔹 MobileNetV2
- Lightweight CNN
- Efisien dan cepat
- Cocok untuk deployment web & edge device

---

## 📊 Evaluasi dan Analisis Komparatif

### 📈 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

### 🔍 Key Findings
- CNN cocok sebagai model awal
- EfficientNetB0 unggul dalam semua metrik
- MobileNetV2 adalah solusi terbaik untuk aplikasi real-time

> ✅ **Rekomendasi AKhir:**  
> Gunakan **EfficientNetB0** untuk akurasi maksimal dan **MobileNetV2** untuk efisiensi sistem.

---

## 🚀 Jalankan Dashboard Secara Lokal

### 🔧 Requirements
- Python ≥ 3.9

Install dependencies:
```bash
pip install streamlit tensorflow pillow numpy
```

📁 Project Structure
```
project/
│── app.py
│── models/
│   ├── cnn_fish.h5
│   ├── efficientnetb0_fish.h5
│   └── mobilenetv2_fish.h5
```


▶️ Jalankan Dashboard
```
-streamlit run app.py
```


🌐 Buka di browser:
```
-http://localhost:8501
```


