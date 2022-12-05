class Location:
    def __init__(self, line: int, column: int):
        self._line = line
        self._column = column

    def getLine(self):
        return self._line

    def getColumn(self):
        return self._column
