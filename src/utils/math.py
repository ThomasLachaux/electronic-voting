def exponentiation(a, n, m):

    b = 1
    c = a
    i = 0
    pow = 1

    while n > 0:
        k = n % 2
        n = n >> 1
        if k == 1:
            b = b * c % m
        c = c * c % m
        i += 1
        pow *= 2

    return b % m
