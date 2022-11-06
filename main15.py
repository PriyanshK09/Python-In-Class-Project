def name(x):
    return lambda a : a + x

num = name(10)
print(num(5))