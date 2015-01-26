#!/usr/bin/python

def censor(text, word):
    fill = "*" * len(word)
    words = text.split()
    censored = []
    for each in words:
        if each == word:
            censored.append(fill)
        else:
            censored.append(each)
    censored = " ".join(censored)
    return censored

print censor("This is a hack and it sucks", "hack")

