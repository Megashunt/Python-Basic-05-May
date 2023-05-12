from math import sqrt
a = int(input("Type your first number here ->>"))
b = int(input("Type your second number here ->>"))
c = int(input("Type your third number here ->>"))

d = b ** 2 - 4 * a * c
print(d)

if d >= 0:
    print('Yes, it bigger')
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(x1)
    print(x2)
else:
    print('Not, it is not')

print(x1)

str_input =