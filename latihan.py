import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
from kalkulatorsegitiga import kalkulatorsegitiga
from image1 import main
# import pandas as pd

# st.write(" Infinity Coding Club 2024")
# #import matplotlib.pyplot as plt

# df = pd.DataFrame ({
#     'No': [1, 2, 3, 4],
#     'Nama' : ['Nurul','Nadia','Vino','Zahwa'],
#     'Nilai' : [98, 90, 100, 92]
# })

# df


        
PAGES = {
     "Page 1" : page_1,
     "Page 2" : page_2,
     "Page 3" : page_3,
     "kalkulatorsegitiga" : kalkulatorsegitiga,
     "konverensi foto" : main
    }   
st.sidebar.image("anos.jpg", width=100)
page = st.sidebar.radio("Halaman", list(PAGES.keys()))
PAGES[page]()

st.markdown(
    """
    
             <style>
             [Data-testid="stActionButtonIcon"]{
                 display: none;
             }
             [data-testid="baseButton-header"]{
                 display: none;
             }
             
             </style>
             """,
    unsafe_allow_html=True,
)