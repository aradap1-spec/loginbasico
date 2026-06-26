# pages/register.py
import streamlit as st
from auth_service import AuthService

st.set_page_config(page_title="Crear Cuenta", page_icon="✍️")

if "auth_service" not in st.session_state:
    st.session_state.auth_service = AuthService()

st.subheader("✍️ Crear Cuenta")

with st.form(key="register_form"):
    new_username = st.text_input("Usuario").strip()
    new_name = st.text_input("Nombre completo").strip()
    new_password = st.text_input("Contraseña", type="password")
    new_password_confirm = st.text_input("Confirmar contraseña", type="password")
    register_submit = st.form_submit_button("Crear cuenta")

if register_submit:
    if new_password != new_password_confirm:
        st.error("Las contraseñas no coinciden")
    else:
        success = st.session_state.auth_service.register(new_username, new_password, new_name)
        if success:
            st.success("Cuenta creada correctamente")
            st.markdown("[🔐 ¿Ya tienes cuenta? Inicia sesión](./appy)")
        else:
            st.error("El usuario ya existe o hubo un error")

st.divider()
st.markdown("[🔐 ¿Ya tienes cuenta? Inicia sesión](./appy)")