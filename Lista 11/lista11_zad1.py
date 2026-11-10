from random import uniform

def approximate_pole(n):
    hits = 0
    for _ in range(n):
        x = uniform(0, 8)
        y = uniform(-1, 8)
        if ((x-5)**2 + (y-5)**2 <= 9
                and (x-2)**2 + (y-3)**2 > 4
                and (x-4)**2 + (y-1)**2 > 4):
            hits += 1

    result = "pole = {} dla n = {}".format(72 * hits / n, n)
    print(result)


approximate_pole(100)
approximate_pole(1000)
approximate_pole(10**5) # ok 24
