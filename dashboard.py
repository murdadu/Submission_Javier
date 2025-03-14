import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Konversi kolom tanggal
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Gabungkan dataset
merged_df = pd.merge(hour_df, day_df, on=['dteday', 'yr', 'mnth', 'weekday'], suffixes=('_hour', '_day'))

# Streamlit Dashboard
st.title("Dashboard Analisis Penyewaan Sepeda")

# Visualisasi: Penyewaan sepeda per hari dalam seminggu
st.subheader("Rata-rata Penyewaan Sepeda per Hari")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=merged_df, x="weekday", y="cnt_hour", palette="coolwarm", ax=ax)
ax.set_xlabel("Hari dalam Seminggu (0 = Minggu, 6 = Sabtu)")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)
st.markdown("\n📌 *Penyewaan sepeda lebih tinggi pada hari kerja dibandingkan akhir pekan, menunjukkan bahwa banyak orang menggunakan sepeda untuk transportasi sehari-hari.*")

# Visualisasi: Penyewaan sepeda per musim
st.subheader("Rata-rata Penyewaan Sepeda per Musim")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=merged_df, x="season_day", y="cnt_hour", palette="Blues", ax=ax)
ax.set_xlabel("Musim (1 = Semi, 2 = Panas, 3 = Gugur, 4 = Dingin)")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)
st.markdown("\n📌 *Musim gugur (fall) memiliki jumlah penyewaan tertinggi, sedangkan musim semi (spring) lebih rendah, hal ini bisa disebabkan oleh cuaca yang lebih nyaman di musim gugur dibandingkan musim semi.*")

# Visualisasi: Penyewaan sepeda berdasarkan cuaca
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=merged_df, x="weathersit_day", y="cnt_hour", palette="Greens", ax=ax)
ax.set_xlabel("Kondisi Cuaca (1 = Cerah, 2 = Berawan, 3 = Hujan)")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)
st.markdown("\n📌 *Cuaca cerah memiliki rata-rata penyewaan tertinggi, sedangkan penyewaan berkurang drastis saat hujan, menunjukkan bahwa faktor cuaca sangat berpengaruh.*")

# Visualisasi: Hubungan suhu dan penyewaan sepeda
st.subheader("Hubungan Suhu dan Penyewaan Sepeda")
df_temp = merged_df.groupby("temp_day")["cnt_hour"].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.lineplot(data=df_temp, x="temp_day", y="cnt_hour", marker="o", color="red", ax=ax)
ax.set_xlabel("Suhu")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)
st.markdown("\n📌 *Penyewaan meningkat seiring kenaikan suhu hingga titik optimal. Namun, jika suhu terlalu tinggi, jumlah penyewaan mulai menurun karena kondisi panas yang kurang nyaman bagi pengguna.*")
