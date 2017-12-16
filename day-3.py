import itertools

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...

# n Steps direction
# 1 0 (0, 0)
# 1 1 (1, 0)
# 2 1 (0, 1)
# 3 2 (-1, 0)
# 4 2 (0, -1)
# 5 3 (1, 0)
# 3 (0, 1)
# 4 (-1, 0)
# 4 (0, -1)
# 5 (1, 0)
# 5 (0, 1)

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

def coord(n):
    if n < 1:
        raise Exception()

    d = (1,0)
    steps_taken = 0
    steps_in_leg = 1
    position = (0,0)

    count = 0
    while steps_taken < n - 1:
        if steps_taken + steps_in_leg > n - 1:
            steps_in_leg = n - 1 - steps_taken

        step = (d[0] * steps_in_leg, d[1] * steps_in_leg)
        position = (position[0] + step[0], position[1] + step[1])
        yield position

        steps_taken += steps_in_leg
        d = next_direction(d)
        count += 1
        if count % 2 == 0:
            steps_in_leg += 1

def last_coord(n):
    last = (0,0)
    for c in coord(n):
        last = c

    return last

def steps_to_port(position):
    return abs(position[0]) + abs(position[1])

def check(n, expected):
    try:
        actual = last_coord(n)
    except Exception as e:
        print("exception: %s" % (e))
        return

    if actual == expected:
        print("ok: last_coord(%d) == %s" % (n, expected))
    else:
        print("fail: last_coord(%d) != %s, got %s instead." % (n, expected, actual))

check(0, Exception())
check(1, (0,0))
check(2, (1,0))
check(3, (1,1))
check(4, (0,1))
check(5, (-1,1))
check(6, (-1,0))
check(7, (-1,-1))
check(8, (0,-1))
check(15, (0,2))

def day3(n):
    print("Steps to port for %d: %d" % (n, steps_to_port(last_coord(n))))

day3(1)
day3(12)
day3(23)
day3(1024)
day3(325489)

def neighbours(p):
    offsets = [-1, 0, 1]
    return fitler(lambda x: x != (0,0), itertools.product(offsets, offsets))

data = {}
max_value = 0
for c in coord(23):
    
