import sys
import string
from collections import Counter


def load_data(filepath):
    with open(filepath, encoding='utf-8') as data:
        return data.read()


def get_most_frequent_words(text_array):
    text_array = sorted(
        text_array.lower().translate(''.maketrans(
            '',
            '',
            string.punctuation)
        ).split(),
    )
    counter = Counter(text_array)
    return counter


if __name__ == '__main__':
    length_string = 30
    half_length_string = int(length_string/2)
    number_of_words = 10

    if len(sys.argv) > 1:
        text_data = load_data(sys.argv[1])
        counter = get_most_frequent_words(text_data)
        print('Ten most popular words'.center(length_string, '='))
        for kw in counter.most_common(number_of_words):
            word, count = kw
            print(
                word.ljust(half_length_string, '.'),
                str(count).rjust(half_length_string, '.')
            )
    else:
        print('You must specify the path to the text file!')
