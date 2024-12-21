import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Membaca data
dfd = pd.read_csv("D:/Bangkit Akademi/Dicoding/data/day.csv")

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

# Membuat bar plot
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
