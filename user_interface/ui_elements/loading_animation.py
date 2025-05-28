import tkinter as tk
from user_interface.ui_elements.frame import Frame

class LoadingAnimation:
    def __init__(self, parent: Frame):
        self.container = parent.frame
        self.running = False
        self.loading_text_output = None
        self.phase = 0
        self.dots_number = 0

    def start(self):
        if self.running:
            return
        self.running = True
        if not self.loading_text_output:
            self.loading_text_output = tk.Label(self.container, text="Laden", width=52, anchor="w")
            self.loading_text_output.pack(pady=0)
        self.phase = 0
        self.dots_number = 0
        self._animate()

    def stop(self):
        self.running = False
        if self.loading_text_output:
            self.loading_text_output.destroy()
            self.loading_text_output = None

    def _animate(self):
        if not self.running:
            return
        max_dots = 4
        text = "Laden" + "." * self.dots_number
        self.loading_text_output.config(text=text)
        if self.phase == 0:
            if self.dots_number < max_dots:
                self.dots_number += 1
            else:
                self.phase = 1
        elif self.phase == 1:
            if self.dots_number > 0:
                self.dots_number -= 1
            else:
                self.phase = 0
        self.loading_text_output.after(100, self._animate)