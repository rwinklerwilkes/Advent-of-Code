##Day Four
def bad_phrase(phrase):
    s = phrase.split()
    s = sorted(s)
    dup = False
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            dup = True
    return dup

def bad_phrase_anagram(phrase):
    s = phrase.split()
    s = [''.join(sorted(word)) for word in s]
    s = sorted(s)
    dup = False
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            dup = True
    return dup

def good_passphrases(pass_input):
    ctr = 0
    for phrase in pass_input:
        if not bad_phrase(phrase):
            ctr += 1
    return ctr

def good_passphrases_anagram(pass_input):
    ctr = 0
    for phrase in pass_input:
        if not bad_phrase_anagram(phrase):
            ctr += 1
    return ctr

file = "Passphrase Input.txt"
passphrases = []
with open(file, 'r') as txtfile:
    for row in txtfile:
        passphrases.append(row.strip())


part_one = good_passphrases(passphrases)
part_two = good_passphrases_anagram(passphrases)
