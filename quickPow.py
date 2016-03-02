def mpow(a, d, n):
    res = 1
    while d > 0:
        if d&1:
            res = res * a % n
        a = a*a%n
        d>>=1
    return res