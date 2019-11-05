from math import asin, degrees, sin, cos, radians


def f(a, b, rad):
    return 0.5 * a ** 3 * sin(rad) + a * (1 / cos(rad)) * (b * cos(rad) - a * sin(rad))


a, b, x = map(int, input().split(" "))

for deg in range(0, 91):
    rad = radians(deg)
    c = f(a, b, rad)
    if x > c:
        print(deg)
        break
