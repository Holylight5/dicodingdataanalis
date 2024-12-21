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
                    'registered': 'Registered',
                    'casual': 'Casual'
                    }, inplace=True)

# Merubah huruf awal kolom menjadi kapital
dfd.columns = dfd.columns.str.title()

# Mengubah kolom datetime menjadi indeks
dfd['Datetime'] = pd.to_datetime(dfd['Datetime'])
dfd.set_index('Datetime', inplace=True)

# Streamlit: Judul Aplikasi
st.title("Analisis Total Pengguna Sepeda")

# Menjumlahkan total pengguna terdaftar dan tidak terdaftar di seluruh dataset
total_data = dfd[['Registered', 'Casual']].sum().reset_index()
total_data.columns = ['User Type', 'Total']

# Menampilkan data
st.subheader("Data Total Pengguna Sepeda")
st.write(total_data)

# Membuat bar plot
st.subheader("Visualisasi Total Pengguna Sepeda")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='User Type', y='Total', data=total_data, palette='viridis', ax=ax)

# Menambahkan judul dan label
ax.set_title('Total Penggunaan Sepeda: Terdaftar vs Tidak Terdaftar', fontsize=14)
ax.set_xlabel('Tipe Pengguna')
ax.set_ylabel('Jumlah Pengguna Sepeda (Data Asli)')
plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(fig)
