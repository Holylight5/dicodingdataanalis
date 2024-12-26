import streamlit as st
import datatemp  
import datamusim 
import datapengguna  
import dataHolidayWorkingday 

st.write(
    """
    Bike Sharing Dashboard
    Bike Sharing Data Analysis Project
    """
)

with st.sidebar:
    st.write(
        """
        Bike Sharing Dashboard
        Bike Sharing Data Analysis Project
        =========================================
        Dirga Marin Ramadhan
        """
    )

# Menambahkan filter untuk memilih No yang ingin ditampilkan
analysis_number = st.sidebar.selectbox(
    "Pilih Analisis",
    [1, 2, 3, 4],  # Pilihan analisis
    index=0  # Default pilihan
)

if analysis_number == 1:
    st.write(
        """
        ### No 1
        Apakah bulan dengan banyak hari libur memiliki lebih banyak penggunaan sepeda?

        Dilihat dari hasil visualisasi data di bawah, banyaknya hari libur tidak menentukan banyaknya pengguna sepeda pada bulan tersebut.
        """
    )
    # Menggunakan plot dari file dataHolidayWorkingday
    st.pyplot(dataHolidayWorkingday.fig)

elif analysis_number == 2:
    st.write(
        """
        ### No 2
        Apakah pengguna sepeda lebih terpengaruh oleh suhu atau kecepatan angin?

        Berdasarkan diagram di bawah dapat disimpulkan bahwa suhu dan kecepatan angin berpengaruh pada banyaknya pengguna sepeda. Pada bagian suhu, semakin nilai suhunya kecil maka pengguna sepeda sedikit. Sementara pada kecepatan angin, pengguna sepeda tidak terlalu berpengaruh besar dengan banyaknya pengguna sepeda.
        """
    )
    # Menggunakan plot dari file datatemp
    st.pyplot(datatemp.fig)

elif analysis_number == 3:
    st.write(
        """
        ### No 3
        Diantara keduanya mana yang paling banyak menggunakan sepeda, pengguna terdaftar atau tidak terdaftar?

        Dari data di bawah dapat disimpulkan bahwa pengguna paling banyak didapatkan oleh pengguna yang terdaftar dengan total pengguna lebih dari 2,5jt.
        """
    )
    # Menggunakan plot dari file datapengguna
    st.pyplot(datapengguna.fig)

elif analysis_number == 4:
    st.write(
        """
        ### No 4
        Di musim apa sepeda paling banyak di rental?

        ============================================
        Musim 
        1: Spring  2: Summer  3: Fall  4 :Winter
        ============================================
        
        Dari data di bawah menunjukkan bahwa pengguna sepeda paling banyak pada musim gugur, bisa jadi karena cuaca di musim gugur yang sejuk dengan pemandangan gugurnya daun pohon yang membuat kesan romantis.
        """
    )
    # Menggunakan plot dari file datamusim
    st.pyplot(datamusim.fig)
