blocks_per_bank = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]

def check_equal(actual, expected):
    if actual == expected:
        print("ok, got expected %s" % (str(expected)))
    else:
        print("fail, expected %s, got %s" % (str(expected), str(actual)))
        raise Exception()

def find_bank_with_most_blocks(blocks_per_bank):
    indexed_bpb = zip(xrange(len(blocks_per_bank)), blocks_per_bank)
    result = reduce(lambda x, y: x if x[1] >= y[1] else y, indexed_bpb)
    return result[0]

def realloc(blocks_per_bank):
    bank_to_redistribute = find_bank_with_most_blocks(blocks_per_bank)
    num_blocks = blocks_per_bank[bank_to_redistribute]
    blocks_per_bank[bank_to_redistribute] = 0

    num_banks = len(blocks_per_bank)
    bank = (bank_to_redistribute + 1) % num_banks

    while num_blocks > 0:
        blocks_per_bank[bank] += 1
        num_blocks -= 1
        bank = (bank + 1) % num_banks

    return blocks_per_bank

def redistribution_cycles(blocks_per_bank):
    configurations = set()
    configurations.add(str(blocks_per_bank))

    count = 0
    while True:
        blocks_per_bank = realloc(blocks_per_bank)
        count += 1

        sbpb = str(blocks_per_bank)
        if sbpb in configurations:
            break

        configurations.add(sbpb)

    return count

check_equal(find_bank_with_most_blocks([0, 2, 7, 0]), 2)
bpb = realloc([0, 2, 7, 0])
check_equal(bpb, [2, 4, 1, 2])
check_equal(redistribution_cycles([0, 2, 7, 0]), 5)

print("Num cycles: %d" % (redistribution_cycles(blocks_per_bank),))
