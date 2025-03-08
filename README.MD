# E-Commerce Customer Analytics Dashboard

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data transaksi pelanggan dalam platform e-commerce dengan menggunakan teknik **Exploratory Data Analysis (EDA)**, **RFM Analysis**, serta memvisualisasikan hasilnya dalam bentuk **dashboard interaktif menggunakan Streamlit**. Analisis ini membantu dalam memahami pola pembelian pelanggan, distribusi geografis pelanggan, serta memberikan insight untuk strategi pemasaran berbasis data.

## 🛠️ Teknologi yang Digunakan
- **Python** (Pandas, NumPy, Seaborn, Matplotlib)
- **Streamlit** untuk pembuatan dashboard interaktif
- **Google Colab** untuk pengolahan data
- **GitHub** untuk penyimpanan dataset

## 📂 Struktur Folder
```
submission
├───dashboard
| ├───venv
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───E-Commerce Public Dataset
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt
```
## 🔍 Exploratory Data Analysis (EDA)
Analisis data dilakukan melalui beberapa tahap berikut:
1. **Assessing & Cleaning Data**
   - Memeriksa kelengkapan dataset
   - Menangani nilai yang hilang atau duplikasi
   - Memastikan tipe data yang sesuai

2. **EDA Numerikal & Kategorikal**
   - Menganalisis distribusi pelanggan berdasarkan Recency, Frequency, dan Monetary (RFM Analysis)
   - Visualisasi distribusi geografis pelanggan berdasarkan kota dan negara bagian
   
3. **RFM Analysis (Recency, Frequency, Monetary)**
   - **Recency**: Mengukur hari sejak transaksi terakhir pelanggan
   - **Frequency**: Menghitung jumlah transaksi yang dilakukan pelanggan
   - **Monetary**: Menganalisis total uang yang dibelanjakan pelanggan

## 📊 Pembuatan Dashboard dengan Streamlit
Dashboard ini dibangun menggunakan **Streamlit** untuk menampilkan hasil analisis secara interaktif. Fitur utama dashboard meliputi:
- **Visualisasi RFM Analysis** (Recency, Frequency, Monetary)
- **Distribusi Metode Pembayaran**
- **Distribusi Geografis Pelanggan**
- **Filter interaktif berdasarkan kota dan negara bagian**

## 🚀 Cara Menjalankan Dashboard
1. **Pastikan semua dependensi telah terinstal**
   ```bash
   pip install -r requirements.txt
   ```
2. **Jalankan Streamlit**
   ```bash
   streamlit run dashboard/main.py
   ```

## 📄 Dataset yang Digunakan
Dataset diambil dari e-commerce dan terdiri dari beberapa file CSV:
- `customers_dataset.csv` → Data pelanggan
- `orders_dataset.csv` → Data pesanan
- `order_items_dataset.csv` → Detail produk dalam pesanan
- `products_dataset.csv` → Data produk
- `sellers_dataset.csv` → Data penjual


## 📌 Kesimpulan & Insight
- Mayoritas pelanggan berasal dari kota besar seperti **São Paulo (SP)** dan **Rio de Janeiro (RJ)**.
- Sebagian besar pelanggan melakukan transaksi sekali atau dua kali dalam rentang data yang tersedia.
- **Recency Analysis** menunjukkan bahwa banyak pelanggan yang sudah lama tidak bertransaksi, menunjukkan potensi program retensi pelanggan.
- **Metode pembayaran** yang paling sering digunakan adalah kartu kredit, diikuti oleh boleto.
- Dashboard ini dapat membantu bisnis untuk mengoptimalkan strategi pemasaran dan meningkatkan kepuasan pelanggan.

## 📢 Kontribusi & Lisensi
Proyek ini bersifat open-source. Jika ingin berkontribusi, silakan buat pull request atau ajukan issue pada repository GitHub.

---

💡 **Dibuat dengan data dan analisis berbasis Python untuk meningkatkan wawasan bisnis e-commerce!**

