a, b, c, d, e, f = map(int, input().split())
D = a * e - b * d
if D != 0:
    x = (c * e - b * f) // D
    y = (a * f - c * d) // D
    print(x, y)