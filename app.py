import json
import difflib

data = json.load(open('data.json'))

def getDefinition(word):
    word = word.lower()
    similarWord = difflib.get_close_matches(word, data.keys(), cutoff=0.8)
    if word in data:
        return data[word]
    elif len(similarWord) > 0:
        answer = input('Did you mean %s? Press Y for Yes and N for No: ' %similarWord[0])
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            return data[similarWord[0]]
        else:
            return ['The word doesn\'t exits. Please check again.']
        # return f'Did you mean {similarWord[0]}?'
    else:
        return ['The word doesn\'t exits. Please check again.']

while True:
    word = input('Enter Word (To exit, type "\end"): ')
    if word == '\end':
        break
    else:
        word = getDefinition(word)
        for item in word:
            print("=>"+item)