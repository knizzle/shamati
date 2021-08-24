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

def last_letter(user_entry): 
    letter_opts = []
    for letter in user_entry:
        keys = [key for key, value in dictionary.items() if letter in value]
        letter_opts.append(keys)
    print(letter_opts)
    word_combos = []
    i = 0
    for letter in letter_opts[i]:
        first_letter = letter
        word_combos.append(first_letter)
    for letter in letter_opts[i+1]:
        second_letter = letter
        word_combos = first_letter + second_letter
        if second_letter == '':
            pass
            print(word_combos)
    for letter in letter_opts[i+2]:
        third_letter = letter
        word_combos = first_letter + second_letter + third_letter
        if third_letter == '':
            pass
        else:
            print(word_combos)
    for letter in letter_opts[i+3]:
        fourth_letter = letter
        word_combos = first_letter + second_letter + third_letter + fourth_letter
        if fourth_letter == '':
            pass
        else:
            print(word_combos)
    for letter in letter_opts[i+4]:
        fifth_letter = letter
        word_combos = first_letter + second_letter + third_letter + fourth_letter + fifth_letter
        if fifth_letter == '':
            pass
        else:
            print(word_combos)
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

last_letter(['sh', 'a', 'l', 'o', 'm'])
# last_letter(['d', 'a', 'f'])