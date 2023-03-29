class Person:
    name = "John"
    age = 36
    country = "Norway"


x = getattr(Person, 'age')
print(x)
