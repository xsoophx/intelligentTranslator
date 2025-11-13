from tkinter import ttk

class MainWindow(ttk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        ttk.Button(self, text="Test", command=controller.do_something).pack()
        self.pack(fill="both", expand=True)
