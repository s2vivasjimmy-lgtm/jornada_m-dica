import streamlit as st

st.set_page_config(
    page_title="Centro de Comando | Enlaces Directos", 
    page_icon="⚡",
    layout="centered"
)

# --- ESTILOS CSS PROFESIONALES (TEMA OSCURO / NEGRO PURO) ---
st.markdown("""
<style>
/* Fondo general de la aplicación en negro absoluto */
.stApp {
    background-color: #050505 !important;
    color: #e2e8f0;
}

/* Ocultar elementos predeterminados de Streamlit para limpieza visual */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Contenedor principal estilo tarjeta ejecutiva */
.main-card {
    background: linear-gradient(145deg, #121214, #1a1a1e);
    border: 1px solid #27272a;
    padding: 40px 30px;
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.7);
    text-align: center;
    margin-top: 30px;
}

/* Títulos y subtítulos */
.title-text {
    font-size: 28px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: 1px;
    margin-bottom: 8px;
    text-transform: uppercase;
}

.subtitle-text {
    font-size: 14px;
    color: #94a3b8;
    margin-bottom: 35px;
    font-weight: 400;
}

/* Botones de acción de alta gama */
.btn-command {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    width: 100%;
    padding: 16px 20px;
    margin: 14px 0;
    background-color: #18181b;
    color: #ffffff !important;
    text-decoration: none;
    border-radius: 12px;
    font-weight: 600;
    font-size: 15px;
    border: 1px solid #3f3f46;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
}

/* Efectos hover profesionales (Cambio sutil con brillo azulado/metálico) */
.btn-command:hover {
    background-color: #27272a;
    border-color: #00d2ff;
    color: #00d2ff !important;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0, 210, 255, 0.15);
}

.btn-icon {
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# --- CONFIGURA TUS LINKS AQUÍ ---
link_maps = "https://maps.app.goo.gl/brQG1Z1gmYCVLPgKA"
link_telegram = "https://t.me/autoridadsaludLG"
link_whatsapp = "https://wa.me/584221927751"

# --- INTERFAZ VISUAL ---
st.markdown("""
<div class="main-card">
    <div class="title-text">Puesto de Comando</div>
    <div class="subtitle-text">Canales oficiales de comunicación y geolocalización</div>
""", unsafe_allow_html=True)

st.markdown(f'<a href="{link_maps}" target="_blank" class="btn-command"><span class="btn-icon">📍</span> UBICACIÓN EN GOOGLE MAPS</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{link_telegram}" target="_blank" class="btn-command"><span class="btn-icon">✈️</span> CANAL DE TELEGRAM</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{link_whatsapp}" target="_blank" class="btn-command"><span class="btn-icon">💬</span> WHATSAPP</a>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
