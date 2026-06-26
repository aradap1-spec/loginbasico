# auth_service.py
from user_repository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()

    def login(self, username: str, password: str) -> dict | None:
        """
        Verifica las credenciales.
        Devuelve los datos del usuario si son correctos, o None si falla.
        """
        # Validaciones de seguridad básicas antes de ir a la "BD"
        if not username or not password:
            return None
            
        user = self.user_repo.get_user_by_username(username)
        
        if user and user["password"] == password:
            # Retornamos la información del usuario (menos el password por seguridad)
            return {"username": username, "name": user["name"]}
            
        return None