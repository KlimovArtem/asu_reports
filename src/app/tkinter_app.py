from tkinter import *
from tkinter.ttk import * 

from app.presentation.views import SignalsListView
from app.presentation.styles import init_fonts


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title = "Отчёты АСУ"
        self.resizable(False, False)
        self.minsize(400, 1)
               
        view = SignalsListView(self, padding=15)
        view.pack(fill="both", expand=True)
        view.columnconfigure(index=1, weight=1)


if __name__ == "__main__":
    app = App()
    style = Style(app)
    style.theme_use('clam')
    fonts = init_fonts(app)

    style.configure(".",  font=fonts.get("main_font"), foreground="#262626", background="#fbfbfb")
    style.configure("Header.TLabel", font=fonts.get("header_font"))
    style.configure("ReportApp.TEntry", padding=(3, 5), bordercolor="#aaaaaa")
    style.map('ReportApp.TEntry', lightcolor=[('focus', '#A5A5A5')])
    style.configure('ReportApp.TSpinbox', padding=(3, 5), arrowsize=16, arrowcolor="#262626")
    style.map('ReportApp.TSpinbox', lightcolor=[('focus', '#A5A5A5')])
    style.configure('ReportApp.TCombobox', padding=(3, 5), arrowsize=16, arrowcolor='#262626')
    style.map('ReportApp.TCombobox', lightcolor=[('focus', '#A5A5A5')])
    style.configure("ReportApp.TButton", font=fonts.get("main_font"), padding=5)
    app.mainloop()