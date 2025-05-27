import tkinter as tk

class CustomInfo():
    def __init__(self, title: str, message: str):
        win = tk.Toplevel()
        win.title(title)
        win.resizable(False, False)
        tk.Label(win, text=message, padx=20, pady=10).pack()
        tk.Button(win, text="OK", bg = "#2196F3", fg = "white", activebackground = "#1976D2", activeforeground = "white", command=win.destroy, width=10).pack(pady=(0,10))
        win.grab_set()  # macht das Fenster modal
    