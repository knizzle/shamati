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

def combo_objs(user_entry):
    word = [user_entry[i:j] for i, j in itertools.combinations(range(len(user_entry)+1),2)]
    combos = sorted(word, key=len, reverse=True)
    print(combos)
    for combo in combos:
        keys = [key for key, value in dictionary.items() if combo in value]
        if keys == []:
            pass
        else:
            print(keys)       
    
            
            
combo_objs('mushlam') 


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

