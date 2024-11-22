import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from datetime import datetime
import os
import base64
from io import BytesIO

# Configurazione della pagina
st.set_page_config(
    page_title="Matheus Lima - Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    """Create a download button for binary files."""
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}" class="download-button">📥 {file_label}</a>'
    return href

def create_skills_radar():
    skills_data = {
        'Categoria': ['Python', 'SQL', 'PowerBI', 'Tableau', 'Machine Learning', 'Excel'],
        'Livello': [100, 70, 60, 70, 90, 100]
    }
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=skills_data['Livello'],
        theta=skills_data['Categoria'],
        fill='toself',
        line_color='#3b82f6',
        fillcolor='rgba(59, 130, 246, 0.3)'
    ))
    
    text_color = 'white' if st.get_option('theme.base') == 'dark' else 'black'
    grid_color = 'rgba(255, 255, 255, 0.2)' if st.get_option('theme.base') == 'dark' else '#e5e7eb'
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                showline=False,
                gridcolor=grid_color,
                tickfont=dict(color=text_color),
            ),
            angularaxis=dict(
                tickfont=dict(color=text_color),
                gridcolor=grid_color
            ),
            bgcolor='rgba(0,0,0,0)'
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=60, b=60)
    )
    
    return fig

def load_image(image_path):
    try:
        if os.path.exists(image_path):
            return Image.open(image_path)
        else:
            st.error(f"Immagine non trovata: {image_path}")
            return None
    except Exception as e:
        st.error(f"Errore nel caricamento dell'immagine: {str(e)}")
        return None

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def local_css():
    st.markdown("""
    <style>
        /* Variabili CSS per il tema */
        :root {
            --background-primary: var(--st-color-background-primary, #f8f9fa);
            --text-primary: var(--st-color-text-primary, #1f2937);
            --text-secondary: var(--st-color-text-secondary, #4b5563);
            --accent-color: #3b82f6;
            --card-background: var(--st-color-background-secondary, white);
            --card-border: var(--st-color-border-light, rgba(0,0,0,0.1));
        }

        [data-theme="dark"] {
            --background-primary: var(--st-color-background-primary, #1a1a1a);
            --text-primary: var(--st-color-text-primary, #ffffff);
            --text-secondary: var(--st-color-text-secondary, #cccccc);
            --card-background: var(--st-color-background-secondary, #2d2d2d);
            --card-border: var(--st-color-border-dark, rgba(255,255,255,0.1));
        }
        
        /* Stile per il pulsante di download */
        .download-button {
            display: inline-block;
            padding: 12px 24px;
            background-color: #3b82f6;
            color: white !important;
            text-decoration: none;
            border-radius: 8px;
            margin: 20px 0;
            font-weight: 500;
            transition: all 0.3s ease;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .download-button:hover {
            background-color: #2563eb;
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }
        
        /* Tema generale */
        .main {
            background-color: var(--background-primary);
            color: var(--text-primary);
        }
        
        /* Stile per i contenitori principali */
        .stTabs [data-baseweb="tab-panel"] {
            background-color: var(--card-background);
            color: var(--text-primary);
            padding: 25px;
            border-radius: 5px;
            box-shadow: 0 2px 4px var(--card-border);
            margin-top: 10px;
        }
        
        /* Card personalizzata */
        .custom-card {
            background-color: var(--card-background);
            color: var(--text-primary);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px var(--card-border);
            margin: 10px 0;
            border: 1px solid var(--card-border);
        }
        
        /* Timeline per le esperienze */
        .timeline-item {
            border-left: 2px solid var(--accent-color);
            padding-left: 20px;
            margin-bottom: 20px;
            position: relative;
            color: var(--text-primary);
        }
        
        .timeline-item::before {
            content: '';
            width: 12px;
            height: 12px;
            background-color: var(--accent-color);
            border-radius: 50%;
            position: absolute;
            left: -7px;
            top: 0;
        }
        
        /* Header personalizzato */
        .header-container {
            background: linear-gradient(135deg, #1e3a8a 0%, var(--accent-color) 100%);
            padding: 2rem;
            border-radius: 10px;
            color: white;
            margin-bottom: 2rem;
        }
        
        .contact-info {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
            color: white;
        }
        
        /* Media queries per dispositivi mobili */
        @media (max-width: 768px) {
            .header-container {
                padding: 1rem;
            }
            
            .header-container > div {
                flex-direction: column !important;
                text-align: center;
                gap: 1rem !important;
            }
            
            .profile-image-container {
                margin: 0 auto;
            }
            
            .contact-info {
                display: flex;
                flex-direction: column;
                gap: 10px;
                text-align: center;
                padding: 15px;
            }
            
            .contact-info span {
                margin: 5px 0;
                display: block;
            }
            
            h1 {
                font-size: 1.5rem !important;
            }
            
            h2 {
                font-size: 1.2rem !important;
            }
            
            .custom-card {
                padding: 15px;
            }
            
            .timeline-item {
                padding-left: 15px;
            }
            
            /* Ottimizzazione colonne per mobile */
            .stColumns {
                flex-direction: column;
            }
            
            .stColumns > div {
                width: 100% !important;
                margin-bottom: 1rem;
            }
            
            /* Ottimizzazione tabs per mobile */
            .stTabs [data-baseweb="tab"] {
                padding: 10px;
                font-size: 0.9rem;
            }
            
            /* Ottimizzazione grafici per mobile */
            .js-plotly-plot {
                height: auto !important;
                max-height: 400px;
            }
            
            /* Ottimizzazione skill cards per mobile */
            .skill-card {
                margin: 8px 0;
                padding: 12px;
            }
            
            /* Miglioramento leggibilità testo su mobile */
            p, li {
                font-size: 0.95rem;
                line-height: 1.5;
            }
        }
    </style>
    """, unsafe_allow_html=True)

def create_skill_progress(skill, level):
    st.markdown(f"""
    <div class="skill-card">
        <h4 style="color: #1f2937; margin-bottom: 10px;">{skill}</h4>
        <div style="background-color: #e5e7eb; height: 10px; border-radius: 5px;">
            <div style="width: {level}%; height: 100%; background-color: #3b82f6; border-radius: 5px;"></div>
        </div>
        <p style="text-align: right; color: #6b7280; margin-top: 5px;">{level}%</p>
    </div>
    """, unsafe_allow_html=True)

def create_timeline_item(title, period, company, description):
    description = description.replace('<b>▶</b>', '<span style="color: #3b82f6; font-weight: 600; font-size: 1.1em;">▶</span>')
    lines = description.split('\n')
    formatted_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith('•'):
            formatted_line = f'<div style="padding-left: 20px; margin: 5px 0;">{line}</div>'
        else:
            formatted_line = f'<div style="margin: 10px 0;">{line}</div>'
        formatted_lines.append(formatted_line)
    
    formatted_description = '\n'.join(formatted_lines)
    
    st.markdown(f"""
    <div class="timeline-item">
        <h3 style="color: #1f2937; margin: 0;">{title}</h3>
        <p style="color: #3b82f6; margin: 5px 0;">{company}</p>
        <p style="color: #6b7280; font-size: 0.9rem; margin: 5px 0;">{period}</p>
        <div style="color: #4b5563; margin-top: 10px;">
            {formatted_description}
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_formatted_text(description):
    description = description.replace('<b>▶</b>', '<span style="color: #3b82f6; font-weight: 600; font-size: 1.1em;">▶</span>')
    lines = description.split('\n')
    formatted_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith('•'):
            formatted_line = f'<div style="padding-left: 20px; margin: 5px 0;">{line}</div>'
        else:
            formatted_line = f'<div style="margin: 10px 0;">{line}</div>'
        formatted_lines.append(formatted_line)
    return '\n'.join(formatted_lines)

def main():
    local_css()
    
    # Caricamento dell'immagine
    image_path = "Soggetto.png"
    profile_image = load_image(image_path)
    
    # Header con gestione condizionale dell'immagine
    if profile_image:
        image_html = f'<div class="profile-image-container"><img src="data:image/png;base64,{image_to_base64(profile_image)}" style="width: 150px; height: 150px; border-radius: 50%; border: 4px solid white;"></div>'
    else:
        image_html = '<div class="profile-image-container" style="width: 150px; height: 150px; border-radius: 50%; border: 4px solid white; background-color: #3b82f6; display: flex; align-items: center; justify-content: center; color: white; font-size: 48px;">ML</div>'
    
    st.markdown(f"""
    <div class="header-container">
        <div style="display: flex; align-items: center; gap: 2rem;">
            {image_html}
            <div>
                <h1 style="color: white; margin: 0;">Matheus Lima de Oliveira Sabino</h1>
                <h2 style="color: white; opacity: 0.9; margin: 10px 0;">Data Analyst Junior</h2>
                <div class="contact-info">
                    <span>📧 matheus.lima211266@gmail.com</span>
                    <span>📱 +39 392 157 5103</span>
                    <span>📍 Bologna</span>
                    <span>🎂 25/05/1998</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Aggiungi il pulsante per scaricare il CV
    cv_path = "curriculumvitae Matheus Lima.pdf"
    if os.path.exists(cv_path):
        st.markdown(
            get_binary_file_downloader_html(cv_path, 'Scarica CV'),
            unsafe_allow_html=True
        )
    
    # Tabs per la navigazione
    tabs = st.tabs(["🎯 Chi Sono", "💡 Competenze", "💼 Esperienze", "🎓 Formazione"])
    
    with tabs[0]:
        chi_sono_text = """
        Data Analyst con background tecnico.
        •Mi appassiona il mondo della data visualization e dello sviluppo di soluzioni analitiche, con particolare interesse per la programmazione e l'automazione dei processi.
        
        <b>▶</b>Mi contraddistingue la capacità di:
        •Analizzare e interpretare dataset complessi
        •Creare visualizzazioni efficaci per comunicare i risultati delle analisi
        •Trasformare i dati in insights strategici e actionable.
        """
        
        formatted_text = create_formatted_text(chi_sono_text)
        
        st.markdown(f"""
        <div class="custom-card">
            <h2>Chi Sono</h2>
            <div style="color: #4b5563;">
                {formatted_text}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Lingue
        st.markdown("<h3>Lingue</h3>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="custom-card" style="text-align: center;">
                <h4>Portoghese</h4>
                <p style="color: #3b82f6;">Madrelingua</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="custom-card" style="text-align: center;">
                <h4>Italiano</h4>
                <p style="color: #3b82f6;">Madrelingua</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown("""
            <div class="custom-card" style="text-align: center;">
                <h4>Inglese</h4>
                <p style="color: #3b82f6;">Orale: C1 (Avanzato), Scritto: B2 (Intermedio superiore)</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[1]:
        st.markdown("<h2>Competenze Tecniche</h2>", unsafe_allow_html=True)
        
        # Usa la nuova funzione per creare il grafico radar
        fig = create_skills_radar()
        st.plotly_chart(fig, use_container_width=True)
        
        # Dettaglio competenze con progress bar
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h3>Data Analysis</h3>", unsafe_allow_html=True)
            create_skill_progress("Python", 100)
            create_skill_progress("SQL", 70)
            create_skill_progress("Machine Learning", 90)
            
        with col2:
            st.markdown("<h3>Visualization</h3>", unsafe_allow_html=True)
            create_skill_progress("PowerBI", 60)
            create_skill_progress("Powerpoint", 90)
            create_skill_progress("Excel", 100)
    
    with tabs[2]:
        st.markdown("<h2>Esperienze Lavorative</h2>", unsafe_allow_html=True)
        
        create_timeline_item(
            "Risk Management Analyst",
            "giugno 2024-dicembre 2024",
            "CRIF",
            """<b>▶</b> Progettazione e implementazione end to end di un sistema antifrode innovativo per il leasing B2B:
            • Modello di scoring avanzato basato su KPI comportamentali
            • Integrazione con API e framework CRIF
            • Esposizione come servizio per istituti bancari e società finanziarie
            • Valutazione automatizzata del rischio frode nelle richieste di finanziamento

            <b>▶</b> Ottimizzazione delle strategie per il credito revolving consumer:
            • Implementazione di un sistema di monitoraggio continuo delle policy
            • Sviluppo di metriche personalizzate per l'analisi delle prestazioni
            • Bilanciamento ottimale tra gestione del rischio ed efficienza operativa
            • Identificazione e correzione degli errori di valutazione

            <b>▶</b> Results:
            • Incremento del 3% del tasso di approvazione mantenendo invariato il profilo di rischio complessivo
            """
        )

        create_timeline_item(
            "Data Analyst",
            "settembre 2023-gennaio 2024",
            "KPI6/Wellow",
            """<b>▶</b> Analisi Social Media & Web:
            • Utilizzo di Marketear e Odience per monitoraggio delle conversazioni online
            • Raccolta e analisi del sentiment su social media per diversi settori (tech, food&wine, politica)
            • Elaborazione di report sul sentiment degli utenti durante eventi specifici

            <b>▶</b> Reporting & Monitoraggio:
            • Creazione di report settimanali sull'andamento delle conversazioni online
            • Monitoraggio delle menzioni e del sentiment per brand specifici
            • Analisi delle tendenze di mercato nel settore vinicolo attraverso l'ascolto social

            <b>▶</b> Supporto all'analisi:
            • Utilizzo degli strumenti proprietari per l'estrazione dei dati
            • Organizzazione delle informazioni in report strutturati
            • Supporto nella presentazione dei risultati al team
            """
        )

        create_timeline_item(
            "Technical Support",
            "Agosto 2019 – Aprile 2023",
            "TONER INK JET DI PAOLO DE VITO & C. S.A.S.(IRIPARO)",
            """<b>▶</b> Riparazione e assistenza tecnica dispositivi:
            • Diagnosi e riparazione di smartphone e tablet (sostituzione display, batterie, connettori)
            • Interventi hardware su PC e notebook (upgrade RAM, sostituzione hard disk, pulizia)
            • Risoluzione problematiche software (ripristino sistemi operativi, backup dati, rimozione malware)
            • Sviluppo di soluzioni creative per riparazioni non standard

            <b>▶</b> Problem Solving & Gestione clientela:
            • Analisi sistematica dei problemi per identificare rapidamente le cause dei guasti
            • Accoglienza clienti e valutazione efficiente delle problematiche
            • Comunicazione chiara delle soluzioni tecniche ai clienti
            • Gestione efficace delle priorità nelle riparazioni multiple

            <b>▶</b> Attività di laboratorio:
            • Utilizzo di strumenti diagnostici per dispositivi mobili
            • Esecuzione accurata di test post-riparazione
            • Gestione organizzata del magazzino ricambi
            • Documentazione dettagliata degli interventi effettuati
            """
        )
        
        create_timeline_item(
            "Database management",
            "Febbraio 2019 – Agosto 2019",
            "COLORCLUB.IT S.R.L(PRINK)",
            """<b>▶</b> Gestione del database prodotti dell'e-commerce aziendale:
            • Data entry e aggiornamento dei codici articoli nel sistema gestionale
            • Verifica e correzione delle discrepanze tra giacenze fisiche e digitali
            • Monitoraggio degli upload dei prodotti sul sito web

            <b>▶</b> Gestione contenuti visivi:
            • Elaborazione base e modifica delle immagini dei prodotti
            • Caricamento e aggiornamento delle foto sul sito aziendale
            • Controllo qualità dei contenuti visuali prima della pubblicazione

            <b>▶</b> Attività di supporto:
            • Segnalazione e correzione di errori nel database prodotti
            • Manutenzione dell'accuratezza dei dati di magazzino
            """
        )
        
    with tabs[3]:
        st.markdown("""
        <div class="custom-card">
            <h2>Formazione</h2>
            <h3 style="color: #3b82f6;">IFTS "Tecnico per l'analisi e la visualizzazione dei dati"</h3>
            <p style="color: #6b7280;">Dicembre 2022 - Giugno 2023</p>
            <ul style="color: #4b5563;">
                <li>Sviluppo di un modello Machine Learning per fake news detection usando scikit-learn</li>
                <li>Implementazione di pipeline ETL per data cleaning e preprocessing</li>
                <li>Creazione di dashboard interattive con Power BI</li>
                <li>Progettazione e gestione database SQL per analytics</li>
                <li>Stack tecnologico: Python, SQL, Power BI, Git, scikit-learn, Excel</li>
            </ul>
            <div style="margin-top: 20px;">
                <span class="badge">Python</span>
                <span class="badge">SQL</span>
                <span class="badge">Power BI</span>
                <span class="badge">Git</span>
                <span class="badge">scikit-learn</span>
                <span class="badge">Excel</span>
                <span class="badge">Powerpoint</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()