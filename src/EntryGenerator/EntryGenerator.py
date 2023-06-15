from src.EntryGenerator.Application.Application import Application
from src.EntryGenerator.Password.Password import Password

from src.EntryGenerator.RawPasswordError.RawPasswordError import RawPasswordError


class EntryGenerator:

    encrypted_password: str
    is_encrypted: bool

    @staticmethod
    def create_application_password_pair_for(*, application_name: str, application_password: str) -> tuple[Application, Password]:
        encrypted_password, is_encrypted = EntryGenerator.encrypt_password(password=application_password)
        if is_encrypted:
            return Application(name=application_name), Password(password=encrypted_password)

        else:
            raise RawPasswordError("Password was not encrypted succesfully")

    @staticmethod
    def generate_key(*, password: str) -> str:
        pass

    @staticmethod
    def encrypt_password(*, password: str) -> tuple[str, bool]:

        return "", True

    @staticmethod
    def decrypt_password(*, password: Password) -> str:
        pass

    @staticmethod
    def get_password(application: Application) -> str:
        pass

    @staticmethod
    def store_password_to_database(*, application: Application, password: Password) -> None:
        pass
