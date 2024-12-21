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

# No 1 Apakah bulan dengan banyak hari libur memiliki lebih banyak penggunaan sepeda
st.write(
    """
    ### No 1
    Apakah bulan dengan banyak hari libur memiliki lebih banyak penggunaan sepeda

   Dilihat dari hasil visualisasi data diatas, banyaknya hari libur tidak menentukan banyaknya pengguna sepeda pada bulan tersebut.
    """
)
# Menggunakan plot dari file datapengguna
st.pyplot(dataHolidayWorkingday.fig)

#Apakah pengguna sepeda lebih terpengaruh oleh suhu atau kecepatan angin?
st.write(
    """
    ### No 2
    Apakah pengguna sepeda lebih terpengaruh oleh suhu atau kecepatan angin?

    Bedasarkan diagram diatas dapat disimpulkan bahwa suhu dan kecepatan angin berpengaruh pada banyaknya pengguna sepeda. Pada bagian suhu semakin nilai suhunya kecil maka pengguna sepeda sedikit. Sementara pada kecepatan angin pengguna sepeda tidak terlalu berpengaruh besar dengan banyaknya pengguna sepeda.
    """
)
# Menggunakan plot dari file datatemp
st.pyplot(datatemp.fig)

# No 3 Diantara keduanya mana yang paling banyak menggunakan sepeda, pengguna terdaftar atau tidak terdaftar?
st.write(
    """
    ### No 3
    Yang paling banyak menggunakan sepeda, pengguna terdaftar atau tidak terdaftar?

    Dari data diatas dapat disimpulkan bahwa pengguna paling banyak didapatkan oleh pengguna yang terdaftar dengan total pengguna lebih dari 2,5jt.
    """
)
# Menggunakan plot dari file datamusim
st.pyplot(datapengguna.fig)

# No 4 Di musim apa sepeda paling banyak di rental?
st.write(
    """
    ### No 4
    Di musim apa sepeda paling banyak di rental?

    Dari data diatas menunjukan bahwa pengguna sepeda paling banyak pada musim gugur, bisa jadi karena cuaca di musim gugur yang sejuk dengan pemandangan gugurnya daun pohon yang membuat kesan romantis.
    """
)
# Menggunakan plot dari file dataHolidayWorkingday
st.pyplot(datamusim.fig)
