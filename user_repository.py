# user_repository.py
import streamlit as st
from supabase import create_client

class UserRepository:
    def __init__(self):
        # Usamos st.secrets para conectar de forma segura en Streamlit Cloud
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        self.supabase = create_client(url, key)

    def get_user_by_username(self, username: str) -> dict | None:
        response = self.supabase.table("users") \
            .select("*") \
            .eq("username", username) \
            .execute()
        
        if response.data:
            return response.data[0]
        return None

    def create_user(self, username: str, password: str, name: str) -> bool:
        try:
            self.supabase.table("users").insert({
                "username": username,
                "password": password,
                "name": name
            }).execute()
            return True
        except Exception:
            return False