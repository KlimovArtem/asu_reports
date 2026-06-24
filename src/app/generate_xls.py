from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Border, Side, NamedStyle, Font, Alignment
from openpyxl.worksheet.worksheet import Worksheet


from app.settings import APP_DIR, STATIC_DIR


def adjust_col_Width(ws):
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = max_length + 10
        ws.column_dimensions[column_letter].width = adjusted_width


data = {
    "system": "НКУ",
    "input": {
        "quantity": 2,
        "control_signals": True,
        "cs_protocol": "Modbus RTU",
        "io_modul_type": "ЭНМВ-1",
        "mesurment": True,
        "mesurment_protocol": "Modbus RTU",
        "mip_type": "ЭНИП-2"
    },
    "output": {
        "quantity": 5,
        "control_signals": False,
        "io_modul_type": "ЭНМВ-1",
        "mesurment": True,
        "mip": "ЭНИП-2"
    }
}


def generate(data: dict):
    wb = Workbook()
    ws = wb.active
    ws.append(
        [
            "№ п/п",
            "Система",
            "Наименование", 
            "Наименование сигнала",
            "Источник сигнала",
            "Тип сигнала",
            "Примечание"
        ]
    )
    counter = 1
    for i in range(1, data["input"]["quantity"]+1):
        if data["input"]["control_signals"]:
            ws.append(
                [
                    counter,
                    data["system"],
                    f"Ввод {i}",
                    "Команда включить",
                    data["input"]["io_modul_type"],
                    "ТУ",
                    ""
                ]
            )
            counter += 1
            ws.append(
                [
                    counter,
                    data["system"],
                    f"Ввод {i}",
                    "Команда отключить",
                    data["input"]["io_modul_type"],
                    "ТУ",
                    ""
                ]
            )
        counter += 1
        ws.append(
            [
                counter,
                data["system"],
                f"Ввод {i}",
                'Положение выключателя "включен"',
                data["input"]["io_modul_type"],
                "ТС",
                ""
            ]
        )
        counter += 1
        ws.append(
            [
                counter,
                data["system"],
                f"Ввод {i}",
                'Положение выключателя "отключен"',
                data["input"]["io_modul_type"],
                "ТС",
                ""
            ]
        )
        counter += 1
        ws.append(
            [
                counter,
                data["system"],
                f"Ввод {i}",
                'Аварийное отключение"',
                data["input"]["io_modul_type"],
                "ТС",
                ""
            ]
        )
        counter += 1
        if data["input"]["mesurment"]:
            ws.append(
                [
                    counter,
                    data["system"],
                    f"Ввод {i}",
                    "Ток - фаза A",
                    data["input"]["mip_type"],
                    "ТИ",
                    ""
                ]
            )
            counter += 1
            ws.append(
                [
                    counter,
                    data["system"],
                    f"Ввод {i}",
                    "Ток - фаза B",
                    data["input"]["mip_type"],
                    "ТИ",
                    ""
                ]
            )
            counter += 1
            ws.append(
                [
                    counter,
                    data["system"],
                    f"Ввод {i}",
                    "Ток - фаза C",
                    data["input"]["mip_type"],
                    "ТИ",
                    ""
                ]
            )
            counter += 1
            ws.append(
                [
                    counter,
                    data["system"],
                    f"Ввод {i}",
                    "Напряжение AB",
                    data["input"]["mip_type"],
                    "ТИ",
                    ""
                ]
            )
            counter += 1
            ws.append(
                [
                    counter,
                    data["system"],
                    f"Ввод {i}",
                    "Напряжение BC",
                    data["input"]["mip_type"],
                    "ТИ",
                    ""
                ]
            )
            counter += 1
            ws.append(
                [
                    counter,
                    data["system"],
                    f"Ввод {i}",
                    "Напряжение CA",
                    data["input"]["mip_type"],
                    "ТИ",
                    ""
                ]
            )
    for i in range(data["output"]["quantity"]):
        counter += 1
        ws.append(
            [
                counter,
                data["system"],
                f"ОЛ {i}",
                'Положение выключателя "включен"',
                data["input"]["mip_type"],
                "ТИ",
                ""
            ]
        )
        ws.append(
            [
                counter,
                data["system"],
                f"ОЛ {i}",
                'Положение выключателя "отключен"',
                data["input"]["mip_type"],
                "ТИ",
                ""
            ]
        )
        ws.append(
            [
                counter,
                data["system"],
                f"ОЛ {i}",
                "Аварийное отключение выключателя",
                data["input"]["mip_type"],
                "ТИ",
                ""
            ]
        )
    adjust_col_Width(ws)
    wb.save(APP_DIR.parent.parent / "temp/example.xlsx")


if __name__ == "__main__":
    generate(data)