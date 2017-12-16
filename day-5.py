f = open('day-5-input.txt')
d = f.read()
f.close()

def toInts(output, s):
    try:
        i = int(s)
        output.append(i)
    except ValueError:
        pass

    return output

str_offsets = d.split('\n')
offsets = reduce(toInts, str_offsets, [])

def escape(maze):
    position = 0
    steps = 0
    while position >= 0 and position < len(maze):
        offset = maze[position]
        maze[position] += 1
        position += offset
        steps += 1

    return steps

steps = escape([0, 3, 0, 1, -3])
print("Test maze takes %d steps to escape." % (steps, ))

steps = escape(offsets)
print("Full maze takes %d steps to escape." % (steps, ))
