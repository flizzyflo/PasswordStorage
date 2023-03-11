from src.Settings.Settings import DATABASE_NAME, DATABASE_TABLE_NAME
from src.Database.DatabaseManager import DatabaseManager
from src.LoggingLogic.Logging import PasswordLogger
from src.UserInterface.ApplicationFrame import ApplicationFrame
from src.UserInterface.ContentFrame import ContentFrame
import tkinter as tk


if __name__ == '__main__':

    d = DatabaseManager(database_name=DATABASE_NAME,
                        table_name=DATABASE_TABLE_NAME)

    logger = PasswordLogger(database_manager=d)
    print(logger.retrieve_information_for_application(application_name="Google_1"))

    r = tk.Tk()
    contents = ContentFrame(master=r)
    applications = ApplicationFrame(master=r)
    contents.grid(row=0,
                  column=0,
                  sticky="NSEW")
    applications.grid(row=0,
                      column=1,
                      sticky="NSEW")
    for i in range(30):
        if i % 2 == 0:
            tk.Label(master=applications.scrollable_frame, text=f"{i}. app").pack()
        else:
            tk.Label(master=contents.scrollable_frame, text=f"{i}. content").pack()

    r.mainloop()