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
    layout="wide"
)

st.title("🌍 Air Quality Dashboard")
st.markdown("Analisis Dataset Kualitas Udara")

# ======================
# LOAD DATA
# ======================
df = pd.read_csv("dashboard/main_data.csv")

# Buat kolom datetime dari year, month, day, hour
df['datetime'] = pd.to_datetime(
    df[['year', 'month', 'day', 'hour']]
)

# Pastikan month integer
df['month'] = df['month'].astype(int)

# ======================
# SIDEBAR
# ======================
st.sidebar.header("Filter Data")

station = st.sidebar.multiselect(
    "Pilih Stasiun",
    options=sorted(df['station'].unique()),
    default=sorted(df['station'].unique())
)

filtered_df = df[df['station'].isin(station)]

# ======================
# METRICS
# ======================
col1, col2, col3 = st.columns(3)

col1.metric("Rata-rata PM2.5", round(filtered_df['PM2.5'].mean(), 2))
col2.metric("Rata-rata PM10", round(filtered_df['PM10'].mean(), 2))
col3.metric("Jumlah Stasiun", filtered_df['station'].nunique())

# ======================
# GRAFIK 1
# ======================
st.subheader("📈 Tren PM2.5 dan PM10 per Bulan")

monthly = filtered_df.groupby('month')[['PM2.5', 'PM10']].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(monthly['month'], monthly['PM2.5'], marker='o', linewidth=2, label='PM2.5')
ax.plot(monthly['month'], monthly['PM10'], marker='o', linewidth=2, label='PM10')

ax.set_xlabel("Bulan")
ax.set_ylabel("Konsentrasi")
ax.set_xticks(range(1, 13))
ax.legend()

st.pyplot(fig)

# ======================
# GRAFIK 2
# ======================
st.subheader("🏭 Rata-rata PM2.5 Berdasarkan Stasiun")

station_avg = filtered_df.groupby('station')['PM2.5'].mean().sort_values(ascending=False)

fig2, ax2 = plt.subplots(figsize=(10, 5))

sns.barplot(
    x=station_avg.values,
    y=station_avg.index,
    palette="Reds_r",
    ax=ax2
)

ax2.set_xlabel("PM2.5")
ax2.set_ylabel("Stasiun")

st.pyplot(fig2)

# ======================
# GRAFIK 3
# ======================
st.subheader("🌦️ Korelasi Faktor Cuaca")

corr = filtered_df[['PM2.5', 'TEMP', 'RAIN', 'WSPM']].corr()

fig3, ax3 = plt.subplots(figsize=(8, 5))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    ax=ax3
)

st.pyplot(fig3)

# ======================
# FOOTER
# ======================
st.markdown("---")
st.caption("Created by Shelley")
