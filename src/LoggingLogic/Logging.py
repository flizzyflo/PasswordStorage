from src.Database.DatabaseManager import DatabaseManager
from src.Settings.Settings import DATABASE_COLUMNS


class PasswordLogger:

    def __init__(self, database_manager: DatabaseManager) -> None:
        self.database_manager = database_manager

    def update_password(self, application_name: str, username: str, new_password: str) -> None:
        self.database_manager.update_password_for_application(application_name=application_name,
                                                              username=username,
                                                              password=new_password)

    def update_username(self, application_name: str, new_username: str, password: str) -> None:
        self.database_manager.update_username_for_application(application_name=application_name,
                                                              username=new_username,
                                                              password=password)

    def password_is_valid(self, password: str) -> bool:
        ...

    def add_item_to_database(self, application_name: str, username: str, password: str) -> None:
        self.database_manager.insert_value_for_application(application_name=application_name,
                                                           username=username,
                                                           password=password)

    def delete_item_from_database(self, application_name: str, username: str, for_all_applications: bool) -> None:
        if for_all_applications:
            self.database_manager.delete_user_for_all_applications(application_name=application_name,
                                                                   username=username)

        else:
            self.database_manager.delete_entry_for_application(application_name=application_name,
                                                               username=username)

    def retrieve_information_for_entry(self, application_name: str, username: str = None) -> dict[str, str]:
        data = self.database_manager.get_value_for_application(application_name=application_name,
                                                               username=username)

        return self.reformat_database_fetch(data=data)

    def retrieve_all_information_from_database(self) -> list[tuple[str]]:
        data = self.database_manager.get_all_database_data()

        return self.reformat_database_fetch(data=data)

    @staticmethod
    def reformat_database_fetch(data: list[tuple[str]]) -> dict[str, list[list[str]]]:
        columns = DATABASE_COLUMNS
        result: dict[str, str] = dict()

        for tup in data:  # data = [ (str, str, str), ... ]
            application_name = tup[0]
            user_data = list()

            if application_name not in result.keys():
                result[application_name] = list()

            for idx, column in enumerate(columns[1:], 1):
                user_data.append({column: tup[idx]})

            result[application_name].append(user_data)

        return result
