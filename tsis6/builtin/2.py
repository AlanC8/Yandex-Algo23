def cnter(s):
    a = len(list(filter(lambda u: u.isupper(), s)))
    return a, len(s)-a


print(cnter("SfafaS"))
