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
    if len(sys.argv) > 1:
        text_data = load_data(sys.argv[1])
        counter = get_most_frequent_words(text_data)
        print('Ten most popular words'.center(30, '='))
        for kw in counter.most_common()[0:10]:
            print(kw[0].ljust(15, '.'), str(kw[1]).rjust(15, '.'))
    else:
        print('You must specify the path to the text file!')
