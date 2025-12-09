class AuthService:
    def login(self, username, password):
        if username == "elek" and password == "alma":
            return "TOKEN1234"
        raise ValueError("Nem jó a user vagy a pw.")
