f = open("day-2-input.txt")
d = f.read()
f.close()

lines = d.split('\n')
lines = filter(lambda l: len(l) > 0, lines)
lines = [ x.split('\t') for x in lines ]

int_lines = map(lambda l: [ int(x) for x in l ], lines)

max_min = map(lambda l: (max(l), min(l)), int_lines)

diffs = map(lambda l: l[0] - l[1], max_min)

checksum = reduce(lambda x, y: x + y, diffs)

print("Checksum: %d" % (checksum,))
