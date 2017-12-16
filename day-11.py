import math

f = open('day-11-input.txt')
d = f.read()
f.close()

directions = d[0:len(d)-1].split(',')

# Hex tiles...
# Assume we start at the origin, movement is a translation...
n = (0, 1)
s = (0, -1)
ne = (math.cos(math.radians(30)), math.sin(math.radians(30)))
se = (math.cos(math.radians(30)), -math.sin(math.radians(30)))
nw = (-math.cos(math.radians(30)), math.sin(math.radians(30)))
sw = (-math.cos(math.radians(30)), -math.sin(math.radians(30)))

def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

position = (0.0,0.0)
max_distance = 0.0
max_distance_position = position
for d in directions:
    if d == "n":
        position = add(position, n)
    elif d == "s":
        position = add(position, s)
    elif d == "se":
        position = add(position, se)
    elif d == "sw":
        position = add(position, sw)
    elif d == "ne":
        position = add(position, ne)
    elif d == "nw":
        position = add(position, nw)
    else:
        print("Unknown direction '%s'" % d)

    distance = math.sqrt(math.pow(position[0], 2) + math.pow(position[1], 2))
    if distance > max_distance:
        max_distance = distance
        max_distance_position = position

print("Position of lost thing: %s" % str(position))
print("Furthest from home: %s, position of lost thing: %s" % (str(max_distance), str(max_distance_position)))

def steps_home(position):
    steps = 0
    while abs(position[0]) > 0.25 or abs(position[1]) > 0.25:
        if position[0] < -0.25 and position[1] > 0.25:
            position = add(position, se)
            #print("moved se")
        elif position[0] < -0.25 and position[1] < -0.25:
            position = add(position, ne)
            #print("moved ne")
        elif position[0] > 0.25 and position[1] > 0.25:
            position = add(position, sw)
            #print("moved sw")
        elif position[0] > 0.25 and position[1] < -0.25:
            position = add(position, nw)
            #print("moved nw")
        elif position[1] > 0.25:
            position = add(position, s)
            #print("moved s")
        elif position[1] < -0.25:
            position = add(position, n)
            #print("moved n")
        else:
            print("WTF")
            break

        steps += 1
    return steps

# Attempt 1: 1043, too high
steps = steps_home(position)
print("Stopped after %d steps at %s" % (steps, str(position)))

# part 2
# Attempt 1: 1467, too low
max_steps = steps_home(max_distance_position)
print("Number of steps home: %d, from %s" % (max_steps, str(max_distance_position)))

