class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0

    def val(self, x):
        return self.cells.get(x, 0) if x[0].isalpha() else int(x)

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split('+')
        return self.val(a) + self.val(b)