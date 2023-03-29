class newIter:
    def __iter__(self):
        self.a = 5
        return self

    def __next__(self):
        x = self.a
        self.a += 5
        return x


nit = newIter()
afsaf = iter(nit)

for i in range(5):
    print(next(afsaf))
