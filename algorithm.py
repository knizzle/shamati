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
    "וו": ["w", "wu", "wa", "wo", "v", "ve", "va"],
    "": ["a", "i", "e", "o", "h", "u", "y"]
}

def keys(user_entry):
    word = [user_entry[i:j] for i, j in itertools.combinations(range(len(user_entry)+1),2)]
    combos = sorted(word, key=len, reverse=True)
    i = 0
    for combo in combos:
        keys = [key for key, value in dictionary.items() if combo in value]
        print(combos[len(keys)-1])
        if keys == []:
            pass
        else:
            print(keys)
            # for key in keys:
            #     if key == '':
            #         pass
            #     else: 
            #         print(key)


def last_letter(user_entry): 
    letter_opts = []
    for letter in user_entry:
        keys = [key for key, value in dictionary.items() if letter in value]
        letter_opts.append(keys)
        return letter_opts[len(letter_opts)-1]  
    if letter_opts[len(user_entry)-1] == ['מ']:
        return 'ם'
    elif letter_opts[len(user_entry)-1] == ['פ']:
        return 'ף'
    elif letter_opts[len(user_entry)-1] == ['כ']:
        return 'ך'
    elif letter_opts[len(user_entry)-1] == ['צ']:
        return 'ץ'
    elif letter_opts[len(user_entry)-1] == ['נ']:
        return 'ן'
    else:
        return -1

'''

user submits list of phonemes
each phoneme has Hebrew letter (key) that matches its value
each phoneme in user entry is list of keys
first list == first letter
second list == second letter
third list == third letter
etc.
if letter in list is '', skip
need combination of all letters, but still in list order

['a','']
['b','c','d','']
['e','f']

==

abe,
abf,
ace,
acf,
ade,
adf,
ae,
af,
be,
bf,
ce,
cf,
de,
df,
e,
f

'''