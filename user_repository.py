# user_repository.py

class UserRepository:
    def __init__(self):
        # Simulación de una base de datos de usuarios (En producción, las contraseñas estarían hasheadas)
        self._database = {
            "admin": {"password": "12345", "name": "Admi"},
            "user1": {"password": "securepass", "name": "Juan"}
        }

    def get_user_by_username(self, username: str) -> dict | None:
        """Busca un usuario en la 'base de datos'. Devuelve el usuario o None."""
        return self._database.get(username, None)