from typing import Any

from app.core import interfaces
from app.settings import STATIC_DIR

from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment
from openpyxl.worksheet.worksheet import Worksheet


class BaseReport(interfaces.ReportInterface):

    def __init__(self, title: str):
        self.title: str = title
        self.data: Any = None
        
        

class XLSReport(BaseReport):
    def __init__(self, title: str):
        super().__init__(title=title)
        self.data: Workbook = Workbook()



class SignalsList(BaseReport):

    def generate(self, data: dict | None = None):
        # Генерируем макет документа
        ## Выделяем активный лист
        data: Workbook = Workbook()
        ws: Worksheet = self.data.active
        ## Изменяем название листа
        ws.title =  "Перечень сигналов"
        ## Объяденяем ячейки под логотип и заголовок
        ws.merge_cells("A1:H1")
        ws.merge_cells("A2:H2")
        ## Устанавливаем высоту объеденённых строк
        ws.row_dimensions[1].height = 116,5
        ws.row_dimensions[2].height = 95
        ## Записываем лого
        logo_img = Image(STATIC_DIR / "img/logo.png")
        ws.add_image(logo_img, 'A1')
        ws["A1"].value = "ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ\nПРОИЗВОДСТВЕННОЕ ОБЪЕДИНЕНИЕ\n«ВЫСОКОВОЛЬТНЫЕ ЭЛЕКТРОТЕХНИЧЕСКИЕ АППАРАТЫ»"
        ws["A1"].alignment = Alignment(horizontal="left", vertical="bottom")
        ws["A2"].value = "Перечень сигналов"
        ws["A2"].alignment = Alignment(horizontal="center", vertical="center")
        ws["A2"].border = Border(top=Side(style="thin"), bottom=Side(style="thin"))

