def func(x):
    if y in x:
        print(x.index(y))
    else:
        print(-1)
    return(y)
x = list(map(int, input("Input list")))
y = 4
print(func(x))