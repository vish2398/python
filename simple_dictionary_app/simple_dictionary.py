import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        yn = yn.lower()
        if yn == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'n':
            return "The word doesn't exist.  Please double check it."
        else:
            return "You chose an invalid option."

    else:
        return "The word doesn't exist.  Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for num,item in enumerate(output, start=1):
        print("({}) {}".format(num, item))
else:
    print(output)
