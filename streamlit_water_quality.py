import joblib
import pandas as pd
import streamlit as st

model = joblib.load('model.pkl')

st.write("#### Klasifikasi Kualitas Air untuk Kebutuhan Air Minum Layak Konsumsi")

col1, col2, col3 = st.columns(3)

ph = col1.number_input("Masukkan PH Air")
hardness = col2.number_input("Masukkan Kesadahan Air")
solids = col3.number_input("Masukkan Zat Padat dalam Air")
chloramines = col1.number_input("Masukkan Kandungan Kloramina dalam Air")
sulfate = col2.number_input("Masukkan Kandungan Sulfat dalam Air")
conductivity = col3.number_input("Masukkan Konduktivitas Air")
organic = col1.number_input("Masukkan Total Organik Karbon dalam Air")
trihalomethanes = col2.number_input("Masukkan Kandungan Trihalometan dalam Air")
turbidity = col3.number_input("Masukkan Tingkat Kekeruhan Air")

df_pred = pd.DataFrame([[ph,hardness,solids,chloramines,sulfate,conductivity,organic,trihalomethanes,turbidity]],
columns = ['ph','Hardness','Solids','Chloramines','Sulfate','Conductivity','Organic_carbon','Trihalomethanes','Turbidity'])

prediction = model.predict(df_pred)

if st.button('Prediksi'):
    if(prediction[0] == 0):
        st.write('<p class="big-font">Air Layak untuk Diminum.</p>', unsafe_allow_html=True)
    else:
        st.write('<p class="big-font">Air Tidak Layak untuk Diminum.</p>', unsafe_allow_html=True)