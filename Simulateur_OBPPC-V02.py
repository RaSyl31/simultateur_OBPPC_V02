import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Base de données PVF", layout="wide")
st.title("1. Génération du Tableau de Base (Données enrichies)")

# ==========================================
# 1. RÉFÉRENTIEL FIXE (Les 39 SKU)
# ==========================================
data_fixe = [
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "VER", "Contenance en cl": 30, "Format": "VC30", "SKU": "Caprice Ananas 30 cl VER", "PVF": 1200},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "VER", "Contenance en cl": 30, "Format": "VC30", "SKU": "Caprice Grenadine 30 cl VER", "PVF": 1200},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "VER", "Contenance en cl": 30, "Format": "VC30", "SKU": "Caprice Orange 30 cl VER", "PVF": 1200},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Tonic", "Emballage": "VER", "Contenance en cl": 30, "Format": "VC30", "SKU": "Tonic 30 cl VER", "PVF": 1200},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "World Cola", "Emballage": "VER", "Contenance en cl": 30, "Format": "VC30", "SKU": "World Cola 30cl VER", "PVF": 1200},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "World Cola", "Emballage": "VER", "Contenance en cl": 30, "Format": "VC30", "SKU": "World Cola 30cl WOCO VER", "PVF": 1200},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "PET", "Contenance en cl": 35, "Format": "PET35", "SKU": "Caprice Bonbon Anglais 35 cl PET", "PVF": 1500},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "PET", "Contenance en cl": 35, "Format": "PET35", "SKU": "Caprice Grenadine 35 cl PET", "PVF": 1500},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "PET", "Contenance en cl": 35, "Format": "PET35", "SKU": "Caprice Orange 35 cl PET", "PVF": 1500},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "World Cola", "Emballage": "PET", "Contenance en cl": 35, "Format": "PET35", "SKU": "World Cola 35cl PET", "PVF": 1500},
    {"Entreprise": "HABIBO", "Segment": "BG", "Marque": "Coca-Cola", "Emballage": "PET", "Contenance en cl": 35, "Format": "PET35", "SKU": "Coca-Cola PET35", "PVF": 1500},
    {"Entreprise": "HABIBO", "Segment": "BG", "Marque": "Fanta", "Emballage": "PET", "Contenance en cl": 35, "Format": "PET35", "SKU": "Fanta PET35", "PVF": 1500},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "PET", "Contenance en cl": 50, "Format": "PET50", "SKU": "Caprice Bonbon Anglais 50 cl PET", "PVF": 2000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "PET", "Contenance en cl": 50, "Format": "PET50", "SKU": "Caprice Grenadine 50 cl PET", "PVF": 2000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "PET", "Contenance en cl": 50, "Format": "PET50", "SKU": "Caprice Orange 50 cl PET", "PVF": 2000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "World Cola", "Emballage": "PET", "Contenance en cl": 50, "Format": "PET50", "SKU": "World Cola 50cl PET", "PVF": 2000},
    {"Entreprise": "HABIBO", "Segment": "BG", "Marque": "Coca-Cola", "Emballage": "PET", "Contenance en cl": 50, "Format": "PET50", "SKU": "Coca-Cola PET50", "PVF": 2000},
    {"Entreprise": "HABIBO", "Segment": "BG", "Marque": "Fanta", "Emballage": "PET", "Contenance en cl": 50, "Format": "PET50", "SKU": "Fanta PET50", "PVF": 2000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "CAN", "Contenance en cl": 33, "Format": "CAN33", "SKU": "Caprice Bonbon Anglais 33 cl CAN", "PVF": 2500},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "CAN", "Contenance en cl": 33, "Format": "CAN33", "SKU": "Caprice Grenadine 33 cl CAN", "PVF": 2500},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "CAN", "Contenance en cl": 33, "Format": "CAN33", "SKU": "Caprice Orange 33 cl CAN", "PVF": 2500},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "World Cola", "Emballage": "CAN", "Contenance en cl": 33, "Format": "CAN33", "SKU": "World Cola 33 cl CAN", "PVF": 2500},
    {"Entreprise": "HABIBO", "Segment": "BG", "Marque": "Coca-Cola", "Emballage": "CAN", "Contenance en cl": 33, "Format": "CAN33", "SKU": "Coca-Cola CAN33", "PVF": 2500},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "VER", "Contenance en cl": 100, "Format": "VC100", "SKU": "Caprice Ananas 100 cl VER", "PVF": 3000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "VER", "Contenance en cl": 100, "Format": "VC100", "SKU": "Caprice Bonbon Anglais 100 cl VER", "PVF": 3000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "VER", "Contenance en cl": 100, "Format": "VC100", "SKU": "Caprice Grenadine 100 cl VER", "PVF": 3000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "VER", "Contenance en cl": 100, "Format": "VC100", "SKU": "Caprice Orange 100 cl VER", "PVF": 3000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Tonic", "Emballage": "VER", "Contenance en cl": 100, "Format": "VC100", "SKU": "Tonic 100 cl VER", "PVF": 3000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "World Cola", "Emballage": "VER", "Contenance en cl": 100, "Format": "VC100", "SKU": "World Cola 100cl VER", "PVF": 3000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "World Cola", "Emballage": "VER", "Contenance en cl": 100, "Format": "VC100", "SKU": "World Cola 100cl WOCO VER", "PVF": 3000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "PET", "Contenance en cl": 150, "Format": "PET150", "SKU": "Caprice Ananas 150 cl PET", "PVF": 5000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "PET", "Contenance en cl": 150, "Format": "PET150", "SKU": "Caprice Bonbon Anglais 150 cl PET", "PVF": 5000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "PET", "Contenance en cl": 150, "Format": "PET150", "SKU": "Caprice Grenadine 150 cl PET", "PVF": 5000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "PET", "Contenance en cl": 150, "Format": "PET150", "SKU": "Caprice Orange 150 cl PET", "PVF": 5000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "World Cola", "Emballage": "PET", "Contenance en cl": 150, "Format": "PET150", "SKU": "World Cola 150cl PET", "PVF": 5000},
    {"Entreprise": "HABIBO", "Segment": "BG", "Marque": "Coca-Cola", "Emballage": "PET", "Contenance en cl": 150, "Format": "PET150", "SKU": "Coca-Cola PET150", "PVF": 5000},
    {"Entreprise": "HABIBO", "Segment": "BG", "Marque": "Fanta", "Emballage": "PET", "Contenance en cl": 150, "Format": "PET150", "SKU": "Fanta PET150", "PVF": 5000},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "FUT", "Contenance en cl": 2000, "Format": "FUT2000", "SKU": "Caprice Bonbon Anglais 20L FUT", "PVF": 65004},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "Caprice", "Emballage": "FUT", "Contenance en cl": 2000, "Format": "FUT2000", "SKU": "Caprice Orange 20L FUT", "PVF": 65004},
    {"Entreprise": "STAR", "Segment": "BG", "Marque": "World Cola", "Emballage": "FUT", "Contenance en cl": 2000, "Format": "FUT2000", "SKU": "World Cola 20L FUT", "PVF": 65004},
]
df_fixe = pd.DataFrame(data_fixe)

