import pickle
import streamlit as st

#membaca model
diabetes_model = pickle.load(open('dp_model.sav', 'rb'))

#judul WEB
st.title('Aplikasi Prediksi Penyakit Diabetes')

#buat tampilan kolom
col1, col2 = st.columns(2)

with col1:
    gender = st.text_input('Input Gender')
    
with col2 :    
    age = st.number_input('Input Umur')

with col1:
    hypertension = st.number_input('Input nilai hipertensi')

with col2 :
    heart_disease = st.number_input('Input Heart Diseas')

with col1:
    smoking_history = st.text_input('Input Smoking History')

with col2:
    bmi = st.number_input('Input BMI')

with col1:
    HbA1c_level = st.number_input('Input HbA1c_level')

with col2:
    blood_glucose_level = st.number_input('Input blood_glucose_level')

if(gender=='Male'):
    gender_x= 1
else:
    gender_x=0

if(smoking_history=='no info'):
    smoking_history_x = 0
elif(smoking_history=='current'):
    smoking_history_x = 1
elif(smoking_history=='ever'):
    smoking_history_x = 2
elif(smoking_history=='former'):
    smoking_history_x = 3
elif(smoking_history=='never'):
    smoking_history_x = 4
elif(smoking_history=='not curent'):
    smoking_history_x = 5

#code prediksi
diab_diagnosis = '' 

#tombol prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[gender_x, age, hypertension, heart_disease, smoking_history_x, bmi, HbA1c_level, blood_glucose_level]])
    if (diab_prediction[0] == 0):
        diab_diagnosis = 'Pasien Tidak Terkena Diabetes'
    else :
        diab_diagnosis = 'Pasien Terkena Diabetes'

    st.success(diab_diagnosis)







