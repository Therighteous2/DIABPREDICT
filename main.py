import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="www.diabpredict.cd",
    layout="centered"

)

#Basculement multipage
page_un = st.Page(
    page= "Info.py",
    title= "Informations"
)
page_deux = st.Page(
    page= "Formulaire_saisie.py",
    title= "Prédire le diabète"
)
page_trois = st.Page(
    page= "Apropos.py",
    title= "A propos de nous"
)

pages = st.navigation([page_un,page_deux,page_trois]
                      
        )
pages.run()

st.markdown("___________")
st.write("**Anticipez le diabète,protégez votre avenir santé!**")
st.markdown(""" 
Notre outil intelligent analyse vos données pour prédire votre risque de diabète en quelques clics!
Entrez vos données telles que l'âge, IMC, antécédents, etc. L'IA analyse vos informations et vous recevrez une prédiction claire.""")

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




