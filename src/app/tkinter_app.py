from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Отчёты отдела АСУ")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

form = ttk.Frame(root, padding=20)
form.columnconfigure(2, weight=1)
form.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(form, text="Перечень сигналов").grid(column=1, row=0, sticky=(N, ))

input_info_fieldset = ttk.Frame(form, padding=10)
input_info_fieldset.grid(column=1, row=1)

ttk.Label(input_info_fieldset, text="Колличество вводов:").grid(column=1, row=1, sticky=W)

av_quantity = StringVar()
av_quantity_entry = ttk.Entry(input_info_fieldset, textvariable=av_quantity)
av_quantity_entry.grid(column=1, row=2, sticky=W)

for child in form.winfo_children(): 
    for subchild in child.winfo_children():
        subchild.grid_configure(pady=2)

av_quantity_entry.focus()


ttk.Button(form, text="Сформировать").grid(column=1, sticky=S)



root.mainloop()