import os 
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# set page configuration

st.set_page_config(page_title="Prediction of Disease Outbreaks",
                   layout="wide",
                   page_icon="👨‍⚕️")

#getting the working directory of the main.py
working_dir=os.path.dirname(os.path.abspath(__file__))

#loading the saved models

diabetes_model=pickle.load(open(r"C:\Prediction_of_Disease_Outbreaks\diabetes_model.sav",'rb'))

heart_disease_model=pickle.load(open(r"C:\Prediction_of_Disease_Outbreaks\heart_disease_model.sav",'rb'))

parkinsons_model=pickle.load(open(r"C:\Prediction_of_Disease_Outbreaks\parkinsons_disease_model.sav",'rb'))

# sidebar for navigation

with st.sidebar:
    selected=option_menu('Prediction of Disease Outbreaks Systems',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                          menu_icon='hospital-fill',
                          icons=['activity', 'heart','person'],
                          default_index=0)
# diabetes prediction page

if selected== 'Diabetes Prediction':
    #page title 
    st.title('Diabetes Prediction using ML')

    #getting the input data from the user 
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose=st.text_input('Gulcose Level')
    with col3:
        BloodPressure=st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')
    with col2:
        Insulin=st.text_input('Insulin Level')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age=st.text_input('Age of the Person')

     # code for prediction 
    diab_diagnosis= ' '

    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies,Glucose,BloodPressure, SkinThickness, Insulin,
                        BMI,DiabetesPedigreeFunction, Age]
        user_input=[float(x) for x in user_input]

        diab_prediction=diabetes_model.predict([user_input])

        if diab_prediction[0]==1:
            diab_diagnosis='The Person is Diabetic'
        else:
            diab_diagnosis='The Person is Not Diabetic '
    st.success(diab_diagnosis)

# heart disease prediction page 
if selected== 'Heart Disease Prediction':
    #page title 
    st.title('Heart Disease Prediction using ML')

    #getting the input data from the user 
    col1, col2, col3 = st.columns(3)
    with col1:
        age=st.text_input('Age')
    with col2:
        sex=st.text_input('Sex')
    with col3:
        cp=st.text_input('Chest Pain Types')
    with col1:
        trestbps=st.text_input('Resting Blood Pleasure')
    with col2:
        chol=st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs=st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg=st.text_input('Resting Electrocardiographic Results')
    with col2:
        thalach=st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang=st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak=st.text_input('ST Depression Induced By Exercise')
    with col2:
        slope=st.text_input('Slope of the Peak Exercise ST Segment')
    with col3:
        ca=st.text_input('Major Vessels Colored by Flourosopy')
    with col1:
        thal=st.text_input('thal: 0 = Normal; 1 = Fixed Defect; 2= Reversable Effect')

     # code for prediction 
    heart_diagnosis= ' '

    #creating a button for prediction
    if st.button('Heart Disease Test Result'):
        user_input=[age, sex, cp, trestbps,chol, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input=[float(x) for x in user_input]

        heart_prediction=heart_disease_model.predict([user_input])

        if heart_prediction[0]==1:
            heart_diagnosis='The Person is Having Heart Disease'
        else:
            heart_diagnosis='The Person Does Not Have Any Heart Disease '
    st.success(heart_diagnosis)

#parkinsons prediction page 
if selected== 'Parkinsons Prediction':
    #page title 
    st.title("Parkinson's Disease Prediction using ML")

    #getting the input data from the user 
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo=st.text_input('MDVP:Fo(HZ)')
    with col2:
        fhi=st.text_input('MDVP:fhi(HZ)')
    with col3:
        flo=st.text_input('MDVP:Flo(HZ)')
    with col4:
        Jitter_percent=st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP=st.text_input('MDVP:RAP')
    with col2:
        PPQ=st.text_input('MDVP:PPQ')
    with col3:
        DDP=st.text_input('Jitter:DDP')
    with col4:
        shimmer=st.text_input('MDVP:shimmer')
    with col5:
        shimmer_dB=st.text_input('MDVP:shimmer(dB)')
    with col1:
        APQ3=st.text_input('shimmer: APQ3')
    with col2:
        APQ5=st.text_input('shimmer: APQ5')
    with col3:
        APQ=st.text_input('shimmer: APQ')
    with col4:
        DDA=st.text_input('shimmer: DDA')
    with col5:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input('DFA')
    with col4:
        spread1=st.text_input('spread1')
    with col5:
        spread2=st.text_input('spread2')
    with col1:
        D2=st.text_input('D2')
    with col2:
        PPE=st.text_input('PPE')
    
     # code for prediction 
    parkinsons_diagnosis= ' '

    #creating a button for prediction
    if st.button("Parkinson's Test Result"):
        user_input=[fo, fhi,flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, shimmer,shimmer_dB, APQ3,APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1,
                    spread2, D2, PPE]
        user_input=[float(x) for x in user_input]

        parkisons_prediction=parkinsons_model.predict([user_input])

        if parkisons_prediction[0]==1:
            parkinsons_diagnosis="The Person Has Parkinson's Disease"
        else:
            parkinsons_diagnosis="The Person Does Not Have Parkinson's Disease"
    st.success(parkinsons_diagnosis)


    
            

