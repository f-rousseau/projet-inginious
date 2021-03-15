def secondDegree(a, b, c):
    delta = b ** 2 - (4 * a * c)
    if delta < 0:
        return None
    froot = (-b + delta ** (1 / 2)) / (2 * a)
    sroot = (-b - delta ** (1 / 2)) / (2 * a)
    return sorted((froot, sroot))
