import tkinter as tk

class CustomAskYesNo:
    def __init__(self, title: str, message: str):
        self.result = None
        self.win = tk.Toplevel()
        self.win.title(title)
        self.win.resizable(False, False)
        tk.Label(self.win, text=message, padx=20, pady=10).pack()
        button_frame = tk.Frame(self.win)
        button_frame.pack(pady=(0, 10))
        tk.Button(button_frame, text="Ja", bg = "#4CAF50", fg = "white", activebackground = "#388E3C", activeforeground = "white", width=10, command=self.yes).pack(side="left", padx=5)
        tk.Button(button_frame, text="Nein", bg = "#F44336", fg = "white", activebackground = "#D32F2F", activeforeground = "white", width=10, command=self.no).pack(side="left", padx=5)
        self.win.grab_set()  # macht das Fenster modal
        self.win.wait_window()  # wartet, bis das Fenster geschlossen wird

    def yes(self):
        self.result = True
        self.win.destroy()

    def no(self):
        self.result = False
        self.win.destroy()