import time


def squaretime(n, t):
    time.sleep(t/1000)
    return n ** 0.5


print(squaretime(4, 10000))
