from src.Database.DatabaseManager import DatabaseManager
from src.EntryGenerator.Application.Application import Application
from src.EntryGenerator.EntryGenerator import EntryGenerator
from src.EntryGenerator.Password.Password import Password
from src.User.User import User


class EntryManager:

    entry_generator: EntryGenerator
    database_manager: DatabaseManager
    unsaved_entries: dict[Application | User, Password]

    def __init__(self) -> None:
        self.entry_generator = None
        self.database_manager = None

    def set_entry_manager_to(self, entry_generator: EntryGenerator) -> None:
        self.entry_generator = entry_generator

    def set_database_manager_to(self, database_manager: DatabaseManager) -> None:
        self.database_manager = database_manager

    def store_entries_to_database(self) -> None:
        pass



#TODO implement adapter methods for entry generator and database manager.
# this class is responsible for controling the whole managing process for data an database