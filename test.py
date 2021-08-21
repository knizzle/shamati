dictionary = {
    "א": ["", "a", "'", "o", "i"],
    "ב": ["v", "b", "bb"],
    # "בּ": ["v", "b", "bb"],
    "ג": ["g", "gg", "j", "zh"],
    "ד": ["d", "dd"],
    "ה": ["", "h", "eh", "ah", "a", "e", "ay", "ei", "ai", "ey"],
    "ו": ["v", "w", "oh", "o", "wu", "oo", "u", "ou", "oe", "ue"],
    # "וּּ": ["oo", "ou", "oe", "u", "ue"],
    "ז": ["z", "s", "zz", "ss"],
    "ח": ["ch", "h", "kh", "ach", "akh"],
    # "חַ": ["ach", "akh"],
    "ט": ["t", "tt", "th"],
    "י": ["y", "i", ""],
    "כ": ["ch", "h", "k", "c", "kk", "cc", "kh", "ck"],
    # "כּ": ["k", "c", "kk", "cc", "ck"],
    "ל": ["l", "ll"],
    "מ": ["m", "mm"],
    "נ": ["n", "nn"],
    "ס": ["s", "ss"],
    "ע": ["", "a", "i", "ee"],
    "פ": ["f", "ff", "ph", "p", "pp"],
    # "פּ": ["p", "pp"],
    "צ": ["ts", "tz", "s", "z", "izz", "tez"],
    "ק": ["k", "c", "kk", "cc", "q", "qq"],
    "ר": ["r", "rr"],
    # "שׁ": ["sh", "ss", "s", "ch", "sch"],
    "ש": ["s", "ss", "sh", "ch", "sch"],
    "ת": ["t", "tt", "th"],
    # "תּ": ["t", "tt", "th"],
    "יי": ["ai", "ay", "ey", "ei"],
    "יו": ["av", "ev"],
    "וו": ["w", "wu", "wa", "wo", "v", "ve", "va"],
    # "ָ": ["o", "oo", "oh", "a", "ah", "aa", "e", "ee", "i"],
    # "ַ": ["a", "o", "ah", "oh", ""],
    # "ֵ": ["e", "ei", "ey", "eh", "ay", "ai", ""],
    # "ֶ": ["e", "eh", "ei"],
    # "ִ": ["i", "e", "ee"],
    # "ֹ": ["o", "oh", "oi", "oy", "ey", "ow"],
    # "וֹ": ["o", "oh", "oi", "oy", "ey", "ow"],
    # "וּ": ["u", "oo", "i", "ee", "eu"],
    # "ֻ": ["u", "oo", "i", "ee", "eu"],
    # "ְ": ["u", "o", "e", "a", "i", "'"],
    "": ["a", "i", "e", "o", "h", "u", "y"]
}

# print(type(dictionary)) => dict

# 'shalom' -> ['sh','l','o','m'] -> ש ל ו מ = 
#   'שלום'


def heb_combos(user_entry):
    for letter in user_entry:
        keys = [key for key, value in dictionary.items() if letter in value]
        print(keys)

def last_letter(user_entry): 
    permutations = []
    for letter in user_entry:
        keys = [key for key, value in dictionary.items() if letter in value]
        permutations.append(keys)   
    if permutations[len(user_entry)-1] == ['מ']:
        return 'ם'
    elif permutations[len(user_entry)-1] == ['פ']:
        return 'ף'
    elif permutations[len(user_entry)-1] == ['כ']:
        return 'ך'
    elif permutations[len(user_entry)-1] == ['צ']:
        return 'ץ'
    elif permutations[len(user_entry)-1] == ['נ']:
        return 'ן'
    else:
        return -1

user_entry = 'rosh'

heb_combos(user_entry)
print(last_letter(user_entry))