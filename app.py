import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title='Health Assistant',
                   layout='wide',
                   page_icon='🤡')

# Get working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load saved models
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))
heart_diseas_model = pickle.load(open(f'{working_dir}/heart_diseas_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction Systems',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsosn Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# ------------------- Diabetes Prediction Page ---------------------
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Machine Learning')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            input_data = [
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]
            diab_prediction = diabetes_model.predict([input_data])

            if diab_prediction[0] == 1:
                diab_diagnosis = '✅ The person is diabetic'
            else:
                diab_diagnosis = '✅ The person is not diabetic'

            st.success(diab_diagnosis)

        except:
            st.error("⚠️ Please enter valid numeric values in all fields.")

# ------------------- Heart Disease Prediction Page ---------------------
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using Machine Learning')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1 = Male, 0 = Female)')
    with col3:
        cp = st.text_input('Chest Pain Type (0–3)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Cholesterol Level')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)')

    with col1:
        restecg = st.text_input('Resting ECG (0, 1, 2)')
    with col2:
        thalach = st.text_input('Max Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = Yes, 0 = No)')

    with col1:
        oldpeak = st.text_input('Oldpeak (ST depression)')
    with col2:
        slope = st.text_input('Slope of ST segment')
    with col3:
        ca = st.text_input('Number of Major Vessels (0–3)')

    with col1:
        thal = st.text_input('Thal (1 = Normal, 2 = Fixed Defect, 3 = Reversible)')

    heart_diagnosis = ''

    if st.button('Heart Diseases Test Result'):
        try:
            input_data = [
                float(age), float(sex), float(cp), float(trestbps),
                float(chol), float(fbs), float(restecg), float(thalach),
                float(exang), float(oldpeak), float(slope), float(ca), float(thal)
            ]
            heart_prediction = heart_diseas_model.predict([input_data])

            if heart_prediction[0] == 1:
                heart_diagnosis = '🚨 The person has heart disease'
            else:
                heart_diagnosis = '✅ The person does not have heart disease'

            st.success(heart_diagnosis)

        except:
            st.error("⚠️ Please enter valid numeric values in all fields.")

# ------------------- Parkinson's Prediction Page ---------------------
if selected == 'Parkinsosn Prediction':
    st.title("Parkinson's Disease Prediction using Machine Learning")

    # Define layout
    col1, col2, col3, col4, col5 = st.columns(5)

    # Input fields
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    # Empty variable for result
    parkinsons_diagnosis = ''

    # Prediction logic
    if st.button("Parkinson's Test Result"):
        try:
            input_data = [
                float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
                float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR),
                float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)
            ]

            parkinsons_prediction = parkinsons_model.predict([input_data])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "🚨 The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "✅ The person does not have Parkinson's disease"

            st.success(parkinsons_diagnosis)

        except:
            st.error("⚠️ Please enter valid numeric values in all fields.")


