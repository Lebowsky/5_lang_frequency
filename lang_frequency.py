import sys
import string
from collections import Counter


def load_data(filepath):
    with open(filepath, encoding='utf-8') as f:
        return f.read()


def get_most_frequent_words(text_array):
    text_array = sorted(text_array.lower().translate(''.maketrans(
        '', '', string.punctuation)).split())
    counter = Counter()
    for word in text_array:
        counter[word] += 1
    return counter


if __name__ == '__main__':
    LENGTH_STRING = 30
    HALF_LENGTH_STRING = int(LENGTH_STRING/2)
    NUMBER_OF_WORDS = 10

    if len(sys.argv) > 1:
        text_data = load_data(sys.argv[1])
        counter = get_most_frequent_words(text_data)
        print('Ten most popular words'.center(LENGTH_STRING, '='))
        for kw in counter.most_common()[:NUMBER_OF_WORDS]:
            print(kw[0].ljust(HALF_LENGTH_STRING, '.'), str(kw[1]).rjust(HALF_LENGTH_STRING, '.'))
    else:
        print('You must specify the path to the text file!')
