# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:53:28 2023

@author: giris
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open("C:/Users/giris/OneDrive/Desktop/multiple disease prediction system/saved models/diabetes_model .sav", "rb"))

heart_disease_model = pickle.load(open("C:/Users/giris/OneDrive/Desktop/multiple disease prediction system/saved models/heart_disease_model (1).sav","rb"))

bp_disease_model = pickle.load(open("C:/Users/giris/OneDrive/Desktop/multiple disease prediction system/saved models/bp_model (1).sav","rb"))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Prediction System',
                          
                          ['Diabetes Prediction',
                           'Blood Pressure Prediction',
                           'Heart Disease Prediction' ],
                          icons=['activity','person','heart',],
                          default_index=0)




# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('DIABETES')
    st.markdown('## PREDICTION SYSTEM')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = """The person is diabetic.
          
          Kindly view the diagnosis system below  """
          
          
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

     
    
# Blood Pressure Prediction Page
if (selected == 'Blood Pressure Prediction'):
    
    # page title
    st.title('BLOOD PRESSURE')
    st.markdown('## PREDICTION SYSTEM')
    
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Level_of_Hemoglobin = st.text_input("Level of Hemoglobin")
        
    with col2:
        Age = st.text_input("Age")
    
    with col3:
       BMI = st.text_input("BMI value")
    
    with col1:
        Sex = st.text_input("Sex")
    
    with col2:
        Smoking = st.text_input("Smoking")
    
    with col3:
       Physical_activity= st.text_input("Physical activity")
    
    with col1:
        salt_content_in_the_diet = st.text_input("salt content in the diet")
    
    with col2:
        Level_of_Stress = st.text_input("Level of Stress")
        
    with col3:
        Chronic_kidney_disease = st.text_input("Chronic_kidney_disease")
        
    with col1:
        Adrenal_and_thyroid_disorders = st.text_input("Adrenal_and_thyroid_disorders")
    
    # code for Prediction
    bp_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('bp Test Result'):
        bp_prediction = bp_disease_model.predict([[float(Level_of_Hemoglobin),int(Age),int(BMI),int(Sex),int(Smoking),int(Physical_activity),int(salt_content_in_the_diet),int(Level_of_Stress),int(Chronic_kidney_disease),int(Adrenal_and_thyroid_disorders)]])
        
        if (bp_prediction[0] == 1):
          bp_diagnosis = """The person is not bp patient.
          
          Kindly view the diagnosis system below """
          
        else:
          bp_diagnosis = 'The person is bp patient'
        
    st.success(bp_diagnosis)

    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('HEART DISEASE')
    st.markdown('## PREDICTION SYSTEM')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal:')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[int(age),int(sex),int(cp),int(trestbps),int(chol),int(fbs),int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = """The person is having heart disease. 
          
          Kindly view the diagnosis system below """
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)

with st.sidebar:
    
    selected = option_menu('Diagnosis System',
                          
                          ['Diabetes Diagnosis', 
                           'Blood Pressure Diagnosis',
                           'Heart Disease Diagnosis' ],
                          icons=['activity','person','heart'],
                          default_index=0)

# Diabetes Diagnosis Page
if(selected == 'Diabetes Diagnosis'):
    st.title('DIAGNOSIS SYSTEM')
    st.write(""" lOW SUGAR LEVELS
             
         Before fasting : less than 60mg/dl 
         After fasting : less than 70mg/dl.
        
             """)
    st.write(""" HIGH SUGAR LEVELS :
              
             Before fasting : Greater  than 100mg/dl 
             After fasting : Greater than 140mg/dl.
         
              """)
    if st.checkbox("Allopathic Remedies"):
        if st.checkbox("low Sugar"):
            st.write(""" Prescribed Medicines:
                      
                      Diazoxide , Octreotide , Dextrose ,Glucagon .                    
                     """)
        elif st.checkbox("High sugar"):
           st.write(""" Prescribed Medicines:
                     
                    DPP-4 inhibitors , Sulfonylureas , Metformin ,SGLT2 inhibitors .
                     
                    """)
      
    elif st.checkbox("Homeopathy Remedies"):
         if st.checkbox("low Sugar"):
             st.write(""" Prescribed Medicines:
                       
                       Nux vomica , Oenothera biennis , Arsenicum  .
                       
                      """)
         elif st.checkbox("High sugar"):
            st.write(""" Prescribed Medicines:
                      
                     Abroma Augusta , Syzygium Jambolanum , Phosphoric acid , Phosphorus .
                      
                     """)
    elif st.checkbox("Ayurvedic remedies"):
        if st.checkbox("low Sugar"):
            st.write(""" Prescribed Medicines:
                      
                      Amla , Cinnamon ,Fenugreek , Bitter Gourd  .
                      
                     """)
        elif st.checkbox("High sugar"):
           st.write(""" Prescribed Medicines:
                     
                    Turmeric , Gymnema Sylvestre ,Holy Basil (Tulsi) , Ginger .
                    
                    """)
    else:
        pass

    
 # Blood Pressure Diagnosis Page   
if(selected == 'Blood Pressure Diagnosis'):
    st.title('DIAGNOSIS SYSTEM')
    st.write(""" lOW BP LEVELS
             
         Systolic Blood pressure :less than 120 mmGh
         Diasystolic Blood pressure :less than 80mGh
         
             """)
    st.write(""" HIGH BP LEVELS :
              
             Systolic Blood pressure :greater than 129 mmGh
             Diasystolic Blood pressure :greater than 89 mmGh
             
              """)
    if st.checkbox("Allopathic Remedies"):
         if st.checkbox("low BP"):
             st.write(""" Prescribed Medicines:
                       
                       fludrocortisone , Orvaten.
                       
                      """)
         elif st.checkbox("High BP"):
            st.write(""" Prescribed Medicines:
                      
                     Captopril, Fasinopril, Acebutolol, Betaxolol, Kateriazia .
                      
                     """)           
    elif st.checkbox("Homeopathy Remedies"):
         if st.checkbox("low BP"):
             st.write(""" Prescribed Medicines:
                       
                     Gelsemium,Carbo vegetabilis,Natrum muriaticum,China.
                      """)
         elif st.checkbox("High BP"):
            st.write(""" Prescribed Medicines:
                      
                     Belladonna,Natrum muriaticum,Nux vomica,Crataegus.
                     """)   
    elif st.checkbox("Ayurvedic remedies"):
        if st.checkbox("low BP"):
            st.write(""" Prescribed Medicines:
                      
                    Gelsemium,Carbo vegetabilis,Natrum muriaticum,China.                      
                     """)
        elif st.checkbox("High BP"):
           st.write(""" Prescribed Medicines:
                     
                    AYUR Sarpgandha , Desi Ashwagandha , Arjun Chaal ,Brahmi .
                     
                    """)   
    else:
        pass


#Heart Disease Diagnosis Page
if(selected == 'Heart Disease Diagnosis'):
    st.title('DIAGNOSIS SYSTEM')
    if st.checkbox("Allopathic Remedies"):
     st.write(""" Prescribed Medicines:
               
              Statins , Beta -Blockers , Aspirin ,Clopidogrel , Warfarin ,ACE Inhibitors.
               
              """)
    elif st.checkbox("Homeopathy Remedies"):
         st.write(""" Prescribed Medicines:
                   
                  Latrodectus,Aurum metallium,Aconitum Catus ,Digitalis,Glononium
                   
                  """)
    elif st.checkbox("Ayurvedic remedies"):
        st.write(""" Prescribed Medicines:
                  
                Triphila,Ashwagandha ,Noni capsules,Nerve Up tablet,Hrudroga Chintamani Rasa
                  
                 """)
    else:
        pass

st.markdown(""" # GENERAL PRECAUTIONS
         
        ### Have 8 hrs of sleep.     Make sure that you have your meal on time.    Regularly do exercise.   """)
    