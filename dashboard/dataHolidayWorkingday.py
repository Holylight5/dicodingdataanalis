import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st

# Membaca data
dfh = pd.read_csv("data/hour.csv")
dfd = pd.read_csv("data/day.csv")

# Merubah nama kolom
dfd.rename(columns={'yr':'year',
                    'mnth':'month',
                    'hum':'humidity',
                    'cnt':'count',
                    'dteday':'Datetime'
                    }, inplace=True)

# Merubah huruf awal kolom menjadi kapital
dfd.columns = dfd.columns.str.title()

# Mengubah kolom datetime menjadi indeks
dfd['Datetime'] = pd.to_datetime(dfd['Datetime'])
dfd.set_index('Datetime', inplace=True)

# Merubah nama kolom
dfh.rename(columns={'yr':'year',
                    'mnth':'month',
                    'hum':'humidity',
                    'cnt':'count',
                    'dteday':'Datetime',
                    'hr':'Hour'
                    }, inplace=True)

# Merubah huruf awal kolom menjadi kapital
dfh.columns = dfh.columns.str.title()

# Memulai Streamlit
st.title("Analisis Penggunaan Sepeda")

# Analisis: Apakah bulan dengan banyak hari libur memiliki lebih banyak penggunaan sepeda?
st.header("Hubungan Antara Jumlah Hari Libur dan Penggunaan Sepeda per Bulan")

# Mengelompokkan data
grouped_data = dfd.groupby(by=["Year", "Month"]).agg({
    "Holiday": "sum",
    "Workingday": "sum",
    "Count": "sum"
}).reset_index()

# Visualisasi menggunakan Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Holiday', y='Count', data=grouped_data, hue='Month', palette='tab20', s=100, ax=ax)

# Menambahkan judul dan label
ax.set_title('Hubungan Antara Jumlah Hari Libur dan Penggunaan Sepeda per Bulan')
ax.set_xlabel('Jumlah Hari Libur')
ax.set_ylabel('Jumlah Penggunaan Sepeda')

# Menampilkan legenda untuk bulan
plt.legend(title='Month', bbox_to_anchor=(1.05, 1), loc='upper left')

# Menampilkan plot di Streamlit
st.pyplot(fig)
