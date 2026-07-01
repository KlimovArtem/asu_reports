from tkinter import *
from tkinter.ttk import * 

from app.domain.models import FormData, RequestData
from app.presentation.views import SignalsListView

class App(Tk):
    def __init__(self):
        super().__init__()
        Style().configure(".",  font="helvetica 14", foreground="#262626", background="#fbfbfb")
        Style().configure("ReportApp.TEntry", padding=(3,2), borderwidth=5, bordercolor="blue")

        self.title = "Отчёты АСУ"
        self.resizable(False, False)
        self.minsize(400, 1)
               
        view = SignalsListView(self, padding=15)
        view.pack(fill="both", expand=True)
        view.columnconfigure(index=1, weight=1)


if __name__ == "__main__":
    app = App()
    style = Style(app)
    style.configure("TEntry", padding=3, borderwidth=5, bordercolor="blue")
    app.mainloop()