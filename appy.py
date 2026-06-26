# appy.py
import streamlit as st
from auth_service import AuthService

st.set_page_config(page_title="Login Arquitectura Formal", page_icon="🔐")

if "auth_service" not in st.session_state:
    st.session_state.auth_service = AuthService()

if "user_info" not in st.session_state:
    st.session_state.user_info = None

# --- VISTA: LOGIN ---
if st.session_state.user_info is None:
    st.subheader("🔐 Iniciar Sesión")
    
    with st.form(key="login_form"):
        username = st.text_input("Usuario").strip()
        password = st.text_input("Contraseña", type="password")
        submit = st.form_submit_button("Iniciar Sesión")
        
    if submit:
        user_data = st.session_state.auth_service.login(username, password)
        
        if user_data:
            st.session_state.user_info = user_data
            st.success(f"Bienvenido {user_data['name']}")
            st.rerun()
        else:
            st.error("Credenciales inválidas. Intente de nuevo.")

    st.divider()
    if st.button("¿No tienes cuenta? Regístrate aquí"):
     st.switch_page("pages/register.py")

# --- VISTA: ÁREA PROTEGIDA ---
else:
    st.title(f"Dashboard de {st.session_state.user_info['name']}")
    st.write("Estás viendo información confidencial protegida por la arquitectura.")
    
    if st.button("Cerrar Sesión"):
        st.session_state.user_info = None
        st.rerun()