class Counter:
    def __init__(self, max):
        self.i = 0
        self.max = max

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max:
            raise StopIteration
        return self.i

count = Counter(5)
for elem in count:
    print(elem)