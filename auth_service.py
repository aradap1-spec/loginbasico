# auth_service.py
from user_repository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def login(self, username: str, password: str) -> dict | None:
        if not username or not password:
            return None
            
        user = self.user_repo.get_user_by_username(username)
        
        if user and user["password"] == password:
            print(f"✅ Usuario '{username}' inició sesión correctamente")
            return {"username": username, "name": user["name"]}
            
        return None

    def register(self, username: str, password: str, name: str) -> bool:
        if not username or not password or not name:
            return False
        
        existing = self.user_repo.get_user_by_username(username)
        if existing:
            return False
        
        return self.user_repo.create_user(username, password, name)