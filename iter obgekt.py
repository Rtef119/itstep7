class Counter:
    def __init__(self, max):
        self.i = 0
        self.max = max

    def __iter__(self):
        self.i = 0
        return self