class Duct:
    size = 0
    name = ""

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def print(self):
        print(self.name, self.size)
