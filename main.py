from src.Settings.Settings import DATABASE_NAME, DATABASE_TABLE_NAME
from src.Database.DatabaseManager import DatabaseManager
from src.LoggingLogic.Logging import PasswordLogger


if __name__ == '__main__':

    d = DatabaseManager(database_name=DATABASE_NAME,
                        table_name=DATABASE_TABLE_NAME)

    logger = PasswordLogger(d)

