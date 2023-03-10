import sqlite3
from pathlib import Path


class DatabaseManager:

    def __init__(self, database_name: str, table_name: str):

        database_path: Path = Path(database_name)
        if database_path.suffix == ".db":
            pass
        else:
            database_name = f"{database_name}.db"

        self.table_name: str = table_name
        self.database_connection: sqlite3.Connection = sqlite3.Connection(database=database_name)
        self.initialize_database_table()

    def initialize_database_table(self) -> None:

        """
        Creates the database table where all information will be stored in.
        :return: None
        """

        cursor: sqlite3.Cursor = self.database_connection.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.table_name}
                        (APPLICATION_NAME VARCHAR NOT NULL,
                        USERNAME VARCHAR NOT NULL,
                        PASSWORD VARCHAR,
                        PRIMARY KEY (APPLICATION_NAME, USERNAME)
                        )""")

        self.database_connection.commit()

    def update_password_for_application(self, application_name: str, username: str, new_password: str) -> None:

        """
        Database Method to change the password for an existing entry within the database.
        :param application_name: The name of the applciation the password should be changed for
        :param username: The name of the user the password should be changed for
        :param new_password: The new password which should be stored within the database
        :return: None
        """

        cursor: sqlite3.Cursor = self.database_connection.cursor()

        cursor.execute(f"""UPDATE {self.table_name} 
                           set PASSWORD='{new_password}'
                           where APPLICATION_NAME = '{application_name}'
                           and USERNAME = '{username}'""")

        self.database_connection.commit()

    def update_username_for_application(self, application_name: str, username: str, new_username: str) -> None:

        """
        Database Method to change the password for an existing entry within the database.
        :param application_name: The name of the application the password should be changed for. Database key
        :param username: The name of the user the password should be changed for. Database key
        :param new_username: The new username which should be stored within the database
        :return: None
        """

        cursor: sqlite3.Cursor = self.database_connection.cursor()

        cursor.execute(f"""UPDATE {self.table_name} 
                           set USERNAME='{new_username}' 
                           where APPLICATION_NAME = '{application_name}' 
                           and USERNAME = '{username}'""")

        self.database_connection.commit()

    def insert_value_for_application(self, application_name: str, username: str, password: str) -> None:

        """
        Insert a new value into the database.
        :param application_name: Application name the information will be stored for. Primary key
        :param username: Name of the user login name into the application. Primary key
        :param password: Password to log in with username into application.
        :return: None
        """

        if not any([application_name, username, password]):
            return None

        cursor: sqlite3.Cursor = self.database_connection.cursor()
        cursor.execute(f"""INSERT INTO {self.table_name} 
                           (APPLICATION_NAME, USERNAME, PASSWORD) 
                            VALUES ('{application_name}', '{username}','{password}')""")
        self.database_connection.commit()

    def get_value_for_application(self, application_name: str, *, username: str = None) -> list[tuple[str]]:

        """
        Get information from database for a specific application. Username is optional.
        :param application_name: Name of the application information are desired for
        :param username: optional, if inserted only information concerning this specific user - application combination
        will be fetched.
        :return: A list of tuples, containing the (application, username, password)
        """

        cursor: sqlite3.Cursor = self.database_connection.cursor()

        if username is None:
            data = cursor.execute(f"""SELECT * 
                                    FROM {self.table_name} 
                                    where APPLICATION_NAME = '{application_name}'""").fetchall()
        else:
            data=cursor.execute(f"""SELECT * 
                                FROM {self.table_name} 
                                where APPLICATION_NAME = '{application_name}' 
                                and USERNAME = '{username}'""").fetchall()
        return data

    def get_all_database_data(self) -> list[tuple[str]]:

        """
        Returns the total amount of database entries.
        :return: A list of tuples, containing the (application, username, password) for all entries in the database.
        """

        cursor: sqlite3.Cursor = self.database_connection.cursor()
        data = cursor.execute(f"""SELECT * 
                                    FROM {self.table_name}""").fetchall()

        return data

    def delete_user_for_all_applications(self, username: str) -> None:

        """
        Deletes the specific user from all entries within the database.
        :param username: name of the user to be deleted
        :return: None
        """

        cursor: sqlite3.Cursor = self.database_connection.cursor()
        cursor.execute(f"""DELETE FROM {self.table_name} 
                           WHERE USERNAME like '%{username}%'""")
        self.database_connection.commit()

    def delete_entry_for_application(self, application_name: str, username: str) -> None:

        """
        Deletes the specific user for a specific application.
        :param application_name: Specific application the user should be deleted for
        :param username: name of the user to be deleted
        :return: None
        """

        cursor: sqlite3.Cursor = self.database_connection.cursor()

        cursor.execute(f"""DELETE FROM {self.table_name} 
                           WHERE APPLICATION_NAME = '{application_name}' 
                           AND USERNAME = '{username}'""")

        self.database_connection.commit()

