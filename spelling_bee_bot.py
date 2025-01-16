import nltk
import nltk.corpus

words = nltk.corpus.words

def valid_dict(dictionary):
    valid = []
    for word in dictionary:
        if len(word)>=4:
            valid.append(word.lower())
    return valid

def save_dict(lines, filename):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(f"{line}\n")

def setup_procedure():
    dict_en = words.raw("en")
    print("dictionary successfully loaded")
    list_en = dict_en.split()
    print(f"{len(list_en)} words in dictionary")
    valid_en = valid_dict(list_en)
    print(f"{len(valid_en)} valid words")
    save_dict(valid_en,"valid_en.txt")

def possibleWords(center, outer, dict_file):
    """
    Takes in a string of the 6 outer letters, one center letter,
        and a filename for the dictionary to be used
    Outputs all possible valid words
    Criteria for a valid word:
    -found in an English dictionary
    -includes center letter
    -only uses letters in outer and center
    -at least 4 letters long

    """
    letters = set([*outer])
    letters.add(center)
    print(f"Today's letters are {letters}")
    dictionary = open(dict_file, "r")
    words = dictionary.read().split()
    #print(len(words))
    result = []
    pangrams = []
    for word in words:
        if center in word:
            sword = set([*word])
            if sword.issubset(letters):
                if letters == sword:
                    pangrams.append(word)
                else:
                    result.append(word)   

    return pangrams, result

def to_text(p, r):
    pangrams = sorted(p, key=len, reverse=True)
    others = sorted(r, key=len, reverse=True)
    text = "Today's Pangram(s):\n"
    for line in pangrams:
        text+=f"{line}\n"
    text+= "Other possible words:\n"
    for line in others:
        text+=f"{line}\n"    
    count = len(pangrams)+len(others)
    text += f"The maximun number of words today is {count}\n"
    print(text)
    
# # YOU ONLY NEED TO RUN SETUP ONCE
# setup_procedure()

yellow_letter = "i"
other_letters = "pzdtue"
dictionary = "valid_en.txt"

p, o = possibleWords(yellow_letter, other_letters, dictionary)
to_text(p,o)
