import math
def fun(x):
    return x**3 - 8*x + 1 + 12*math.sin(x) + 10*math.cos(x)

def find_roots_on_interval(start, end, step):
    roots = []
    current = start
    while current <= end:
        x1 = current
        x2 = current + step
        if fun(x1) * fun(x2) < 0:
            root = binary_search(x1, x2)
            roots.append(root)
        current += step
    return roots

def binary_search(x1, x2):
    precision = 0.001
    while abs(x2 - x1) >= precision:
        mid = (x1 + x2) / 2.0
        if fun(mid) == 0.0:
            return mid
        elif fun(mid) * fun(x1) < 0:
            x2 = mid
        else:
            x1 = mid
    return (x1 + x2) / 2.0

roots = find_roots_on_interval(-5, 5, 0.1)

for idx, root in enumerate(roots):
    print(f"Интервал {idx+1}:")
    print(f"Решение: {round(root, 3)}")

for idx, root in enumerate(roots):
    interval_start = round(idx * 0.1 - 5, 1)
    interval_end = round((idx + 1) * 0.1 - 5, 1)
    print(f"Интервал [{interval_start:.1f};{interval_end:.1f}]")
    print(f"Решение: {round(root, 3)}")

