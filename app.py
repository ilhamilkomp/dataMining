import pickle
import streamlit as st

# membaca dan load model 
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# judul aplikasi 
st.title('Perediksi Diabetes App')

kolom1, kolom2 = st.columns(2)

with kolom1 :   
    Pregnancies = st.text_input('Masukan Nilai Pregnancies')
with kolom2 : 
    Glucose = st.text_input('Masukkan Nilai Glucose')
with kolom1 :
    BloodPressure = st.text_input('Masukkan Nilai BloodePressure')
with kolom2 :
    SkinThickness = st.text_input('Masukkan Nilai SkinThickness')
with kolom1 :
    Insulin = st.text_input('Masukkan Nilai Insulin')
with kolom2 :
    BMI = st.text_input('Masukkan Nilai BMI')
with kolom1 :
    DiabetesPedigreeFunction = st.text_input('Masukkan Nilai DiabetesPedigreeFunction')
with kolom2 :
    Age = st.text_input('Masukkan Nilai Age')

# membuat fungsi untuk memprediksi diabetes berdasarkan input user
diabetes_diagnosis = ''

#tombol prediksi
if (st.button('Prediksi Diabetes')):
    diabetes_prediction = diabetes_model.predict([[
        Pregnancies,
        Glucose,
        BloodPressure,
        SkinThickness,
        Insulin,
        BMI,
        DiabetesPedigreeFunction,
        Age
    ]])

    if(diabetes_prediction[0] == 1):
        diabetes_diagnosis = 'Pasien Terkena Diabetes'
    else :
        diabetes_diagnosis = 'Pasien Tidak Terkena Diabetes'

        st.success(diabetes_diagnosis)
        
