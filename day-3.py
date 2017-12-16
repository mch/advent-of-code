input = 325489

def next_direction(d):
    if d == (1, 0):
        return (0, 1)
    elif d == (0, 1):
        return (-1, 0)
    elif d == (-1, 0):
        return (0, -1)
    elif d == (0, -1):
        return (1, 0)

    raise Exception()

def find_position(n):
    direction = (1, 0)
    distance = 1

    return (n - 1, 0)


def check(n, expected):
    result = find_position(n)
    if result == expected:
        print("OK")
    else:
        print("Fail: find_position(%d) != %s, got %s" % (n, str(expected), str(result)))

check(1, (0,0))
check(2, (1,0))
check(3, (1,1))
