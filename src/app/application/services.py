from app.domain.interfaces import ReportInterface


class ReportService:
    def __init__(self, report_type: ReportInterface):
        self._report: ReportInterface = report_type()
    
    def generate_report(self, data):
        return self._report.generate(data)

    def save(self, path):
        return self._report.save(path)