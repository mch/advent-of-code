# Grammar
# group = "{" ( group | garbage )* "}"
# garbage = "<" ( "!" . | . )* ">"
# . = any character

def garbage(index, stream):
    while index < len(stream):
        c = stream[index]
        if c == "!":
            index += 2
        elif c != ">":
            index += 1
        elif c == ">":
            break

    return index + 1

def group(index, stream, score):
    total_score = score
    while index < len(stream):
        c = stream[index]
        if c == "{":
            index, nested_score = group(index + 1, stream, score + 1)
            total_score += nested_score
        elif c == "<":
            index = garbage(index + 1, stream)
        elif c == ",":
            index += 1
        elif c == "}":
            break
        else:
            print("Invalid character in group at position %d" % (index,))
            break

    return index + 1, total_score


def day9(stream):
    index, score = group(0, stream, 0)
    return score

def check_equal(f, args, expected):
    actual = f(*args)
    if actual == expected:
        print("Ok")
    else:
        print("Fail: f(%s) == '%s', != expected value: '%s'" % (str(args), str(actual), str(expected)))

check_equal(day9, ["{}"], 1)
check_equal(day9, ["{{{}}}"], 6)
check_equal(day9, ["{{},{}}"], 5)
check_equal(day9, ["{{{},{},{{}}}}"], 16)
check_equal(day9, ["{<a>,<a>,<a>,<a>}"], 1)
check_equal(day9, ["{{<ab>},{<ab>},{<ab>},{<ab>}}"], 9)
check_equal(day9, ["{{<!!>},{<!!>},{<!!>},{<!!>}}"], 9)
check_equal(day9, ["{{<a!>},{<a!>},{<a!>},{<ab>}}"], 3)

def main():
    f = open('day-9-input.txt')
    d = f.read()
    f.close()
    score = day9(d)
    print("Puzzle result: %d" % (score,))

if __name__ == "__main__":
    main()

