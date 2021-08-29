# Shamati
- *shamati* (שמעתי) means *I heard* in Hebrew 
- Capstone project for PDX Code Guild

### Project Overview
This project will attempt to help English speakers learn Hebrew. The user does NOT need to know how to read or write in Hebrew, though it would be beneficial to them in the long run. In my early Arabic-learning days, I would use the website [Fuzzy Arabic](http://fuzzyarabic.herokuapp.com/) as a tool to help me discover words that I had heard in Arabic, but did not know the meaning to, nor if I had even heard it correctly. Shamati takes a word or combination of sounds that the user hears/heard, typed phonetically in Latin script, and offers a list of possible Hebrew words. The list will include each word's meaning, root letters, transliteration, and part of speech.

### User Stories
1. **NON-ENGLISH SPEAKER**
* Dropdown options: Arabic, Russian, English (auto) (BACKLOG)
2. **HEBREW LEARNER**
* For English/Latin script, create script converter ***MVP #1***
* Find words in dictionary and list on page ***MVP #2***
* I want a sound byte to hear how the Hebrew words sound, and to verify what I think I heard (BACKLOG)
3. **ANY USER**
* Create autocomplete API (BACKLOG)
* Bind input text/autocomplete
4. **HEBREW TEACHER**
* Ability to add audio files, and correct/contribute to a collaborative dictionary (BACKLOG)
5. **MOBILE USER**
* CSS media queries
* Available offline (BACKLOG)

### Data Model
* Phoneme
* Hebrew Letter 
* Word
