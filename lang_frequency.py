import sys
import string
from collections import Counter


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file:
        return file.read()


def get_most_frequent_words(text, number_of_words):
    text_list = text.lower().translate(''.maketrans(
            '',
            '',
            string.punctuation),
        ).split()
    counter = Counter(text_list)
    return counter.most_common(number_of_words)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        length_string = 30
        half_length_string = int(length_string / 2)
        number_of_words = 10

        text = load_data(sys.argv[1])
        words_list = get_most_frequent_words(text, number_of_words)
        print('Ten most popular words'.center(length_string, '='))
        for word, count in words_list:
            print(
                word.ljust(half_length_string, '.'),
                str(count).rjust(half_length_string, '.')
            )
    else:
        print('You must specify the path to the text file!')
