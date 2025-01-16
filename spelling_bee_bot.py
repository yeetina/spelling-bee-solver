import nltk
import nltk.corpus


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

def setup_procedure(nltk_dict, filename):
    words = nltk.corpus.words
    dict_en = words.raw(nltk_dict)
    print("dictionary successfully loaded")
    list_en = dict_en.split()
    print(f"{len(list_en)} words in dictionary")
    valid_en = valid_dict(list_en)
    print(f"{len(valid_en)} valid words")
    save_dict(valid_en,filename)

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
    print(f" \nToday's letters are {letters}\n")
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

def to_text(p, o):
    pangrams = list(set(p))
    others = list(set(o))
    pangrams = sorted(pangrams, key=len, reverse=True)
    others = sorted(others, key=len, reverse=True)
    
    text = "Today's Pangram(s):\n"
    for line in pangrams:
        text+=f"{line}\n"
    text+= "\nOther possible words:\n"
    for line in others:
        text+=f"{line}\n"    
    count = len(pangrams)+len(others)
    text += f"Spelling Bee Bot found {count} words.\n"
    print(text)
    

yellow_letter = input("What is the center letter? ").lower()
other_letters = input("Enter the other letters in any order: ").lower()
dictionary = "valid_en.txt"

# # ONLY RUN SETUP IF YOU WANT TO CHANGE OR ADD A NEW DICTIONARY
# setup_procedure("en", dictionary)

p, o = possibleWords(yellow_letter, other_letters, dictionary)
to_text(p,o)
