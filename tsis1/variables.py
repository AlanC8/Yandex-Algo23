x = 5
y = "John"
print(type(x))
print(type(y))
x1 = str(3)    # x will be '3'
y1 = int(3)    # y will be 3
z = float(3)  # z will be 3.0
x2, y2, z2 = "Orange", "Banana", "Cherry"
print(x2)
print(y2)
print(z2)
fruits = ["apple", "banana", "cherry"]
x3, y3, z3 = fruits
print(x3)
print(y3)
print(z3)


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)