from src.EntryGenerator.RawPasswordError.RawPasswordError import RawPasswordError


class Password:
    def __init__(self, *, password: str) -> None:
        self.password: str = None
        self.set_password(password=password)

    def set_password(self, password: str) -> None:
        decrypted_password: str = self.decrypt_password(password=password)
        self.password = decrypted_password

    def get_password(self) -> str:
        return self.encrypt_password()
