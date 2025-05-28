import tkinter as tk

class Frame:
    """
    Wrapper für ein Tkinter-Frame oder LabelFrame mit optionalem Titel und Rand.
    """

    def __init__(self, parent, text=None, small_margin=False):
        self.parent = parent
        self.text = text
        # LabelFrame, wenn ein Text angegeben ist, sonst normales Frame
        if text:
            self.frame = tk.LabelFrame(parent, text=text)
        else:
            self.frame = tk.Frame(parent)
        # Rand je nach Option
        margin = 2 if small_margin else 10
        self.frame.pack(padx=margin, pady=margin)

    def clear(self):
        """Entfernt alle enthaltenen Widgets aus dem Frame."""
        for widget in self.frame.winfo_children():
            widget.destroy()