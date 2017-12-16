f = open('day-4-input.txt')
d = f.read()
f.close()

passphrases = d.split('\n')

def validate_passphrase(p):
    if len(p) < 1:
        return False

    words = p.split(' ')
    word_set = set(words)
    return len(words) == len(word_set)

def sum_valid(count, phrase):
    if validate_passphrase(phrase):
        return count + 1
    return count


num_valid_phrases = reduce(sum_valid, passphrases, 0)

print("Of %d pass phrases, %d are valid" % (len(passphrases), num_valid_phrases))
