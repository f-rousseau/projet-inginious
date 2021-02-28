import numpy as np


def secondDegree(a, b, c):
    coeff = [a, b, c]
    sol = np.roots(coeff)
    if np.iscomplex(sol[0]):
        return None
    return sorted(sol)


print(secondDegree(0, 0, 1))
