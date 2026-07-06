from pathlib import Path
from typing import Any

from app.domain.interfaces import ReportInterface
from app.domain.models import SignalsList


class ReportService:
    REPORTS = {
        "signals list":  SignalsList, 
    }
    
    def __init__(self, report_type: str, report_title="Перечень сигналов"):
        self._report_type: ReportInterface = ReportService.REPORTS[report_type]
        self._report = self._report_type(report_title)
    
    def generate_report(self, data: dict):
        _data = self._report.data_scheme(**data)
        self._report.generate(_data)

    def save(self, path: Path | str):
        if isinstance(path, str):
            path = Path(path)
        self._report.save(path)
    
