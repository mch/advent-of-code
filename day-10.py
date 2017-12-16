position = 0
skip_size = 0

string = range(0, 256)
lengths = [14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244]
#string = range(0, 5)
#lengths = [3, 4, 1, 5]

for l in lengths:
    sublist = []
    starting_position = position
    for i in xrange(l):
        sublist.append(string[position])
        position = (position + 1) % len(string)

    sublist.reverse()

    position = starting_position
    for i in xrange(l):
        string[position] = sublist[i]
        position = (position + 1) % len(string)

    position = (position + skip_size) % len(string)
    skip_size += 1

print("Multiplying first two numbers, %d * %d = %d" % (string[0], string[1], string[0] * string[1]))
