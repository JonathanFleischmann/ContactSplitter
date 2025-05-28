import tkinter as tk

class CustomInfo:
    """
    Zeigt ein modales Info-Fenster mit Titel, Nachricht und OK-Button an.
    """

    def __init__(self, title: str, message: str):
        # Neues Toplevel-Fenster erstellen
        win = tk.Toplevel()
        win.title(title)
        win.resizable(False, False)
        # Nachricht anzeigen
        tk.Label(win, text=message, padx=20, pady=10).pack()
        # OK-Button zum Schließen
        tk.Button(
            win,
            text="OK",
            bg="#2196F3",
            fg="white",
            activebackground="#1976D2",
            activeforeground="white",
            command=win.destroy,
            width=10
        ).pack(pady=(0, 10))
        win.grab_set()  # macht das Fenster modal