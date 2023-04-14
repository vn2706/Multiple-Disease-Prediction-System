import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
import cv2
psymptom=[]

st.set_page_config(page_title="Multiple Disease Prediction System", page_icon=":stethoscope:",layout="wide")

# function to obtain user symptoms
def get_symptoms1():
    options = sorted(l1)
    symptom1 = st.selectbox('What are you experiencing',options,key="1")
    symptom2 = st.selectbox('What are you experiencing',options,key="2")
    symptom3 = st.selectbox('What are you experiencing',options,key="3")
    symptom4 = st.selectbox('What are you experiencing',options,key="4")
    symptom5 = st.selectbox('What are you experiencing',options,key="5")
    symptoms = [symptom1,symptom2,symptom3,symptom4,symptom5]
    
    answer = st.radio("Would you like to enter more symptoms?",("Yes","No"),index = 1)
    if answer == "Yes":
        symptom = st.text_input("Enter number of symptms:",1)
        for i in range(int(symptom)):
            symptomn = st.selectbox('What are you experiencing',options,i)
            symptoms.append(symptomn)
    if answer == "No":
        symptoms = symptoms[:5]
    return symptoms
#-----------------------------------------------------------functions to deploy machine learning models and incorporation into Streamlit framework----------
def DecisionTree():
    from sklearn import tree
    z = tree.DecisionTreeClassifier() 
    z = z.fit(X,y)

    from sklearn.metrics import accuracy_score
    y_pred=z.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    for i in range(0,len(symptom)):
        value = symptom[i]
        psymptom.append(value)
    for k in range(0,len(l1)):
        for c in psymptom:
            if(c==l1[k]):
                l2[k]=1
    inputtest = [l2]
    predict = z.predict(inputtest)
    predicted=predict[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break
    if (h=='yes'):
        result=disease[a]
        st.success(result)
        
    else:
        result="You seem to be healthy. Take Care!"
        st.success(result)
        
def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))
    # calculating accuracy 
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    for i in range(0,len(symptom)):
        value = symptom[i]
        psymptom.append(value)
    for k in range(0,len(l1)):
        for z in psymptom:
            if(z==l1[k]):
                l2[k]=1
    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]
    h='no'
    for a in range(0,len(disease)):
         if(predicted == a):
             h='yes'
             break
    if (h=='yes'):
         result=disease[a]
         st.success(result)
         
    else:
         result="Not found"
         st.success(result)
         
def NB():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    for i in range(0,len(symptom)):
        value = symptom[i]
        psymptom.append(value)
    for k in range(0,len(l1)):
        for z in psymptom:
            if(z==l1[k]):
                l2[k]=1
    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break
    if (h=='yes'):
        result=disease[a]
        st.success(result)
    else:
        result="Not found"
        st.success(result)
        
# ----------------------------------------------------------end of function block---------------------------------------------------------------------------

# list of symptoms
l1=['None','itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss',
'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin',
'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure',
'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']

# disease list
disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
         
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']
l2=[]
for i in range(0,len(l1)):
    l2.append(0)
    
df=pd.read_csv('Prototype.csv')

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)

tr=pd.read_csv('Prototype-1.csv')

tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

result=""

#---------------------------------------------------------------------------CSS Code-------------------------------------------------------------------
#---styling for buttons---"
st.markdown("""
<style>
    .stButton button {
        border-radius: 50px;
        background-color: #00CED1;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border: none;
        box-shadow: 0px 5px 10px #6495ED;
        display: flex;
        align-items: center;
    }
    .stButton button:hover {
        background-color: #4169E1;
        box-shadow: 0px 3px 6px #4169E1;
    }
    .stButton button i {
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)
#---styling for the hr---"
hr = """
<style>
    .circle {
        width: 15px;
        height: 15px;
        border-radius: 50%;
        display: inline-block;
        margin: 0 10px;
    }
    #circle-1 {
        background-color:  #FF0000;
    }
    #circle-2 {
        background-color: #808080;
    }
    #circle-3 {
        background-color:#008000;
    }
    .circle-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 50px;
    }