# ==========================================
# 2. UPLOAD ET TRAITEMENT
# ==========================================
st.sidebar.header("Importer le fichier de ventes")
uploaded_file = st.sidebar.file_uploader("Fichier Excel/CSV", type=["xlsx", "csv"])

if uploaded_file is not None:
    try:
        # Lecture (skiprows=2 pour sauter l'en-tête complexe)
        if uploaded_file.name.endswith('.csv'):
            df_raw = pd.read_csv(uploaded_file, skiprows=2)
        else:
            df_raw = pd.read_excel(uploaded_file, skiprows=2)

        # Garder les colonnes Articles (0), Vente A (1), Evol (2)
        df_raw = df_raw.iloc[:, [0, 1, 2]] 
        df_raw.columns = ['SKU', 'A', 'Evol_Pct']

        # --- NETTOYAGE ---
        # Supprimer les lignes vides ou "Total"
        df_raw = df_raw.dropna(subset=['SKU'])
        df_raw['SKU'] = df_raw['SKU'].astype(str).str.strip()
        df_raw = df_raw[~df_raw['SKU'].str.lower().isin(['', 'total', 'nan'])]

        # Convertir A en float (nettoyer les espaces et virgules)
        df_raw['A'] = df_raw['A'].astype(str).str.replace(' ', '').str.replace(',', '.')
        df_raw['A'] = pd.to_numeric(df_raw['A'], errors='coerce').fillna(0)

        # Convertir Evol en float
        df_raw['Evol_Pct'] = df_raw['Evol_Pct'].astype(str).str.replace('%', '').str.replace(' ', '').str.replace(',', '.')
        df_raw['Evol_Pct'] = pd.to_numeric(df_raw['Evol_Pct'], errors='coerce')

        # --- CALCUL DE A-1 ---
        def calculate_A1(row):
            evol = row['Evol_Pct']
            val_A = row['A']
            if pd.isna(evol) or val_A == 0:
                return val_A # Si évolution vide, on suppose A-1 = A
            elif evol <= -100:
                return 0.0 # Si -100%, A-1 = 0
            else:
                return val_A / (1 + (evol / 100))

        df_raw['A-1'] = df_raw.apply(calculate_A1, axis=1)

        # --- CALCUL DE LA PART ---
        total_general = df_raw['A'].sum()
        df_raw['Part vs Réal A'] = (df_raw['A'] / total_general) * 100

        # --- FUSION ---
        df_final = pd.merge(df_fixe, df_raw, on="SKU", how="left")
        
        # Remplir les NaN par 0 pour les ventes et la part
        df_final['A'] = df_final['A'].fillna(0)
        df_final['A-1'] = df_final['A-1'].fillna(0)
        df_final['Part vs Réal A'] = df_final['Part vs Réal A'].fillna(0)

        # --- FORMATAGE POUR L'AFFICHAGE (comme dans votre exemple) ---
        df_affichage = df_final.copy()
        
        # Formater les prix avec espace (ex: 1 200 Ar)
        df_affichage['PVF'] = df_affichage['PVF'].apply(lambda x: f"{int(x):,} Ar".replace(',', ' '))
        
        # Formater A et A-1 avec espace pour les milliers et virgule pour les décimales
        def format_nombre(val):
            if pd.isna(val): return ""
            # Format: 1 958 734,00
            return f"{val:,.2f}".replace(',', ' ').replace('.', ',')
            
        df_affichage['A-1'] = df_affichage['A-1'].apply(format_nombre)
        df_affichage['A'] = df_affichage['A'].apply(format_nombre)
        
        # Formater la part en %
        df_affichage['Part vs Réal A'] = df_affichage['Part vs Réal A'].apply(lambda x: f"{x:.2f}%".replace('.', ','))

        # Affichage du tableau
        st.subheader("Tableau de Base Enrichi")
        st.dataframe(df_affichage, use_container_width=True, hide_index=True)

    except Exception as e:
        st.error(f"Erreur lors du traitement : {e}")
else:
    st.info("Veuillez uploader le fichier Excel pour générer le tableau.")
