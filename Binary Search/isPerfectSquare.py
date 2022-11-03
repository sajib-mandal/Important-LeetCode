def isPerfectSquare(x):
    l, r = 0, x
    while l <= r:
        m = (l + r) // 2
        if m * m < x:
            l = m + 1
        elif m * m > x:
            r = m - 1
        else:
            return m
    return r


print(isPerfectSquare(16))
print(isPerfectSquare(14))
