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

# Buat datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Sidebar filter
st.sidebar.header("Filter Data")

station = st.sidebar.multiselect(
    "Pilih Stasiun",
    options=df['station'].unique(),
    default=df['station'].unique()
)

filtered_df = df[df['station'].isin(station)]

# ======================
# METRICS
# ======================
col1, col2, col3 = st.columns(3)

col1.metric("Rata-rata PM2.5", round(filtered_df['PM2.5'].mean(),2))
col2.metric("Rata-rata PM10", round(filtered_df['PM10'].mean(),2))
col3.metric("Jumlah Stasiun", filtered_df['station'].nunique())

# ======================
# GRAFIK 1
# ======================
st.subheader("📈 Tren PM2.5 dan PM10")

monthly = filtered_df.groupby('month')[['PM2.5','PM10']].mean()

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(monthly.index, monthly['PM2.5'], marker='o', label='PM2.5')
ax.plot(monthly.index, monthly['PM10'], marker='o', label='PM10')

ax.set_xlabel("Bulan")
ax.set_ylabel("Konsentrasi")
ax.legend()

st.pyplot(fig)

# ======================
# GRAFIK 2
# ======================
st.subheader("🏭 Polusi Berdasarkan Stasiun")

station_avg = filtered_df.groupby('station')['PM2.5'].mean().sort_values()

fig2, ax2 = plt.subplots(figsize=(10,5))

sns.barplot(
    x=station_avg.values,
    y=station_avg.index,
    palette="Reds_r",
    ax=ax2
)

st.pyplot(fig2)

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
    ax=ax3
)

st.pyplot(fig3)

# ======================
# FOOTER
# ======================
st.markdown("---")
st.caption("Created by Shelley")
