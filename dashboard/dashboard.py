# dashboard/dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================
# CONFIG
# ======================
st.set_page_config(
    page_title="Air Quality Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ======================
# LOAD DATA
# ======================
df = pd.read_csv("dashboard/main_data.csv")

df['datetime'] = pd.to_datetime(df[['year','month','day','hour']])

# ======================
# HEADER
# ======================
st.title("🌍 Air Quality Dashboard")
st.markdown("Analisis kualitas udara berdasarkan PM2.5, PM10, lokasi stasiun, dan faktor cuaca.")

st.info("Dashboard ini menampilkan pola polusi udara dan faktor yang memengaruhinya.")

# ======================
# SIDEBAR
# ======================
st.sidebar.header("📌 Filter")

station = st.sidebar.multiselect(
    "Pilih Stasiun",
    options=sorted(df['station'].unique()),
    default=sorted(df['station'].unique())
)

filtered_df = df[df['station'].isin(station)]

# ======================
# METRICS
# ======================
st.subheader("📊 Ringkasan Data")

col1, col2, col3 = st.columns(3)

col1.metric("Rata-rata PM2.5", round(filtered_df['PM2.5'].mean(),2))
col2.metric("Rata-rata PM10", round(filtered_df['PM10'].mean(),2))
col3.metric("Jumlah Stasiun", filtered_df['station'].nunique())

# ======================
# GRAFIK 1
# ======================
st.subheader("📈 Tren PM2.5 dan PM10 per Bulan")

monthly = filtered_df.groupby('month')[['PM2.5','PM10']].mean().reset_index()

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(monthly['month'], monthly['PM2.5'], marker='o', linewidth=2, label='PM2.5')
ax.plot(monthly['month'], monthly['PM10'], marker='o', linewidth=2, label='PM10')

ax.set_xlabel("Bulan")
ax.set_ylabel("Konsentrasi")
ax.legend()
ax.grid(True, alpha=0.3)

st.pyplot(fig)

# Insight otomatis
st.success("PM2.5 dan PM10 cenderung meningkat pada awal dan akhir tahun.")

# ======================
# GRAFIK 2
# ======================
st.subheader("🏭 Rata-rata PM2.5 Berdasarkan Stasiun")

station_avg = filtered_df.groupby('station')['PM2.5'].mean().sort_values(ascending=False)

fig2, ax2 = plt.subplots(figsize=(10,5))
sns.barplot(
    x=station_avg.values,
    y=station_avg.index,
    palette="Reds_r"
)

st.pyplot(fig2)

st.warning(f"Stasiun dengan polusi tertinggi: {station_avg.index[0]}")

# ======================
# GRAFIK 3
# ======================
st.subheader("🌦️ Korelasi Faktor Cuaca")

corr = filtered_df[['PM2.5','TEMP','RAIN','WSPM']].corr()

fig3, ax3 = plt.subplots(figsize=(8,5))
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

st.pyplot(fig3)

st.info("Kecepatan angin memiliki korelasi negatif terhadap PM2.5.")

# ======================
# FOOTER
# ======================
st.markdown("---")
st.caption("Created by Sherli | Dicoding Submission")
