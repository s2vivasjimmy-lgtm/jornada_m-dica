import streamlit as st

st.set_page_config(page_title="Contacto Rápido", page_icon="🔗")

# Estilo de los botones
st.markdown("""
<style>
.btn-link {
    display: block;
    width: 100%;
    padding: 20px;
    margin: 10px 0;
    text-align: center;
    background-color: #ffffff;
    color: #000000 !important;
    text-decoration: none;
    border-radius: 10px;
    font-weight: bold;
    font-size: 18px;
    border: 2px solid #00d2ff;
    transition: 0.3s;
}
.btn-link:hover { background-color: #00d2ff; color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

st.title("🔗 Acceso Directo")
st.write("Selecciona una vía de contacto o ubicación:")

# --- CONFIGURA TUS LINKS AQUÍ ---
link_maps = "https://maps.app.goo.gl/brQG1Z1gmYCVLPgKA"
link_telegram = "https://t.me/autoridadsaludLG"
link_whatsapp = "https://wa.me/584221927751"

# Botones
st.markdown(f'<a href="{link_maps}" target="_blank" class="btn-link">📍 UBICACIÓN EN MAPS</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{link_telegram}" target="_blank" class="btn-link">✈️ TELEGRAM</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{link_whatsapp}" target="_blank" class="btn-link">💬 WHATSAPP</a>', unsafe_allow_html=True)
