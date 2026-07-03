import tkinter as tk
from tkinter import ttk
from tkinter import font as tk_fonts


from app.settings import STATIC_DIR


def init_fonts(app: tk.Tk):
    return {
        "main_font": tk_fonts.Font(family="Helvetica", size=12),
        "header_font": tk_fonts.Font(family="Helvetica", size=14, weight="bold")
    }
