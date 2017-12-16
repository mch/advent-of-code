import re

f = open('day-12-input.txt')
d = f.readlines()
f.close()

def parse(output, line):
    # 0 <-> 584, 830
    match = re.search("([0-9]+) <-> ([0-9, ]+)", line)
    node = match.group(1)
    connected_nodes = match.group(2).split(', ')
    output[node] = connected_nodes

    return output

graph = reduce(parse, d, {})

all_nodes = set(graph.keys())

connected = set()
connected.add('0')

def traverse(graph, node, connected):
    nodes = graph[node]

    for n in nodes:
        if n not in connected:
            connected.add(n)
            traverse(graph, n, connected)

traverse(graph, '0', connected)
groups = []
groups.append(connected)

print("There are %d programs in the group containing program 0." % len(connected))

remaining = all_nodes.difference(connected)
while len(remaining) > 0:
    connected = set()
    starting_node = remaining.pop()
    connected.add(starting_node)

    traverse(graph, starting_node, connected)
    groups.append(connected)
    remaining = remaining.difference(connected)
