import tkinter as tk
from tkinter import ttk


class ScrollableFrame(tk.Frame):

    """Frame construct which is scrollable. All widgets need to be placed within the 'instance.scrollable_frame' frame
    widget.
    """
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs, relief="groove", borderwidth=3)
        self.canvas = tk.Canvas(master=self)

        self.scrollable_frame = tk.Frame(master=self.canvas)
        self.scrollable_frame.bind("<Configure>",
                                   lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.scrollbar = tk.Scrollbar(master=self.scrollable_frame,
                                      orient="vertical",
                                      command=self.canvas.yview)

        self.canvas.create_window((0, 0),
                                  window=self.scrollable_frame,
                                  anchor="n")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side="right",
                            fill=tk.Y)


