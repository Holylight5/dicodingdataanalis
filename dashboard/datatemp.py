import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Membaca data
dfh = pd.read_csv("data/hour.csv")
dfd = pd.read_csv("data/day.csv")
# Merubah nama kolom
dfd.rename(columns={'yr': 'year',
                    'mnth': 'month',
                    'hum': 'humidity',
                    'cnt': 'count',
                    'dteday': 'Datetime'
                    }, inplace=True)

# Merubah huruf awal kolom menjadi kapital
dfd.columns = dfd.columns.str.title()

# Mengubah kolom datetime menjadi indeks
dfd['Datetime'] = pd.to_datetime(dfd['Datetime'])
dfd.set_index('Datetime', inplace=True)

# Merubah nama kolom
dfh.rename(columns={'yr': 'year',
                    'mnth': 'month',
                    'hum': 'humidity',
                    'cnt': 'count',
                    'dteday': 'Datetime',
                    'hr': 'Hour'
                    }, inplace=True)

# Merubah huruf awal kolom menjadi kapital
dfh.columns = dfh.columns.str.title()

# Memulai Streamlit
st.title("Analisis Penggunaan Sepeda")

# Analisis: Hubungan Suhu dan Kecepatan Angin terhadap Penggunaan Sepeda
st.header("Hubungan Suhu dan Kecepatan Angin terhadap Penggunaan Sepeda")

# Membuat figure dan axis untuk plot
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Scatter plot untuk suhu vs penggunaan sepeda
sns.scatterplot(x='Temp', y='Count', data=dfd, color='blue', ax=axes[0])
axes[0].set_title('Hubungan antara Suhu dan Penggunaan Sepeda')
axes[0].set_xlabel('Suhu (Temp)')
axes[0].set_ylabel('Jumlah Penggunaan Sepeda (Count)')

# Scatter plot untuk kecepatan angin vs penggunaan sepeda
sns.scatterplot(x='Windspeed', y='Count', data=dfd, color='red', ax=axes[1])
axes[1].set_title('Hubungan antara Kecepatan Angin dan Penggunaan Sepeda')
axes[1].set_xlabel('Kecepatan Angin (Windspeed)')
axes[1].set_ylabel('Jumlah Penggunaan Sepeda (Count)')

# Menambahkan layout yang lebih rapat
plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(fig)
