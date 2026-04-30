# 🌫️ Air Pollution Insight Dashboard

Dashboard ini dibuat untuk menganalisis kondisi kualitas udara menggunakan **Air Quality Dataset**.  
Fokus analisis meliputi pola konsentrasi polutan dari waktu ke waktu, lokasi dengan tingkat pencemaran tertinggi, serta hubungan antara kondisi cuaca dan polusi udara selama periode **Maret 2013 hingga Februari 2017**.

---

## 🎯 Pertanyaan Bisnis

1. Bagaimana tren konsentrasi PM2.5 dan PM10 per bulan selama periode Maret 2013 hingga Februari 2017, serta kapan periode polusi tertinggi terjadi?

2. Stasiun pemantauan mana yang memiliki rata-rata tingkat polusi tertinggi selama periode Maret 2013 hingga Februari 2017?

3. Bagaimana pengaruh faktor cuaca seperti suhu, curah hujan, dan kecepatan angin terhadap tingkat polusi udara selama periode Maret 2013 hingga Februari 2017?

---

## 📊 Apa yang Bisa Dilihat di Dashboard?

✨ **Statistik Ringkas**  
Menampilkan rata-rata PM2.5, PM10, dan jumlah stasiun pemantauan.

📈 **Perubahan Polusi dari Waktu ke Waktu**  
Grafik tren bulanan untuk melihat kapan kualitas udara memburuk atau membaik.

🏭 **Perbandingan Antar Stasiun**  
Menunjukkan wilayah/stasiun dengan tingkat polusi tertinggi dan terendah.

🌦️ **Hubungan Cuaca & Polusi**  
Visualisasi korelasi antara suhu, hujan, kecepatan angin, dan konsentrasi PM2.5.

🎯 **Filter Interaktif**  
Pengguna dapat memilih stasiun tertentu untuk melihat data yang lebih spesifik.

---

## 📁 Susunan File Proyek

```bash
submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   └── Air-quality-dataset.zip
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt

---

## ⚙️ Cara Install & Menjalankan Dashboard

```bash
pip install -r requirements.txt
streamlit run dashboard/dashboard.py
