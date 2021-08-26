import itertools

dictionary = {
    "א": ["", "a", "'", "o", "i"],
    "ב": ["v", "b"],
    "ג": ["g", "j", "zh"],
    "ד": ["d"],
    "ה": ["", "h", "eh", "ah", "a", "e", "ay", "ei", "ai", "ey"],
    "ו": ["v", "w", "oh", "o", "wu", "oo", "u", "ou", "oe", "ue"],
    "ז": ["z", "s"],
    "ח": ["ch", "h", "kh", "ach", "akh"],
    "ט": ["t", "th"],
    "י": ["y", "i", "", "e"],
    "כ": ["ch", "h", "k", "c", "kh", "ck"],
    "ל": ["l"],
    "מ": ["m"],
    "נ": ["n"],
    "ס": ["s"],
    "ע": ["", "a", "i", "ee"],
    "פ": ["f", "ph", "p"],
    "צ": ["ts", "tz", "s", "z", "izz", "tez"],
    "ק": ["k", "c", "q"],
    "ר": ["r"],
    "ש": ["s", "sh", "ch", "sch"],
    "ת": ["t", "th"],
    "יי": ["ai", "ay", "ey", "ei"],
    "יו": ["av", "ev"],
    "וו": ["w", "wu", "wa", "wo", "v", "ve", "va", "vu"],
    "": ["a", "i", "e", "o", "h", "u", "y"]
}

def last_letter(user_entry): 
    letter_opts = []
    for letter in user_entry:
        keys = [key for key, value in dictionary.items() if letter in value]
        letter_opts.append(keys)
    print(letter_opts)
    if letter_opts[len(user_entry)-1] == ['מ']:
        print('ם')
    elif letter_opts[len(user_entry)-1] == ['פ']:
        print('ף')
    elif letter_opts[len(user_entry)-1] == ['כ']:
        print('ך')
    elif letter_opts[len(user_entry)-1] == ['צ']:
        print('ץ')
    elif letter_opts[len(user_entry)-1] == ['נ']:
        print('ן')
    else:
        print(-1)

# last_letter(['sh', 'a', 'l', 'o', 'm'])
# last_letter(['d', 'a', 'f'])


def heb_keys(user_entry): 
    for letter in user_entry:
        keys = [key for key, value in dictionary.items() if letter in value]
        return keys

heb_keys(['d', 'a', 'f'])
# heb_keys(['h', 'ai', 'm'])

keys = [['ד'], ['א', 'ה', 'ע', ''], ['ף']]


def word_combos(keys):
    words = list(itertools.product(*keys))
    for word in words:
        word = ''.join(word)
        print(word)

word_combos(keys)

'''
דאף
דהף
דעף
דף

'''