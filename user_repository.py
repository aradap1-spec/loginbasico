# user_repository.py
import os
from supabase import create_client

class UserRepository:
    def __init__(self):
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_KEY")
        self.supabase = create_client(url, key)

    def get_user_by_username(self, username: str) -> dict | None:
        response = self.supabase.table("users") \
            .select("*") \
            .eq("username", username) \
            .execute()
        
        if response.data:
            return response.data[0]
        return None