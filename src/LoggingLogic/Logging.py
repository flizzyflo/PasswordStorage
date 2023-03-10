from src.Database.DatabaseManager import DatabaseManager
from src.Settings.Settings import DATABASE_COLUMNS


class PasswordLogger:

    def __init__(self, database_manager: DatabaseManager) -> None:
        self.database_manager = database_manager

    def update_password(self, application_name: str, username: str, new_password: str) -> None:

        """
        Method to access database and change password stored on database-level.
        :param application_name: Name of the application you want to change the password for. Key value in DB-Table
        :param username: Username you want to change the password for. Key value in DB-Table
        :param new_password: New password value to be stored in database.
        :return: None
        """

        self.database_manager.update_password_for_application(application_name=application_name,
                                                              username=username,
                                                              new_password=new_password)

    def update_username(self, application_name: str, username: str, new_username: str) -> None:

        """
        Method to access database and change password stored on database-level.
        :param application_name: Name of the application you want to change the password for. Key value in DB-Table
        :param username: Username you want to change the username for. Key value in DB-Table.
        :param new_username: new Username to be set within database. Changes the key for this entry!
        :return: None
        """

        self.database_manager.update_username_for_application(application_name=application_name,
                                                              username=username,
                                                              new_username=new_username)

    def password_is_valid(self, password: str) -> bool:
        ...

    def add_item_to_database(self, application_name: str, username: str, password: str) -> None:

        """
        Adds a new entry into the database.
        :param application_name: Application you want to store the data for
        :param username: username within the application
        :param password: password to be stored
        :return: None
        """

        self.database_manager.insert_value_for_application(application_name=application_name,
                                                           username=username,
                                                           password=password)

    def delete_item_from_database(self, username: str, *, application_name: str = None,  for_all_applications: bool = False) -> None:

        """
        General function to either delete a single entry (user per application) or all entries for a specific username for all applications
        within the database.
        :param application_name: application to delete the entry/entries for
        :param username: username where the entry/entries should be deleted for
        :param for_all_applications: boolean value, if true delete all entries for the specific user passed in
        :return: None
        """

        if for_all_applications:
            self.database_manager.delete_user_for_all_applications(username=username)

        else:
            self.database_manager.delete_entry_for_application(application_name=application_name,
                                                               username=username)

    def retrieve_information_for_application(self, application_name: str, *, username: str = None) -> dict[str, list[dict[str, str]]]:

        """
        Fetches and returns information for a specific application - user combination
        :param application_name: specific application you want information for
        :param username: specific user you want information for. If username is 'None' all information for the specific
        application are fetched.
        :return: Dictionary with application as key and information as dictionary for each single
        individual, containing the username and password data.
        Example returnvalue: {Google: [{Username: Peter, Password: Secr3tP4s5w0rd}, {Username: Anna, ...},...],
        Facebook: [{key:value}, {key:value}, ...], ...}
        """

        data = self.database_manager.get_value_for_application(application_name=application_name,
                                                               username=username)

        return self.__reformat_database_fetch(data=data)

    def retrieve_all_information_from_database(self) -> dict[str, list[dict[str, str]]]:

        """
        Fetches and returns total information from the complete database.
        :return: Dictionary with application as key and information as dictionary for each single
        individual, containing the username and password data.
        Example returnvalue: {Google: [{Username: Peter, Password: Secr3tP4s5w0rd}, {Username: Anna, ...},...],
        Facebook: [{key:value}, {key:value}, ...], ...}
        """

        data = self.database_manager.get_all_database_data()

        return self.__reformat_database_fetch(data=data)

    @staticmethod
    def __reformat_database_fetch(data: list[tuple[str]]) -> dict[str, list[dict[str, str]]]:

        """
        Reformats the fetched data from the database itself into a dictionary format
        :param data: fetched data from database as list of tuples
        :return: dictionary with application as keys and username - passwords as key-values.
        """

        columns = DATABASE_COLUMNS
        result: dict[str, list[dict[str, str]]] = dict()  # {Application: [{Username: Peter, Password: test},...], ...}

        for tup in data:  # data = [ (str, str, str), ... ]
            application_name = tup[0]
            user_data = dict()

            if application_name not in result.keys():
                result[application_name] = list()

            for idx, column in enumerate(columns[1:], 1):
                user_data[column] = tup[idx]

            result[application_name].append(user_data)

        return result
