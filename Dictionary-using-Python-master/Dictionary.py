import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead " % get_close_matches(word, data.keys())[0])
        choice=input("for continue press y or exit press n")
        if choice == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif choice == "n":
            print("Your choice is terminated")
    else:
        print("you chose wrong choice")
word = input( " Enter word for search in Dictionary:- ")
output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)