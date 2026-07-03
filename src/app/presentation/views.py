from tkinter import *
from tkinter.ttk import *

from app.presentation.styles import init_fonts
from app.presentation.serializers import SignalsListSubdataSerializer


class SignalsListView(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        fonts = init_fonts(parent)
        self.form_data = {
            "system": StringVar(),
            "supplys": {
                "quantity": IntVar(),
                "di_module_type": StringVar(),
                "control": BooleanVar(),
                "do_module_type": StringVar(),
                "measurements": BooleanVar(),
                "ai_module_type": StringVar(),
            },
            "feeders": {
                "quantity": IntVar(),
                "di_module_type": StringVar(),
                "control": BooleanVar(),
                "do_module_type": StringVar(),
                "measurements": BooleanVar(),
                "ai_module_type": StringVar(),
            }
        }

        # Заголовок формы
        Label(self, text="Перечень сигналов", style="Header.TLabel").grid(row=1, column=1, pady=15, sticky=(N, ))

        # Система. Полле ввода с лейблом 
        Label(self, text="Объект:").grid(row=2, column=1, sticky=(W, E))
        system_entry = Entry(self, textvariable=self.form_data["system"], font=fonts.get("main_font"), style="ReportApp.TEntry")
        system_entry.grid(row=3, column=1, pady=10, sticky=(W, E))

        # Ввод. Фиелдсет
        supplys_fldset = LabelFrame(self, text="Ввод", padding=10)
        supplys_fldset.grid(row=4, column=1, pady=5, sticky=(W, E))
        supplys_fldset.columnconfigure(index=1, weight=3)
        supplys_fldset.columnconfigure(index=2, weight=1)

        ## Ввод. Кол-во вводов Полле ввода с лейблом 
        Label(supplys_fldset, text="Количество вводов:").grid(row=1, column=1, padx=3, pady=5, sticky=(W, N, S))
        supplys_quantity_etry = Spinbox(
            supplys_fldset,
            from_=0,
            to=100,
            increment=1, 
            width=6,
            textvariable=self.form_data["supplys"]["quantity"],
            font=fonts.get("main_font"),
            style="ReportApp.TSpinbox"
        )
        supplys_quantity_etry.grid(row=1, column=2, padx=3, pady=5, sticky=E)

        ## Ввод. Сигналы сигнализации. Полле ввода с лейблом 
        Label(supplys_fldset, text="Тип I/O оборудования (DI):").grid(row=2, column=1, columnspan=2,  padx=3, pady=5, sticky=(W, E))
        supplys_input_signals_etry = Combobox(
            supplys_fldset,
            values=["ЭНМВ-1", "АИРИС-МИ-120", "ТОР200"],
            textvariable=self.form_data["supplys"]["di_module_type"],
            font=fonts.get("main_font"),
            style="ReportApp.TCombobox"
        )
        supplys_input_signals_etry.grid(row=3, column=1, columnspan=2, padx=3, pady=5, sticky=(W, E))

        ## Ввод. Сигналы управления. Полле ввода с лейблом
        supplys_control_lbl = Label(supplys_fldset, text="Тип I/O оборудования (DO):")
        supplys_control_etry = Combobox(
            supplys_fldset,
            values=["ЭНМВ-1", "АИРИС-МИ-120", "ТОР200"],
            textvariable=self.form_data["supplys"]["do_module_type"],
            font=fonts.get("main_font"),
            style="ReportApp.TCombobox"
        )

        ## Ввод. Сигналы управления. Чекбокс
        supplys_control_chkbox = Checkbutton(
            supplys_fldset,
            text="Управление",
            offvalue=False,
            onvalue=True,
            variable=self.form_data["supplys"]["control"],
            command=lambda: self.hide_show_widget(
                callback_flag=self.form_data["supplys"]["control"],
                widgets=[supplys_control_lbl, supplys_control_etry],
                start_row=5
            ),
            style="ReportApp.TCheckbutton"
        )
        supplys_control_chkbox.grid(row=4, column=1, pady=3, sticky=(W, E))

        ## Ввод. Измерения. Полле ввода с лейблом
        supplys_measurements_lbl = Label(supplys_fldset, text="Тип средства измерений (AI):")
        supplys_measurements_etry = Combobox(
            supplys_fldset,
            values=["ЭНИП-2", "АИРИС-МИ-120", "СЭТ-4"],
            textvariable=self.form_data["supplys"]["ai_module_type"],
            font=fonts.get("main_font"),
            style="ReportApp.TCombobox"
        )

        ## Ввод. Измерения. Чекбокс
        supplys_measurements_chkbox = Checkbutton(
            supplys_fldset,
            text="Измерения",
            offvalue=False,
            onvalue=True,
            variable=self.form_data["supplys"]["measurements"],
            command=lambda: self.hide_show_widget(
                callback_flag=self.form_data["supplys"]["measurements"],
                widgets=[supplys_measurements_lbl, supplys_measurements_etry],
                start_row=8
            ),
            style="ReportApp.TCheckbutton"
        )
        supplys_measurements_chkbox.grid(row=7, column=1, pady=3, sticky=(W, E))

        # Отходящие линии. Фиелдсет
        feeders_fldset = LabelFrame(self, text="Отходящие линии", padding=10)
        feeders_fldset.grid(row=5, column=1, pady=5, sticky=(W, E))
        feeders_fldset.columnconfigure(index=1, weight=3)
        feeders_fldset.columnconfigure(index=2, weight=1)

        ## Отходящие линии. Кол-во вводов Полле ввода с лейблом
        Label(feeders_fldset, text="Количество ОЛ:").grid(row=1, column=1, padx=3, pady=5, sticky=(W, E))
        feeders_quantity_etry = Spinbox(
            feeders_fldset,
            from_=0,
            to=100,
            increment=1, 
            width=4,
            textvariable=self.form_data["feeders"]["quantity"],
            font=fonts.get("main_font"),
            style="ReportApp.TSpinbox"
        )
        feeders_quantity_etry.grid(row=1, column=2, padx=3, pady=5, sticky=(W, E))

        ## Отходящие линии. Сигналы сигнализации. Полле ввода с лейблом 
        Label(feeders_fldset, text="Тип I/O оборудования (DI):").grid(row=2, column=1, columnspan=2, padx=3, pady=5, sticky=(W, E))
        feeders_input_signals_etry = Combobox(
            feeders_fldset, 
            values=["ЭНМВ-1", "АИРИС-МИ-120", "ТОР200"],
            textvariable=self.form_data["feeders"]["di_module_type"],
            font=fonts.get("main_font"),
            style="ReportApp.TCombobox"
        )
        feeders_input_signals_etry.grid(row=3, column=1, columnspan=2, padx=3, pady=5, sticky=(W, E))

        ## Отходящие линии. Сигналы управления. Полле ввода с лейблом
        feeders_control_lbl = Label(feeders_fldset, text="Тип I/O оборудования (DO):")
        feeders_control_etry = Combobox(
            feeders_fldset,
            values=["ЭНМВ-1", "АИРИС-МИ-120", "ТОР200"],
            textvariable=self.form_data["feeders"]["do_module_type"],
            font=fonts.get("main_font"),
            style="ReportApp.TCombobox"
        )

        ## Отходящие линии. Сигналы управления. Чекбокс
        feeders_control_chkbox = Checkbutton(
            feeders_fldset,
            text="Управление",
            offvalue=False,
            onvalue=True,
            variable=self.form_data["feeders"]["control"],
            command=lambda: self.hide_show_widget(
                callback_flag=self.form_data["feeders"]["control"],
                widgets=[feeders_control_lbl, feeders_control_etry],
                start_row=5
            ),
            style="ReportApp.TCheckbutton"
        )
        feeders_control_chkbox.grid(row=4, column=1, pady=3, sticky=(W, E))

        ## Отходящие линии. Измерения. Полле ввода с лейблом
        feeders_measurements_lbl = Label(supplys_fldset, text="Тип средства измерений (AI):")
        feeders_measurements_etry = Combobox(
            feeders_fldset,
            values=["ЭНИП-2", "АИРИС-МИ-120", "СЭТ-4"],
            textvariable=self.form_data["feeders"]["ai_module_type"],
            font=fonts.get("main_font"),
            style="ReportApp.TCombobox"
        )

        ## Отходящие линии. Измерения. Чекбокс
        feeders_measurements_chkbox = Checkbutton(
            feeders_fldset,
            text="Измерения",
            offvalue=False,
            onvalue=True,
            variable=self.form_data["feeders"]["measurements"],
            command=lambda: self.hide_show_widget(
                callback_flag=self.form_data["feeders"]["measurements"],
                widgets=[feeders_measurements_lbl, feeders_measurements_etry],
                start_row=8
            ),
            style="ReportApp.TCheckbutton"
        )
        feeders_measurements_chkbox.grid(row=7, column=1, pady=3, sticky=(W, E))

        accept_button = Button(self, text="Отправить", command=self.send_form_data, style="ReportApp.TButton")
        accept_button.grid(row=6, column=1, sticky=(W, E))

    def hide_show_widget(self, callback_flag, widgets:list, start_row: int):
        if callback_flag.get():
            for offset, widget in enumerate(widgets):
                row_num = start_row+offset
                widget.grid(row=row_num, column=1, columnspan=2, padx=3, pady=5, sticky=(W, E))
        else:
            for widget in widgets:
                widget.grid_forget()
    
    def send_form_data(self):
        form_data = {
            key: {key:subvalue.get() for key, subvalue in value.items()} if isinstance(value, dict) else value.get()
            for key, value in self.form_data.items()
        }
        print(form_data)
        serialized_data = SignalsListSubdataSerializer(**form_data)
        print(serialized_data)
