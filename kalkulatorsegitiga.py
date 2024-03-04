import streamlit as st
def kalkulatorsegitiga():
    st.title('Hitung Luas Segitiga')
    panjang = st.number_input("Masukan Nilai Panjang", 0)
    tinggi = st.number_input("Masukkan Nilai tinggi", 0)
    hitung = st.button("Hitung Luas")
    
    if hitung:
        luas = panjang * tinggi /2
        st.success(f"Luas Segitiga adalah={luas}")
        