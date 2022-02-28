n = 8
fib0 = 0
fib1 = 1

while n > 0:
    temp = fib0
    fib0 = fib1
    fib1 += temp
    n -= 1

resul = fib1
print(resul)