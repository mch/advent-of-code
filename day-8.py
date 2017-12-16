import re

f = open('day-8-input.txt')
d = f.read()
f.close()

sample = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

lines = d.split('\n')
#lines = sample.split('\n')

def parse_line(outputs, line):
    matches = re.search('([a-z]+) ([a-z]+) ([0-9\-]+) if ([a-z]+) ([><=!]+) ([0-9\-]+)', line)

    if matches is not None:
        register = matches.group(1)
        operation= matches.group(2)
        value = int(matches.group(3))
        cond_register = matches.group(4)
        cond_op = matches.group(5)
        cond_value = int(matches.group(6))

        outputs.append((register, operation, value, cond_register, cond_op, cond_value))

    return outputs

instructions = reduce(parse_line, lines, [])

def eval_condition(registers, register, op, value):
    if register not in registers:
        registers[register] = 0

    reg_value = registers[register]
    if op == '>' and reg_value > value:
        return True
    elif op == '<' and reg_value < value:
        return True
    elif op == '>=' and reg_value >= value:
        return True
    elif op == '<=' and reg_value <= value:
        return True
    elif op == '!=' and reg_value != value:
        return True
    elif op == '==' and reg_value == value:
        return True

    return False

def update_register(registers, register, op, value):
    if register not in registers:
        registers[register] = 0

    if op == 'inc':
        registers[register] += value
    elif op == 'dec':
        registers[register] -= value

    return registers

registers = {}
for i in instructions:
    if eval_condition(registers, i[3], i[4], i[5]):
        update_register(registers, i[0], i[1], i[2])

biggest = reduce(lambda x, y: x if registers[x] > registers[y] else y, registers.keys())

print("Register with largest value is %s, value: %d" % (biggest, registers[biggest]))

class Instruction:
    def __init__(self):
        self.affected_register = None # String
        self.operation = None # inc or dec
        self.value = None # integer
        self.cond_register = None # String
        self.cond_op = None # > < >= <= != ==
        self.cond_value = None # integer

