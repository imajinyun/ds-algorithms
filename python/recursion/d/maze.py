class Maze:

    def __init__(self, filename: str) -> None:
        self.items, file = [], open(filename, 'r')
        for line in file:
            rows = []
            col = 0

    def __getitem__(self, index):
        return self.items[index]
