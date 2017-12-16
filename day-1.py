
f = open('day-1-input.txt')
d = f.read()
f.close()

pairs = zip(d, d[1:])

pairs[-1] = (pairs[-1][0], d[0])

matching_pairs = filter(lambda p: p[0] == p[1], pairs)

result = reduce(lambda x, y: x + int(y[0]), matching_pairs, 0)

print("Result for day 1: %d" % (result,))
