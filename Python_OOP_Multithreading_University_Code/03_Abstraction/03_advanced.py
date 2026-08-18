"""Template-method style abstraction."""

from abc import ABC, abstractmethod

class DataExporter(ABC):
    def export(self, rows: list[dict]) -> str:
        """Concrete workflow uses abstract formatting step."""
        self._validate(rows)
        return self._format(rows)

    def _validate(self, rows):
        if not isinstance(rows, list):
            raise TypeError("rows must be a list")

    @abstractmethod
    def _format(self, rows: list[dict]) -> str:
        pass

class CsvExporter(DataExporter):
    def _format(self, rows):
        if not rows:
            return ""
        headers = list(rows[0])
        lines = [",".join(headers)]
        lines.extend(",".join(str(row[h]) for h in headers) for row in rows)
        return "\n".join(lines)

class TextExporter(DataExporter):
    def _format(self, rows):
        return "\n".join(str(row) for row in rows)


def main():
    rows = [{"id": 1, "name": "Isha"}, {"id": 2, "name": "Dev"}]
    print(CsvExporter().export(rows))
    print("---")
    print(TextExporter().export(rows))


if __name__ == "__main__":
    main()
