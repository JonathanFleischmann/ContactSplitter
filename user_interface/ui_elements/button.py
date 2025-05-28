import tkinter as tk
from user_interface.ui_elements.frame import Frame

class Button:
    """
    Wrapper-Klasse für einen farbigen Tkinter-Button mit verschiedenen Farbvarianten.
    """

    def __init__(self, parent: Frame, text, callback_method, in_one_row=False, slim=False):
        # Button-Größe je nach 'slim'-Option
        self.length = 10 if slim else 22
        self.parent = parent
        self.text = text
        self.callback_method = callback_method
        self.in_one_row = in_one_row

    def green(self):
        """Erstellt einen grünen Button."""
        self._set_colors("#4CAF50", "white", "#388E3C", "white")
        return self.render_button()
    
    def blue(self):
        """Erstellt einen blauen Button."""
        self._set_colors("#2196F3", "white", "#1976D2", "white")
        return self.render_button()
    
    def purple(self):
        """Erstellt einen lilafarbenen Button."""
        self._set_colors("#7C4CAF", "#FFFFFF", "#4E138D", "#FFFFFF")
        return self.render_button()
    
    def red(self):
        """Erstellt einen roten Button."""
        self._set_colors("#F44336", "white", "#D32F2F", "white")
        return self.render_button()
    
    def orange(self):
        """Erstellt einen orangenen Button."""
        self._set_colors("#FF9800", "black", "#F57C00", "black")
        return self.render_button()
    
    def _set_colors(self, bg, fg, active_bg, active_fg):
        """Setzt die Farben für den Button."""
        self.bg = bg
        self.fg = fg
        self.active_bg = active_bg
        self.active_fg = active_fg

    def render_button(self):
        """Erstellt und platziert den Button im UI."""
        button = tk.Button(
            self.parent.frame,
            text=self.text,
            bg=self.bg,
            fg=self.fg,
            activebackground=self.active_bg,
            activeforeground=self.active_fg,
            command=self.callback_method,
            width=self.length
        )
        # Button-Anordnung je nach Option
        if self.in_one_row:
            button.pack(side=tk.LEFT, padx=5, pady=5)
        else:
            button.pack(padx=5, pady=5)
        return button