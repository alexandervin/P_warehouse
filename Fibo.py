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

# class Fibonacci:
#     '''Итератор последовательности Фибоначчи до N элементов'''
#
#     def __init__(self, n):
#         self.i, self.a, self.b, self.n = 0,0,1,n
#
#     def __iter__(self):
#         self.i, self.a, self.b = 0, 0, 1
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > 1:
#             if self.i > self.n:
#                 raise StopIteration
#             self.a, self.b = self.b, self.a + self.b
#             return self.a
#
# fib_iter = Fibonacci(n=8)
# for value in fib_iter:
#     print(value)
#
print(13 in fib_iter)