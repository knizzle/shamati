# Shamati
In Hebrew, the word *shamati* (שמעתי) means *I heard*.  
Kelsey's capstone project for PDX Code Guild, cohort Salmon.

### Project Overview
This project will attempt to help English speakers learn Hebrew. The user does NOT need to know how to read or write in Hebrew, though it would be beneficial to them in the long run. In my early Arabic-learning days, I would use the website [Fuzzy Arabic](http://fuzzyarabic.herokuapp.com/) as a tool to help me discover words that I had heard in Arabic, but did not know the meaning to, nor if I had even heard it correctly. Shamati takes a word or combination of sounds that the user hears/heard, typed phonetically in Latin script, and offers a list of possible Hebrew words. The list will include each word's meaning, root letters, transliteration, and part of speech. [Pealim](https://www.pealim.com/) is a Hebrew dictionary that gives the same output, however the user must know how to read/write in Hebrew script. 

### User Stories
1. As a **NON-ENGLISH SPEAKER**, I want the option to type in my own language, because I am more comfortable producing phonemes is my own script. 
* Dropdown options: Arabic, Russian, English (auto) (BACKLOG)
* For English/Latin script, create script converter- ***MVP #1***
2. As a **HEBREW LEARNER**, I want a tool that is simple and easy to use. No frills, no unnecessary styling and fluff - just basic input and output. Another nice feature would be to have the option to upload audio files of origin, or talk-to-text feature for those "it kinda sounded like ____" moments.
* Create 'fuzzy' match API - ***MVP #2*** -- UPDATE: regex
* Grab meaning from Pealim - ***MVP #3***
3. As **ANY USER**, I want word suggestions as I type, because I may not know what I heard fully, but I might recognize it if I saw it.
* Create autocomplete API - ***MVP #4*** (BACKLOG)
* Bind input text/autocomplete
4. As a **HEBREW TEACHER**, I want audio files and the ability to edit, in order to ensure accuracy, and so that my students don't have to unlearn something in the future. 
* Ability to add audio files/contribute to collaborative dictionary - ***MVP #5*** (BACKLOG)
5. As a **MOBILE USER**, I want a platform that is adjustable and easy to use on my mobile device, so that I can use it anywhere at anytime.
* CSS media queries
* Available offline (BACKLOG)

### Data Model
* Phoneme
* Hebrew Letter 
* Word

### Schedule 
###### 09 AUG, 2021: Proposal done
###### 13 AUG, 2021: MVP #1 done 
###### 17 AUG, 2021: MVP #2 done
###### 19 AUG, 2021: MVP #3 done
###### 24 AUG, 2021: Begin presentation practice
###### 27 AUG, 2021: Present to PDX Code Guild
