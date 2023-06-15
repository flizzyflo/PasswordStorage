

class User:

    def __init__(self, *, name: str, master_password: str) -> None:
        self.name = name
        self.master_password = master_password

