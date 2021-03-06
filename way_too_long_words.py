#!/usr/bin/env python3

def way_too_long_words(word):
    length = len(word)
    if length <= 10:
        return word
    else:
        return word[0]+str(length - 2)+word[length - 1]

if __name__ == "__main__":
    for _ in range(int(input())):
        word = input()
        print(way_too_long_words(word))
