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

# Sidebar filter untuk memilih rentang tanggal
st.sidebar.header("Filter Tanggal")
start_date = st.sidebar.date_input("Mulai Tanggal", merged_df['dteday'].min())
end_date = st.sidebar.date_input("Sampai Tanggal", merged_df['dteday'].max())

# Filter data berdasarkan rentang tanggal
filtered_df = merged_df[(merged_df['dteday'] >= pd.to_datetime(start_date)) & (merged_df['dteday'] <= pd.to_datetime(end_date))]

# Visualisasi: Penyewaan sepeda per hari dalam seminggu
st.subheader("Rata-rata Penyewaan Sepeda per Hari")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=filtered_df, x="weekday", y="cnt_hour", ax=ax)
ax.set_xticklabels(["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"])
ax.set_xlabel("Hari")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)
st.markdown("\n📌 *Penyewaan sepeda lebih tinggi pada hari kerja dibandingkan akhir pekan, menunjukkan bahwa banyak orang menggunakan sepeda untuk transportasi sehari-hari.*")

# Visualisasi: Penyewaan sepeda per musim
st.subheader("Rata-rata Penyewaan Sepeda per Musim")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=filtered_df, x="season_day", y="cnt_hour", ax=ax)
ax.set_xticklabels(["Semi","Panas","Gugur","Dingin"])
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)
st.markdown("\n📌 *Musim gugur (fall) memiliki jumlah penyewaan tertinggi, sedangkan musim semi (spring) lebih rendah, hal ini bisa disebabkan oleh cuaca yang lebih nyaman di musim gugur dibandingkan musim semi.*")

# Visualisasi: Penyewaan sepeda berdasarkan cuaca
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=filtered_df, x="weathersit_day", y="cnt_hour", ax=ax)
ax.set_xticklabels(["Cerah","Berawan","Hujan",])
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)
st.markdown("\n📌 *Cuaca cerah memiliki rata-rata penyewaan tertinggi, sedangkan penyewaan berkurang drastis saat hujan, menunjukkan bahwa faktor cuaca sangat berpengaruh.*")