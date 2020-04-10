def fibo(x):
    if  x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)
print(fibo(7))

def fibonnaci(n):
    result = []
    a,b = 0,1
    for i in range(n):
        result.append(a)
        a,b = b, a+b
    return result

print(fibonnaci(8))

for value in fibonnaci(8):
    print(value)