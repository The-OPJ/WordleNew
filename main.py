import random


def get_word():
    file = open("words.txt", "r")
    word_list = []
    for line in file:
        line = line[0:line.index(",")]
        if len(line) == 5 and line[-1] != "s":
            word_list.append(line)
    file.close()
    secret = word_list[random.randint(0, len(word_list) - 1)]
    return secret

def ask_word():


def compare_word(word):

secret = get_word()

