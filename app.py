import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Charger le modèle sauvegardé
model = joblib.load('xgb_model.joblib')

# Définir les colonnes attendues par le modèle
expected_columns = [
    "month_year", "month_month", "town", "flat_type", "storey_range", 
    "floor_area_sqm", "flat_model", "lease_commence_date", 
    "remaining_lease_months", "block"
]

# Ajouter du CSS pour définir l'image de fond
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://topequipementmaison.com/wp-content/uploads/2022/08/limmobilier.jpg');  /* Remplacez par l'URL de votre image */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Titre de l'application
st.title("Prédiction du prix de revente d'un appartement")

# Entrée des caractéristiques utilisateur
month = st.text_input("Mois de la vente (format: YYYY-MM)", value="2024-11")
town = st.selectbox("Ville", ["ANG MO KIO", "BEDOK", "CHOA CHU KANG", "OTHER"])
flat_type = st.selectbox("Type d'appartement", ["2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE"])
block = st.text_input("Bloc", value="123")  # Ajout de la colonne 'block'
street_name = st.text_input("Nom de la rue", value="EXAMPLE STREET")
storey_range = st.selectbox("Tranche d'étage", ["01 TO 03", "04 TO 06", "07 TO 09", "10 TO 12"])
floor_area_sqm = st.number_input("Surface en m²", min_value=0.0, step=0.1, value=50.0)
flat_model = st.selectbox("Modèle d'appartement", ["Improved", "New Generation", "Simplified", "Type S1", "Type S2"])
lease_commence_date = st.number_input("Année de début de bail", min_value=1900, step=1, value=2000)
remaining_lease = st.text_input("Bail restant (ex: 54 years 05 months)", value="54 years 05 months")

# Bouton de prédiction
if st.button("Faire une prédiction"):
    try:
        # Prétraitement des données d'entrée
        # Extraction de l'année et du mois à partir du champ 'month'
        month_date = pd.to_datetime(month, format="%Y-%m", errors="coerce")
        if pd.isnull(month_date):
            st.error("Le mois est invalide. Utilisez le format YYYY-MM.")
            st.stop()
        month_year = month_date.year
        month_month = month_date.month

        # Conversion de `remaining_lease` en mois
        years, months = 0, 0
        if "years" in remaining_lease and "months" in remaining_lease:
            parts = remaining_lease.split(" years ")
            years = int(parts[0])
            months = int(parts[1].replace(" months", ""))
        remaining_lease_months = years * 12 + months

        # Création d'un DataFrame avec les colonnes EXACTEMENT comme lors de l'entraînement
        input_data = pd.DataFrame({
            "month_year": [month_year],
            "month_month": [month_month],
            "town": [town],
            "flat_type": [flat_type],
            "storey_range": [storey_range],
            "floor_area_sqm": [floor_area_sqm],
            "flat_model": [flat_model],
            "lease_commence_date": [lease_commence_date],
            "remaining_lease_months": [remaining_lease_months],
            "block": [block]  # Ajout de la colonne 'block'
        })

        # Afficher les colonnes du DataFrame pour vérifier la correspondance
        st.write(f"Colonnes du DataFrame d'entrée : {input_data.columns.tolist()}")

        # Vérifiez si les colonnes correspondent à celles attendues
        for col in expected_columns:
            if col not in input_data.columns:
                st.error(f"La colonne attendue '{col}' est manquante.")
                st.stop()

        # Assurez-vous que les colonnes sont dans le bon ordre
        input_data = input_data[expected_columns]

        # Conversion des colonnes catégoriques en numériques si nécessaire
        categorical_columns = ["town", "flat_type", "storey_range", "flat_model", "block"]
        for col in categorical_columns:
            input_data[col] = input_data[col].astype("category").cat.codes

        # Afficher le DataFrame après transformation
        st.write(f"DataFrame après transformation : {input_data}")

        # Prédiction
        prediction = model.predict(input_data)
        st.success(f"Le prix prédit de revente est : {prediction[0]:,.2f} €")

    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")
