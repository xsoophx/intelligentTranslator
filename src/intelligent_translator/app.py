import tkinter as tk
from ui.main_window import MainWindow
from logic.controller import Controller

def main():
    root = tk.Tk()
    root.title("Intelligent Translator")
    root.geometry("300x150")
    root.lift()
    root.attributes('-topmost', True)

    controller = Controller()
    MainWindow(root, controller)

    root.mainloop()

if __name__ == "__main__":
    main()
