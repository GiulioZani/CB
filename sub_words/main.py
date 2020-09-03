from urllib.request import urlopen
from re import split
from sys import argv


def count(char, w1):
    res = []
    for c1 in w1:
        if c1 == char:
            res.append(c1)
    return len(res)


def contains(w1, w2):
    done = []
    for char in w1:
        if char not in done:
            count1 = count(char, w1)
            count2 = count(char, w2)
            done.append(char)
            if count1 != count2:
                return False
    return True


def main():
    file_name = argv[1]
    word = argv[2]
    text = ''
    if file_name.startswith('http://') or file_name.startswith('https://'):
        text = urlopen(file_name).lower()
    else:
        text = open(file_name).read().lower()
    words = split('[^a-z]+', text)

    result = []
    for w_candidate in words:
        if contains(word, w_candidate):
            result.append(w_candidate)
    print(result)


if __name__ == '__main__':
    main()