</style>
<div class="circle-container">
    <div class="circle" id="circle-1"></div>
    <div class="circle" id="circle-2"></div>
    <div class="circle" id="circle-3"></div>
</div>
"""
#--- CSS style for the expanders---
style = """
    .streamlit-expander {
        border-radius: 10px;
        border: 1px solid #f0f0f0;
        padding: 10px;
        margin-bottom: 10px;
    }

    .streamlit-expanderHeader {
        border-radius: 10px 10px 0px 0px;
        background-color: #E6E6FA;
        padding: 10px;
    }

    .streamlit-expanderContent {
        border-radius: 0px 0px 10px 10px;
        border-top: none;
        margin-top: -10px;
        margin-bottom: 10px;
        padding: 10px;
    }
"""

#------------------------------------------------------------------streamlit framework design-----------------------------------------------------------"

with st.sidebar:
    selected=option_menu('Menu Options',
                         ['Home','Check your Symptoms','View Diagnosis'],
                         icons=['person-circle','file-earmark-medical-fill'],
                         default_index=0)
    image = cv2.imread('image1.png')
    st.sidebar.image(image, caption="", use_column_width=True)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

if selected=='Home':
    st.write("<h1>MULTIPLE DISEASE PREDICTION SYSTEM</h1>", unsafe_allow_html=True)
    st.info("Welcome to the Multiple Disease Prediction System! Our web-application provides you the oppurtunity to gain an understanding of your symptoms.\n Harness the potential of machine learning algorithms to avoid health issues!!!")
    st.write(hr ,unsafe_allow_html=True,)
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("USAGE")
    st.write("<div style='text-align:left; color:blue; font-size:20px;'>Using our web-app has 4 key steps. Expand each step to view.</div>", unsafe_allow_html=True)
    st.write("\n")
    steps = {
    "STEP 1.": "SYMPTOMS SPECIFICATION \n\n <span style='color: red; font-style: italic'> Specify your symptoms using the symptoms select box.",
    "STEP 2.": "OBTAIN RESULT \n\n <span style='color: red; font-style: italic'> Activate each result to understand your symptoms.",
    "STEP 3.": "IDENTIFY POTENTIALLY INFECTED ORGAN \n\n <span style='color: red; font-style: italic'> View the diagnosis to understand which organ could be potentially affected",
    "STEP 4.": "<span style='color: red; font-style: italic'> If the diagnosis suggests you may have a particular condition, follow up with your doctor. If your symptoms are severe or you have other concerns, seek medical attention immediately."
    }
    st.write(f"<style>{style}</style>", unsafe_allow_html=True)
    for step_title, step_content in steps.items():
        with st.expander(step_title):
            st.write(step_content,unsafe_allow_html=True)
    st.write(hr ,unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("ACCESS ANYWHERE!")
    st.write("<div style='text-align:left; color:blue; font-size:20px;'>Access our web-app anywhere, anytime for better health-care & management!!!.</div>", unsafe_allow_html=True)
    image1 = cv2.imread('image3.jpeg')
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(image1, width=800,use_column_width=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
if selected=='Check your Symptoms':
        
    st.title("Symptoms Checker")
      
    OPTIONS = sorted(l1)       
    symptom = get_symptoms1()
    for value in symptom:
        if value =='None':
            continue
        else:
            psymptom.append(value)
            
    print(psymptom)
    
    if len(psymptom) < 1:
        st.warning(' No symptoms have been selcted. To proceed, please select accordingly')
        
    if len(psymptom)<3:
        st.warning("Please enter at least 3 symptoms.")
    elif len(set(psymptom)) != len(psymptom):
        st.warning("Duplicate symptoms selected!!! Please select accordingly.")
    else:
    
        if st.button('RESULT 1 : DT'):
            DecisionTree()
        if st.button('RESULT 2 : RF'):
            randomforest()
        if st.button('RESULT 3 : NB'):
            NB()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------       
if selected=='View Diagnosis':
    if st.button('View Diagnosis'):
        img = cv2.imread('image2.png')
        x, y, w, h = (275, 120, 296, 141)  
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        st.image(img, caption='Human Body with Infected Organ Highlighted',width=500)
