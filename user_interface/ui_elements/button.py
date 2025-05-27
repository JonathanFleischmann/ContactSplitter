import tkinter as tk
from user_interface.ui_elements.frame import Frame

class Button:
    def __init__(self, parent: Frame, text, callback_method, in_one_row=False, slim=False):
        if slim:
            self.length = 10
        else:
            self.length = 22
        self.parent = parent
        self.text = text
        self.callback_method = callback_method
        self.in_one_row = in_one_row

    def green(self):
        self.bg = "#4CAF50"
        self.fg = "white"
        self.active_bg = "#388E3C"
        self.active_fg = "white"
        return self.render_button()
    
    def blue(self):
        self.bg = "#2196F3"
        self.fg = "white"
        self.active_bg = "#1976D2"
        self.active_fg = "white"
        return self.render_button()
    
    def purple(self):
        self.bg = "#7C4CAF"
        self.fg = "#FFFFFF"
        self.active_bg = "#4E138D"
        self.active_fg = "#FFFFFF"
        return self.render_button()
    
    def red(self):
        self.bg = "#F44336"
        self.fg = "white"
        self.active_bg = "#D32F2F"
        self.active_fg = "white"
        return self.render_button()
    
    def orange(self):
        self.bg = "#FF9800"
        self.fg = "black"
        self.active_bg = "#F57C00"
        self.active_fg = "black"
        return self.render_button()
    
    def render_button(self):
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
        if self.in_one_row:
            button.pack(side=tk.LEFT, padx=5, pady=5)
        else:
            button.pack(padx=5, pady=5)
        return button