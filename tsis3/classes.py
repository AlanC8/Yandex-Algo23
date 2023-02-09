# class InputOutString(object):
#     def __init__(self):
#         self.s = ""

#     def getString(self):
#         self.s = input()
    
#     def print_string(self):
#         print(self.s.upper())

# strObj = InputOutString()
# strObj.getString()
# strObj.printString()


# class Shape(object):
#     def __init__(self):
#         self.
#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, l):
#         Shape.__init__(self)
#         self.length = l

#     def area(self):
#         return self.length*self.length

# aSquare= Square(5)
# print(aSquare.area())


# class Point:
#     def move(self,x,y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(str(self.x) + ' ' + str(self.y))

#     def dist(self):
#         print(abs(self.y-self.x))

# p = Point()

# p.move(1,2)
# p.show()
# p.dist()
# p.move(10,5)
# p.dist()

class Account:
    owner = ""
    balance = 0
    def deposit(self,dep):
        self.dep = dep
        self.balance += dep

    def withdraw(self,wit):
        self.wit = wit
        self.balance -= wit
        print(self.balance)

bank = Account()

bank.deposit(int(input()))

bank.withdraw(int(input()))

