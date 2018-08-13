Y = lambda f:(lambda x:x(x))(lambda y:f(lambda *args:y(y)(*args)))
power_gen = lambda f:lambda n:n*n
print(Y(power_gen)(10))
fac_gen = lambda f:lambda n: 1 if n < 2 else f(n-1) + f(n-2)
print([Y(fac_gen)(i) for i in range(10)])
