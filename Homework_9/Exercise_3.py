def func(n, m):
    res = '*' * m + '\n' + ('*' + ' ' * (m - 2) + '*' + '\n') * (n - 2) + '*' * m
    return(res)
n = int(input('N = '))
m = int(input("M = "))
print(func(n, m))
