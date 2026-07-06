from tkinter import *
from tkinter.ttk import * 

from app.presentation.views import ChoosenReportTypeView, SignalsListView
from app.presentation.styles import init_fonts


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title = "Отчёты АСУ"
        self.resizable(False, False)
        self.minsize(400, 1)
        self.view = None
        self.views = {
            "/": ChoosenReportTypeView(self),
            "Перечень сигналов": SignalsListView(self)
        }

        self.view = self.views["/"]
        self.view.grid(row=1, column=1, sticky ="nsew")
        self.columnconfigure(index=1, weight=1)
        self.rowconfigure(index=1, weight=1)

        self.view.columnconfigure(index=1, weight=1)

    def show_view(self, url: str):
        new_view = self.views.get(url, None)
        if new_view:
            self.view.grid_forget()
            self.view = new_view
            self.view.grid(row=1, column=1, sticky ="nsew")
            self.view.columnconfigure(index=1, weight=1)
        else:
            pass



if __name__ == "__main__":
    app = App()
    style = Style(app)
    style.theme_use('clam')
    fonts = init_fonts(app)

    style.configure(".",  font=fonts.get("main_font"), foreground="#262626", background="#fbfbfb")
    style.configure("Header.TLabel", font=fonts.get("header_font"))
    style.configure("ReportApp.TEntry", padding=(3, 5), bordercolor="#aaaaaa")
    style.map('ReportApp.TEntry', lightcolor=[('focus', '#0080fe')])
    style.configure('ReportApp.TSpinbox', padding=(3, 5), arrowsize=16, arrowcolor="#262626")
    style.map('ReportApp.TSpinbox', lightcolor=[('focus', '#0080fe')])
    style.configure('ReportApp.TCombobox', padding=(3, 5), arrowsize=16, arrowcolor='#262626')
    style.map('ReportApp.TCombobox', lightcolor=[('focus', '#0080fe')])
    app.option_add("*TCombobox*Listbox*Font", fonts.get("main_font"))
    style.configure("ReportApp.TButton", font=fonts.get("main_font"), padding=5, foreground="#fbfbfb", background="#0080fe")
    style.map('ReportApp.TButton', background=[('active', '#0f52ba')])
    app.mainloop()