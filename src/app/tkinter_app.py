from tkinter import *
from tkinter.ttk import * 

from app.domain.models import FormData, RequestData
from app.presentation.views import SignalsListView

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title = "Отчёты АСУ"

        view = SignalsListView(self)
        view.pack(fill="both", expand=True, anchor="center")


# root = Tk()

# data = {
#     "system": StringVar(),
#     "input_quantity": IntVar(),
#     "control_signals": BooleanVar(),
#     "io_modul_type": StringVar(),
#     "mesuarment": BooleanVar(),
#     "mesuarment_instrument_type": StringVar(),
#     "output_quantity": IntVar(),
#     "out_control_signals": BooleanVar(),
#     "out_io_modul_type": StringVar(),
#     "out_mesuarment": BooleanVar(),
#     "out_mesuarment_instrument_type": StringVar(),
# }

# def open_control_comand_fields():
#     if  data["control_signals"].get():
#         io_modul_type_lbl.grid(row=2, column=0, sticky="ew", padx=3, pady=5)
#         io_modul_type.grid(row=3, column=0, sticky="ew", padx=3, pady=5)
#     else:
#         io_modul_type_lbl.grid_forget()
#         io_modul_type.grid_forget()

# def open_out_control_comand_fields():
#     if data["out_control_signals"].get():
#         out_io_modul_type_lbl.grid(row=2, column=0, sticky=W, padx=3, pady=5)
#         out_io_modul_type.grid(row=3, column=0, sticky=W, padx=3, pady=5)
#     else:
#         out_io_modul_type_lbl.grid_forget()
#         out_io_modul_type.grid_forget()


# def open_mesuarment_fields():
#     if  data["mesuarment"].get():
#         mesuarment_instrument_type_lbl.grid(row=5, column=0, sticky=W, padx=3, pady=5)
#         mesuarment_instrument_type.grid(row=6, column=0, sticky=W, padx=3, pady=5)
#     else:
#         mesuarment_instrument_type_lbl.grid_forget()
#         mesuarment_instrument_type.grid_forget()

# def open_out_mesuarment_fields():
#     if data["out_mesuarment"].get():
#         out_mesuarment_instrument_type_lbl.grid(row=5, column=0, sticky=W, padx=3, pady=5)
#         out_mesuarment_instrument_type.grid(row=6, column=0, sticky=W, padx=3, pady=5)
#     else:
#         out_mesuarment_instrument_type_lbl.grid_forget()
#         out_mesuarment_instrument_type.grid_forget()


# def send_data():
#     global data
#     # form_data = {key: value.get() for key, value in data.items()}
#     print(data)

# root.title("Отчёты АСУ")

# form = Frame(root, padding=10)
# form.pack(fill="both", expand=True, anchor="center")

# Label(form, text="Перечень сигналов").pack(fill="x", expand=True, padx=10, pady=5)

# Label(form, text="Объект:").pack(fill="x", expand=True, padx=3, pady=5)
# Entry(form, textvariable=data["system"]).pack(fill="x", expand=True, padx=3, pady=5)

# input_fieldset = LabelFrame(form, text="Ввод", padding=10)
# input_fieldset.pack(fill="both", expand=True)

# Label(input_fieldset, text="Количество вводов:").grid(row=0, column=0, sticky=W, padx=3, pady=5)
# input_quantity_entry = Spinbox(input_fieldset, from_=0, to=100, increment=1,  width=4, textvariable=data["input_quantity"])
# input_quantity_entry.grid(row=0, column=1, padx=3, pady=5)

# control_signals_checkbox = Checkbutton(
#     input_fieldset, text="Управление",
#     offvalue=False,
#     onvalue=True,
#     variable=data["control_signals"],
#     command=open_control_comand_fields
# )
# control_signals_checkbox.grid(row=1, column=0, sticky=W, pady=3)

# io_modul_type_lbl = Label(input_fieldset, text="Тип I/O оборудования:")
# io_modul_type = Combobox(
#     input_fieldset,
#     values=["ЭНМВ-1", "АИРИС-МИ-120", "ТОР200"],
#     textvariable=data["io_modul_type"]
# )

# mesuarment_checkbox = Checkbutton(
#     input_fieldset, text="Измерения",
#     offvalue=False,
#     onvalue=True,
#     variable=data["mesuarment"],
#     command=open_mesuarment_fields
# )
# mesuarment_checkbox.grid(row=4, column=0, sticky=W, pady=3)

# mesuarment_instrument_type_lbl = Label(input_fieldset, text="Тип средства измерений:")
# mesuarment_instrument_type = Combobox(
#     input_fieldset,
#     values=["ЭНИП-2", "АИРИС-МИ-120", "СЭТ-4"],
#     textvariable=data["mesuarment_instrument_type"]
# )

# output_fieldset = LabelFrame(form, text="Отходящие линии", padding=10)
# output_fieldset.pack(fill="both", expand=True)

# Label(output_fieldset, text="Количество ОЛ:").grid(row=0, column=0, sticky=W, padx=3, pady=5)
# output_quantity = Spinbox(output_fieldset, from_=0, to=100, increment=1,  width=4, textvariable=data["output_quantity"])
# output_quantity.grid(row=0, column=1, padx=3, pady=5)

# out_control_signals_checkbox = Checkbutton(
#     output_fieldset,
#     text="Управление",
#     offvalue=False,
#     onvalue=True,
#     variable=data["out_control_signals"],
#     command=open_out_control_comand_fields
# )
# out_control_signals_checkbox.grid(row=1, column=0, sticky=W, pady=3)

# out_io_modul_type_lbl = Label(output_fieldset, text="Тип I/O оборудования:")
# out_io_modul_type = Combobox(
#     output_fieldset,
#     values=["ЭНМВ-1", "АИРИС-МИ-120", "ТОР200"],
#     textvariable=data["out_io_modul_type"]
# )

# out_mesuarment_checkbox = Checkbutton(
#     output_fieldset, text="Измерения",
#     offvalue=False,
#     onvalue=True,
#     variable=data["out_mesuarment"],
#     command=open_out_mesuarment_fields
# )
# out_mesuarment_checkbox.grid(row=4, column=0, sticky=W, pady=3)

# out_mesuarment_instrument_type_lbl = Label(output_fieldset, text="Тип средства измерений:")
# out_mesuarment_instrument_type = Combobox(
#     output_fieldset,
#     values=["ЭНИП-2", "АИРИС-МИ-120", "СЭТ-4"],
#     textvariable=data["out_mesuarment_instrument_type"]
# )

# accept_button = Button(form, text="Отправить", command=send_data)
# accept_button.pack(fill="x", expand=True, padx=10, pady=10)

# root.mainloop()


if __name__ == "__main__":
    app = App()
    app.mainloop()