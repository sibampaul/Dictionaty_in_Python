import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def dictionary(word):
    word = word.lower()
    if word in data.keys():
        print("%s means : \n" %word)
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        ch =input("Do you mean %s Y/N : " %get_close_matches(word,data.keys())[0])
        if ch == "Y" or ch == "y":
            print("%s means : \n" %word)
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "No such word exists in this Dictionary"
    else:
        return "No such word exists in this Dictionary"
def output():
    word = input("Enter the word : ")
    for items in dictionary(word):
        print(items)
    repeat()

def repeat():
    repeat= input("\nDo you want to continue Y/N : ")
    if repeat == 'Y' or repeat == 'y':
        output()
    else:
        pass
output()
