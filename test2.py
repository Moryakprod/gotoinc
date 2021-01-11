from collections import Counter
import re


def most_common_words_in_text(text):
    word_list = []

    for word in re.split("[,.:; ()]", text):
        if word:
            word_list.append(word)

    if len(word_list) < 3:
        word_list.clear()
        print("меньше 3-х слов",  word_list)
    else:
        print(Counter(word_list).most_common(3))


text = input("Enter your text: ")
most_common_words_in_text(text)
