def alltrue(tpl):
    return len(tuple(filter(lambda x: x == True, tpl))) == len(tpl)


newTuple = tuple((1, True))
print(alltrue(newTuple))
