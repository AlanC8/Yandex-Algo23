def cnter(s):
    a = len(list(filter(lambda u: u.isdigit(), s)))
    return a, len(s)-a


print(cnter("Sfafa5"))
