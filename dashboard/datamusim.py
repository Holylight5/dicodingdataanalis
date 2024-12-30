import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Membaca data
dfd = pd.read_csv("data/day.csv")

# Merubah nama kolom
dfd.rename(columns={'yr': 'year',
                    'mnth': 'month',
                    'hum': 'humidity',
                    'cnt': 'count',
                    'dteday': 'Datetime',
                    'season': 'Season'
                    }, inplace=True)

# Merubah huruf awal kolom menjadi kapital
dfd.columns = dfd.columns.str.title()

# Mengubah kolom datetime menjadi indeks
dfd['Datetime'] = pd.to_datetime(dfd['Datetime'])
dfd.set_index('Datetime', inplace=True)

# Streamlit: Judul Aplikasi
st.title("Analisis Penggunaan Sepeda Berdasarkan Musim")

# Mengelompokkan data berdasarkan musim dan menghitung total pengguna
seasonal_rentals = dfd.groupby('Season').agg({'Count': 'sum'}).sort_values('Count', ascending=False)

# Menampilkan data
st.subheader("Jumlah Pengguna Sepeda per Musim")
st.write(seasonal_rentals)

# Membuat bar plot utama
st.subheader("Visualisasi Penggunaan Sepeda per Musim")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=seasonal_rentals.index, y=seasonal_rentals['Count'], palette='viridis', ax=ax)

# Menambahkan judul dan label
ax.set_title('Jumlah Sepeda yang Disewa per Musim', fontsize=14)
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Pengguna Sepeda')

# Mengatur format sumbu y agar menampilkan angka ribuan
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: f"{int(x):,}"))

plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(fig)

# Membuat plot untuk musim Spring
spring_data = dfd[dfd['Season'] == 1]
fig, ax = plt.subplots(figsize=(8, 6))
sns.lineplot(data=spring_data, x=spring_data.index, y='Count', ax=ax)
ax.set_title('Penggunaan Sepeda di Musim Semi (Spring)', fontsize=14)
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Pengguna Sepeda')
plt.tight_layout()
spring_fig = plt.gcf()
st.pyplot(spring_fig)  # Display Spring figure
plt.close()

# Membuat plot untuk musim Summer
summer_data = dfd[dfd['Season'] == 2]
fig, ax = plt.subplots(figsize=(8, 6))
sns.lineplot(data=summer_data, x=summer_data.index, y='Count', ax=ax)
ax.set_title('Penggunaan Sepeda di Musim Panas (Summer)', fontsize=14)
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Pengguna Sepeda')
plt.tight_layout()
summer_fig = plt.gcf()
st.pyplot(summer_fig)  # Display Summer figure
plt.close()

# Membuat plot untuk musim Fall
fall_data = dfd[dfd['Season'] == 3]
fig, ax = plt.subplots(figsize=(8, 6))
sns.lineplot(data=fall_data, x=fall_data.index, y='Count', ax=ax)
ax.set_title('Penggunaan Sepeda di Musim Gugur (Fall)', fontsize=14)
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Pengguna Sepeda')
plt.tight_layout()
fall_fig = plt.gcf()
st.pyplot(fall_fig)  # Display Fall figure
plt.close()

# Membuat plot untuk musim Winter
winter_data = dfd[dfd['Season'] == 4]
fig, ax = plt.subplots(figsize=(8, 6))
sns.lineplot(data=winter_data, x=winter_data.index, y='Count', ax=ax)
ax.set_title('Penggunaan Sepeda di Musim Dingin (Winter)', fontsize=14)
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Pengguna Sepeda')
plt.tight_layout()
winter_fig = plt.gcf()
st.pyplot(winter_fig)  # Display Winter figure
plt.close()
