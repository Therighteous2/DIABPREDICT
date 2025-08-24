#A propos
import streamlit as st

st.title("A propos")
st.markdown(
    """<h3 style='color: Black;'>
Cette application web est conçue pour prédire la probabilité
qu'un patient ait du diabète en fonction de ses données médicales.
Le modèle a été entrainé sur le Pima Indians Diabetes Dataset et ne peut être précis 
pour d'autres populations.
C'est le fruit d'un memoire de fin d'études en Licence de Genie informatique à l'Université Officielle de Mbujimayi.

  </h3>  """, unsafe_allow_html=True
)
st.sidebar.header("**Concepteur et réalisateur**")
st.sidebar.image('C:\\Users\\windows 10\\Desktop\\MyProject\\images\\Admin.jpg',use_container_width=True)
st.sidebar.info("**Abel MUBENGA K.**")
st.sidebar.markdown(
    """*Etudiant en Génie Informatique, chercheur en Génie logiciel et Machine Learning*
    """
)

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

