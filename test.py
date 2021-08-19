dictionary = {
    "א": ["", "a", "'"],
    "ב": ["v", "bb"],
    "בּ": ["v", "b", "bb"],
    "ג": ["g", "gg", "j", "zh"],
    "ד": ["d", "dd"],
    "ה": ["", "h", "eh", "ah", "a", "e", "ay", "ei", "ai", "ey"],
    "ו": ["v", "w", "oh", "o", "wu", "oo", "u"],
    "וּּ": ["oo", "ou", "oe", "u", "ue"],
    "ז": ["z", "s", "zz", "ss"],
    "ח": ["ch", "h", "kh"],
    "חַ": ["ach", "akh"],
    "ט": ["t", "tt", "th"],
    "י": ["y", "i", ""],
    "כ": ["ch", "h", "k", "c", "kk", "cc", "kh"],
    "כּ": ["k", "c", "kk", "cc", "ck"],
    "ל": ["l", "ll"],
    "מ": ["m", "mm"],
    "נ": ["n", "nn"],
    "ס": ["s", "ss"],
    "ע": ["", "a"],
    "פ": ["f", "ff", "ph", "p", "pp"],
    "פּ": ["p", "pp"],
    "צ": ["ts", "tz", "s", "z", "izz", "tez"],
    "ק": ["k", "c", "kk", "cc", "q", "qq"],
    "ר": ["r", "rr"],
    "שׁ": ["sh", "ss", "s", "ch", "sch"],
    "ש": ["s", "ss", "sh"],
    "ת": ["t", "tt", "th"],
    "תּ": ["t", "tt", "th"],
    "יי": ["ai", "ay", "ey", "ei"],
    "יו": ["av", "ev"],
    "וו": ["w", "wu", "wa", "wo", "v", "ve", "va"],
    "ָ": ["o", "oo", "oh", "a", "ah", "aa", "e", "ee", "i"],
    "ַ": ["a", "o", "ah", "oh", ""],
    "ֵ": ["e", "ei", "ey", "eh", "ay", "ai", ""],
    "ֶ": ["e", "eh", "ei"],
    "ִ": ["i", "e", "ee"],
    "ֹ": ["o", "oh", "oi", "oy", "ey", "ow"],
    "וֹ": ["o", "oh", "oi", "oy", "ey", "ow"],
    "וּ": ["u", "oo", "i", "ee", "eu"],
    "ֻ": ["u", "oo", "i", "ee", "eu"],
    "ְ": ["u", "o", "e", "a", "i", "'"]
}

# print(type(dictionary)) => dict

# 'shalom' -> ['sh','l','o','m'] -> ש ל ו מ = 
#   'שלום'

user_entry = 'shalom'

heb_word = ''

i = 0

for i in range(len(user_entry)):
    for letter in user_entry:
        heb_word += letter[i]
        print(heb_word)
        keys = [key for key, value in dictionary.items() if heb_word in value]
        if keys != []:
            print(keys)

    # if any consecutive combination of 3 letters matches a value in dict., print 'key' and append heb_word        
    # if any consecutive combination of 2 letters matches a value in dict., print 'key' and append
    # if >1 key, print/append all possible combos


# first = ''
# second = ''
# third = ''
# fourth = ''
# fifth = ''

'''
'm' yes
'om' no
'o' 'm' yes
'lom' no
'lo' 'm' yes
'l' 'o' 'm' yes
'alo' 'm' no
'al' 'o' 'm' no
'a' 'l' 'o' 'm' yes
'hal' 'o' 'm' no
'ha' 'l' 'o' 'm' yes
'h' 'a' 'l' 'o' 'm' yes
'sha' 'l' 'o' 'm' no
'sh' 'a' 'l' 'o' 'm' yes
's' 'h' 'a' 'l' 'o' 'm' yes

'''