import json
import time

words = []

with open('bad_words.txt', encoding='utf-8') as file:
    for word in file.read().split(', '):
        if word != '':
            words.append(word.replace('\n', '').replace('.', '').lower())

with open('bad_words.json', 'w', encoding='utf-8') as file_json:
    json.dump(words, file_json)

