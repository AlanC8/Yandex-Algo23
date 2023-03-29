class iterating:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


iterator = iterating()
myiter = iter(iterator)

for i in range(20):
    print(next(myiter))
