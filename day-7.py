f = open('day-7-input.txt')
d = f.read()
f.close()

sample = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""

#lines = sample.split('\n')
lines = d.split('\n')

def parse_line(output, l):
    if len(l) < 1:
        return output

    match = re.search('([a-z]+) \(([0-9]+)\)', l)
    children_match = re.search(' -> ([a-z, ]+)', l)

    if match is not None and children_match is None:
        output.append((match.group(1), match.group(2), []))
    elif match is not None and children_match is not None:
        children = children_match.group(1).split(', ')
        output.append((match.group(1), match.group(2), children))

    return output

programs = reduce(parse_line, lines, [])

def prune_leaves(programs, leaf_names):
    shears = lambda collection: filter(lambda name: name not in leaf_names, collection)
    programs = map(lambda p: (p[0], p[1], shears(p[2])), programs)

    return programs

prune_branches = lambda programs: filter(lambda p: len(p[2]) > 0, programs)

print("Number of programs: %d, number of leaves: %d" % (len(programs), len(leafs)) )

leafs = filter(lambda x: len(x[2]) == 0, programs)
leaf_names = set(map(lambda l: l[0], leafs))

count = len(programs) + 1
while len(programs) < count and len(programs) > 1:
    count = len(programs)
    programs = prune_leaves(programs, leaf_names)

    leafs = filter(lambda x: len(x[2]) == 0, programs)
    for leaf in leafs:
        leaf_names.add(leaf[0])

    programs = prune_branches(programs)

    print("Number of programs: %d, number of leaves: %d" % (len(programs), len(leafs)) )

# bottom program...
# start with a set of leaf programs that have no children
# for each program that is not a leaf, see if it's children are only leafs, and if so, treat it as a leaf.
# iterate until one program is left.
