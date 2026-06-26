from tkinter import *
from tkinter.ttk import * 

root = Tk()

data = {
    "input_quantity": IntVar(),
    "control_signals": BooleanVar(),
    "io_modul_type": StringVar()
}

def checkbutton_changed():
    if  data["control_signals"].get():
        io_modul_type_lbl.grid(row=2, column=0, sticky=W)
        io_modul_type = grid(row=3, column=0, sticky=W)
    else:
        io_modul_type_lbl.grid_forget()
        io_modul_type.grid_forget()

root.title("Tkinter Sample")

w, h = 300, 200
x = (root.winfo_screenwidth() - w) // 2
y = 60
root.geometry(f"{w}x{h}+{x}+{y}")

form = Frame(root)
form.grid(row=0, column=0, padx=10, pady=10)
form.columnconfigure(index=0, weight=1)

Label(form, text="Перечень сигналов").grid(row=0, column=0, sticky=(W, E))

input_fieldset = Frame(form)
input_fieldset.grid(row=1, column=0)

Label(input_fieldset, text="Количество вводов:").grid(row=0, column=0, sticky=W)
input_quantity_entry = Spinbox(input_fieldset, from_=0, to=100, increment=1,  width=4, textvariable=data["input_quantity"])
input_quantity_entry.grid(row=0, column=1)

# Label(input_fieldset, text="Управление").grid(row=1, column=0, sticky=W)
control_signals_checkbox = Checkbutton(
    input_fieldset, text="Управление",
    offvalue=False,
    onvalue=True,
    variable=data["control_signals"],
    command=checkbutton_changed
)
control_signals_checkbox.grid(row=1, column=0, sticky=W)

io_modul_type_lbl = Label(input_fieldset, text="Тип I/O оборудования:")
io_modul_type = Combobox(
    input_fieldset,
    values=["ЭНМВ-1", "АИРИС-МИ-120", "ТОР200"],
    textvariable=data["io_modul_type"]
)
    



root.mainloop()
