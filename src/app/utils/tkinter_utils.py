from openpyxl.styles import (Alignment,
                             Border,
                             NamedStyle,
                             Side, 
                             Font,
                             PatternFill)


normalize: NamedStyle = NamedStyle(
    name="normalize",
)
normalize.font = Font(name="Arial", size=14, color="000000")
normalize.fill = PatternFill(fill_type=None, start_color="FFFFFF")
normalize.border = Border()
normalize.alignment = Alignment(horizontal='center', vertical='center')

tb_border: NamedStyle = NamedStyle(
    name="tb_border",
)
tb_border.border = Border(top=Side("thin", "000000"), bottom=Side("thin", "000000"))

def adjust_col_width(ws):
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) * 1.5
        ws.column_dimensions[column_letter].width = adjusted_width

def apply_style(items: tuple, style_name: str):
    for item in items:
        for cell in item:
            cell.style = style_name
