from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Border, Side, NamedStyle, Font, Alignment
from openpyxl.worksheet.worksheet import Worksheet


from app.settings import APP_DIR, STATIC_DIR

data = {
    "input": {
        "quantity": 2,
        "measurement": True,
        "mip_type": "ЭНИП-2",
        "io_modul_type": "ЭНМВ-1",
        "control_signals": True
    },
    "output": {
        "quantity": 5,
        "measurement": True,
        "mip_type": None,
        "io_modul_type": "ЭНМВ-1",
        "control_signals": False
    } 
}

def generate():
    pass

if __name__ == "__main__":
    generate()