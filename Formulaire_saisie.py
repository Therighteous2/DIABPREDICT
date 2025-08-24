import streamlit as st
from PIL import Image
import numpy as np
import pickle
import time

#Chargement du scaler et du modèle sauvegardé
model = pickle.load(open('C:\\Users\\windows 10\\Desktop\\MyProject\\pages\\model.pkl','rb'))
scaler = pickle.load(open('C:\\Users\\windows 10\\Desktop\\MyProject\\pages\\scaling.pkl','rb'))

#Titre et description de l'application
st.title("DIAGNOSTIC DU DIABETE A PARTIR DES DONNEES CLINIQUES")
st.markdown("*Entrez les données médicales du patient pour prédire s'il est susceptible d'avoir du diabète :*")
#Du code pour la barre latérale
#le logo
img= Image.open('C:\\Users\\windows 10\\Desktop\\MyProject\\images\\logo.png')
st.sidebar.image(img, width=100)

st.sidebar.write("*Anticipez le diabète, protégez votre avenir!*")
st.sidebar.image('C:\\Users\\windows 10\\Desktop\\MyProject\\images\\img01.png',use_container_width=True)
#Formulaire de saisie
with st.form(key='patient_data_form'):
    col1,col2 = st.columns(2) #Diviser les entrées en deux colonnes
    #Les valeurs ci-après sont à vérifier:
    Pregnancies = col1.number_input("Nombre Grossesse(s)", min_value=0,max_value=20,value=5)
    Glucose = col1.number_input("Glucose", min_value=0,max_value=300,value=120)
    BloodPressure = col1.number_input("Pression Arterielle", min_value=12,max_value=200,value=80)
    SkinThickness = col1.number_input("Plis cutanée (Biceps)", min_value=0,max_value=100,value=20)
    Insulin = col2.number_input("Niveau d'insuline", min_value=0,max_value=900,value=80)
    BMI = col2.number_input("Indice de masse corporelle:", min_value=0.0,max_value=70.0,value=25.5,format="%.2f")
    PedegreeFunction = col2.number_input("Facteur héréditaire:", min_value=0.00,max_value=3.00,value=0.02,format="%.2f")
    Age = col2.number_input("Âge:", min_value=0,max_value=120,value=30)
    
    #déclaration du bouton de prédiction
    btn_soumettre = st.form_submit_button("PREDIRE")
    if btn_soumettre:
        with st.spinner("veuillez patienter"):
            time.sleep(2) #Simuler un temps de retard de deux seconde
        #créer un tableau d'entrée
        input_data = np.array([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,PedegreeFunction,Age]).reshape(1,-1)
        #Mettre à l'échelle les données d'entrée
        scaled_data = scaler.transform(input_data)
        #faire la prédiction
        prediction = model.predict(scaled_data)
        #Afficher le résultat
        if prediction[0] == 1:
            #st.toast("**Le patient est diabétique**")
            st.error("**Le patient est diabétique**")
        else:
            st.success("**Le patient est non-diabétique**")

    #CSS pour image de fond
    st.markdown(
         """
        <style>
        .stApp {
            background-image: url("https://images.pexels.com/photos/6941883/pexels-photo-6941883.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
            background-size: cover;
            background-repeat: no-repeat;
            background position:center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.error("Veuillez effacer les valeurs par défaut et remplir celles du patient pour faire la prédiction.")


   







