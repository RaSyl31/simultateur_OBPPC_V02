import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Analyse PVF", layout="wide")
st.title("Analyse des Parts de Marché par Tranche de Prix (PVF)")

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

# Liste des PVF avec doublons pour l'effet escalier
liste_pvf = [1000, 1200, 1200, 1500, 1500, 2000, 2000, 2500, 2500, 3000, 3000, 3500, 3500, 4000, 4000, 4500, 4500, 5000, 5000]

# ==========================================
# 2. UPLOAD ET TRAITEMENT
# ==========================================
st.sidebar.header("Importer le fichier de ventes")
uploaded_file = st.sidebar.file_uploader("Fichier Excel/CSV", type=["xlsx", "csv"])

if uploaded_file is not None:
    try:
        # Lecture du fichier
        if uploaded_file.name.endswith('.csv'):
            df_raw = pd.read_csv(uploaded_file, skiprows=2)
        else:
            df_raw = pd.read_excel(uploaded_file, skiprows=2)

        df_raw = df_raw.iloc[:, [0, 1, 2]] 
        df_raw.columns = ['SKU', 'A', 'Evol_Pct']

        # Nettoyage
        df_raw = df_raw.dropna(subset=['SKU'])
        df_raw['SKU'] = df_raw['SKU'].astype(str).str.strip()
        df_raw = df_raw[~df_raw['SKU'].str.lower().isin(['', 'total', 'nan'])]

        df_raw['A'] = df_raw['A'].astype(str).str.replace(' ', '').str.replace(',', '.')
        df_raw['A'] = pd.to_numeric(df_raw['A'], errors='coerce').fillna(0)

        df_raw['Evol_Pct'] = df_raw['Evol_Pct'].astype(str).str.replace('%', '').str.replace(' ', '').str.replace(',', '.')
        df_raw['Evol_Pct'] = pd.to_numeric(df_raw['Evol_Pct'], errors='coerce')

        # Calcul A-1
        def calculate_A1(row):
            evol = row['Evol_Pct']
            val_A = row['A']
            if pd.isna(evol) or val_A == 0: return val_A
            elif evol <= -100: return 0.0
            else: return val_A / (1 + (evol / 100))
        df_raw['A-1'] = df_raw.apply(calculate_A1, axis=1)

        # Calcul Part
        total_general = df_raw['A'].sum()
        df_raw['Part vs Réal A'] = (df_raw['A'] / total_general) * 100

        # Fusion
        df_final = pd.merge(df_fixe, df_raw, on="SKU", how="left")
        df_final['A'] = df_final['A'].fillna(0)
        df_final['A-1'] = df_final['A-1'].fillna(0)
        df_final['Part vs Réal A'] = df_final['Part vs Réal A'].fillna(0)

        # ==========================================
        # 3. AFFICHAGE DU TABLEAU PRINCIPAL
        # ==========================================
        df_affichage = df_final.copy()
        
        # Formater les prix avec espace
        df_affichage['PVF'] = df_affichage['PVF'].apply(lambda x: f"{int(x):,} Ar".replace(',', ' '))
        
        # Formater A et A-1
        def format_nombre(val):
            if pd.isna(val): return ""
            return f"{val:,.2f}".replace(',', ' ').replace('.', ',')
            
        df_affichage['A-1'] = df_affichage['A-1'].apply(format_nombre)
        df_affichage['A'] = df_affichage['A'].apply(format_nombre)
        
        # Formater la part en %
        df_affichage['Part vs Réal A'] = df_affichage['Part vs Réal A'].apply(lambda x: f"{x:.2f}%".replace('.', ','))

        # Sélection des colonnes
        colonnes_a_garder = [
            'Entreprise', 'Segment', 'Marque', 'Emballage', 'Contenance en cl', 
            'Format', 'SKU', 'PVF', 'A-1', 'A', 'Part vs Réal A'
        ]
        df_affichage = df_affichage[colonnes_a_garder]

        st.subheader("1. Tableau de Base Enrichi")
        st.dataframe(df_affichage, use_container_width=True, hide_index=True)

        # ==========================================
        # 4. CALCUL DU TABLEAU DE CUMUL ET GRAPHIQUE
        # ==========================================
        resultats = []
        cumul_habibo = 0.0
        cumul_star = 0.0

        for pvf in liste_pvf:
            part_habibo = df_final[(df_final['PVF'] == pvf) & (df_final['Entreprise'] == 'HABIBO')]['Part vs Réal A'].sum()
            part_star = df_final[(df_final['PVF'] == pvf) & (df_final['Entreprise'] == 'STAR')]['Part vs Réal A'].sum()
            
            if not resultats or resultats[-1]['PVF'] != pvf:
                cumul_habibo += part_habibo
                cumul_star += part_star
            
            resultats.append({
                'PVF': pvf,
                'Cumul HABIBO': cumul_habibo,
                'Cumul STAR': cumul_star,
                'Cumul TOTAL MARCHÉ': cumul_habibo + cumul_star
            })

        df_resultat = pd.DataFrame(resultats)

        # Création du graphique
        st.subheader("2. Graphique d'évolution des cumuls par PVF")
        
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=df_resultat['PVF'], y=df_resultat['Cumul HABIBO'], 
            mode='lines', name='Cumul Habibo', 
            line=dict(shape='hv', color='#7b2cbf', width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=df_resultat['PVF'], y=df_resultat['Cumul STAR'], 
            mode='lines', name='Cumul Star', 
            line=dict(shape='hv', color='#0077b6', width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=df_resultat['PVF'], y=df_resultat['Cumul TOTAL MARCHÉ'], 
            mode='lines', name='Cumul TOTAL MARCHÉ', 
            line=dict(shape='hv', color='#f77f00', width=2)
        ))

        # Annotations
        df_annot = df_resultat.drop_duplicates(subset=['PVF'], keep='last')
        annotations = []
        
        for i, row in df_annot.iterrows():
            if row['Cumul TOTAL MARCHÉ'] > 0:
                annotations.append(dict(
                    x=row['PVF'],
                    y=row['Cumul TOTAL MARCHÉ'],
                    text=f"{int(row['PVF'])} Ar; {row['Cumul TOTAL MARCHÉ']:.2f}%",
                    showarrow=True,
                    arrowhead=2,
                    ax=-50,
                    ay=-30,
                    bgcolor="white",
                    bordercolor="gray",
                    borderwidth=1,
                    font=dict(size=11, color="black")
                ))

        fig.update_layout(
            annotations=annotations,
            xaxis_title="Prix (Ar)",
            yaxis_title="Pourcentage (%)",
            yaxis=dict(tickformat=".2f", range=[0, 105]),
            xaxis=dict(
                tickmode='array', 
                tickvals=sorted(list(set(liste_pvf))),
                range=[0, 5500] # Pour zoomer et ignorer les prix > 5500
            ),
            legend=dict(
                orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5
            ),
            hovermode="x unified",
            template="plotly_white",
            height=700,
            margin=dict(l=40, r=40, t=40, b=40)
        )

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Erreur lors du traitement : {e}")
else:
    st.info("Veuillez uploader le fichier Excel pour générer l'analyse.")
