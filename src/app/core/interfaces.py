from abc import ABC, abstractmethod


class ReportInterface(ABC):

    @abstractmethod
    def generate():
        """Create report"""
        pass

    @abstractmethod
    def save(self):
        """Save report"""
        pass