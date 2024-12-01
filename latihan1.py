import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args)/len(args) if args else 0
d = lambda s: "".join(set(s))

print("lambda a(5):", a(5))
print("lambda b(3, 4):", b(3, 4))
print("lambda c(1, 2, 3, 4, 5):", c(1, 2, 3, 4, 5))
print("lambda d('hello lola'):", d("lola"))

