from app.domain.interfaces import ReportInterface
from app.domain.models import SignalsList


class ReportService:
    REPORTS = {
        "signals list": SignalsList
    }
    
    def __init__(self, report_name: str):
        self._report: ReportInterface = ReportService.REPORTS[report_name]
    
    def generate_report(self, data):
            return self._report.generate(data)

    def save(self, path):
        return self._report.save(path)
    
