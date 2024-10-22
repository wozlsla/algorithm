def sum(n):
    if n <= 1:
        return n
    return n + sum(n - 1)


def sum(n):
    if n < 0:
        return "ERROR : Use non-negative integer"
    if n <= 1:
        return n
    return n + sum(n - 1)


def sum(n):
    print(n)
    if n == 0:
        return n
    elif n > 0:
        return n + sum(n - 1)
    elif n < 0:
        return n + sum(n + 1)


print(sum(int(input("Num: "))))
