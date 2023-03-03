# def square_power(n):
#     for i in range(1, n + 1):
#         yield i * i


# nums = int(input())
# a = square_power(nums)

# for i in range(nums):
#     print(next(a), end=" ")

# def even_numbers(n):
#     for i in range(1, n + 1):
#         if (i % 2 == 0):
#             yield i


# second_num = int(input())
# for i in even_numbers(second_num):
#     print(i, end=" ")

# 3
# def three_four(n):
#     for i in range(1, n+1):
#         if (i % 3 == 0 and i % 4 == 0):
#             yield i


# for i in three_four(int(input())):
#     print(i, end=" ")

# 4
# def square(a, b):
#     for i in range(a, b + 1):
#         yield i * i


# first = int(input())
# second = int(input())
# for i in square(first, second):
#     print(i, end=" ")

def reverse(n):
    i = n
    while i != -1:
        yield i
        i -= 1


reverse_num = int(input())
for i in reverse(reverse_num):
    print(i, end=" ")
