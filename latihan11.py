import math
nilaiA = lambda x: x**2
a = nilaiA(5)
print(a)

nilaiB = lambda x, y: math.sqrt(x**2 + y**2)
b = nilaiB(10, 6)
print(b)

nilaiC = lambda *args: sum(args)/len(args)
c = nilaiC(1, 2, 3)
print(c)

nilaiD = lambda s: "#".join(set(s))
d = nilaiD("153")
print(d)
