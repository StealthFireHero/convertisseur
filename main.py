import streamlit as st
from datetime import datetime

def enregistrer_conversion(texte):
    maintenant = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("Historique_conversions_gramme.txt", "a") as f:
        f.write(f"[{maintenant}] {texte}\n")

st.title("Convertisseur de Grammes")

option = st.selectbox("Choisis une conversion :", [
    "Gramme en Livres (lb)",
    "Gramme en Once (oz)",
    "Gramme en Stone (st)",
    "Gramme en Grain (gr)",
    "Gramme en Carat (ct)"
])

grammes = st.number_input("Masse en grammes :", min_value=0.0)

if st.button("Convertir"):
    if option == "Gramme en Livres (lb)":
        valeur = grammes / 453.59237
        unite = "lb"
    elif option == "Gramme en Once (oz)":
        valeur = grammes / 28.34952
        unite = "oz"
    elif option == "Gramme en Stone (st)":
        valeur = grammes / 6350.29318
        unite = "st"
    elif option == "Gramme en Grain (gr)":
        valeur = grammes * 15.43236
        unite = "gr"
    elif option == "Gramme en Carat (ct)":
        valeur = grammes * 5
        unite = "ct"

    texte = f"{grammes} g équivalent à {valeur:.4f} {unite}"
    st.success(texte)
    enregistrer_conversion(texte)
