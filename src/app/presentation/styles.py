import tkinter as tk
from tkinter import font as tk_fonts



def init_fonts(app: tk.Tk):
    return {
        "main_font": tk_fonts.Font(family="Helvetica", size=12),
        "header_font": tk_fonts.Font(family="Helvetica", size=14, weight="bold")
    }
