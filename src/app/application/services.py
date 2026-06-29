from app.domain.interfaces import ReportInterface


class ReportService:
    def __init__(self, report_type: ReportInterface):
        self._report: ReportInterface = report_type()
    
    def generate_report(self, data):
        