from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

class ReportInterface(ABC):

    @abstractmethod
    def generate(self, data: Any):
        """Create report"""
        pass

    @abstractmethod
    def save(self, path: Path | str):
        """Save report"""
        pass