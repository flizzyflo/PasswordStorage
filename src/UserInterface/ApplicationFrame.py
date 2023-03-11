import tkinter as tk

from src.UserInterface.ScrollableFrame import ScrollableFrame


class ApplicationFrame(ScrollableFrame):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)