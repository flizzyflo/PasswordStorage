import sqlite3
from pathlib import Path


class DatabaseManager:

    def __init__(self, database_name: str, table_name: str):

        database_path: Path = Path(database_name)
        if database_path.suffix == ".db":
            pass
        else:
            database_name = f"{database_name}.db"

        self.table_name: str = None
        self.database_connection: sqlite3.Connection = sqlite3.Connection(database=database_name)
        self.initialize_database_table(table_name=table_name)

    def initialize_database_table(self, table_name: str) -> None:
        cursor: sqlite3.Cursor = self.database_connection.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}
                        (APPLICATION_NAME VARCHAR NOT NULL,
                        USERNAME VARCHAR NOT NULL,
                        PASSWORD VARCHAR,
                        PRIMARY KEY (APPLICATION_NAME, USERNAME)
                        )""")

        self.table_name: str = table_name
        self.database_connection.commit()

    def update_password_for_application(self, application_name: str, username: str, password: str) -> None:
        cursor: sqlite3.Cursor = self.database_connection.cursor()

        cursor.execute(f"""UPDATE {self.table_name} 
                           set PASSWORD='{password}'
                           where APPLICATION_NAME = '{application_name}'
                           and USERNAME = '{username}'""")

        self.database_connection.commit()

    def update_username_for_application(self, application_name: str, username: str, new_username: str) -> None:
        cursor: sqlite3.Cursor = self.database_connection.cursor()

        cursor.execute(f"""UPDATE {self.table_name} 
                           set USERNAME='{new_username}' 
                           where APPLICATION_NAME = '{application_name}' 
                           and USERNAME = '{username}'""")

        self.database_connection.commit()

    def insert_value_for_application(self, application_name: str, username: str, password: str) -> None:

        if not any([application_name, username, password]):
            return None

        cursor: sqlite3.Cursor = self.database_connection.cursor()
        cursor.execute(f"""INSERT INTO {self.table_name} 
                           (APPLICATION_NAME, USERNAME, PASSWORD) 
                            VALUES ('{application_name}', '{username}','{password}')""")
        self.database_connection.commit()

    def get_value_for_application(self, application_name: str, username: str = None) -> list[tuple[str]]:
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
        cursor: sqlite3.Cursor = self.database_connection.cursor()
        data = cursor.execute(f"""SELECT * 
                                    FROM {self.table_name}""").fetchall()

        return data

    def delete_user_for_all_applications(self, username: str) -> None:
        cursor: sqlite3.Cursor = self.database_connection.cursor()
        cursor.execute(f"""DELETE FROM {self.table_name} 
                           WHERE USERNAME like '%{username}%'""")
        self.database_connection.commit()

    def delete_entry_for_application(self, application_name: str, username: str) -> None:
        cursor: sqlite3.Cursor = self.database_connection.cursor()

        cursor.execute(f"""DELETE FROM {self.table_name} 
                           WHERE APPLICATION_NAME = '{application_name}' 
                           AND USERNAME = '{username}'""")

        self.database_connection.commit()

