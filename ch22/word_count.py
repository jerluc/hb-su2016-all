import operator
import string


def _sanitize(words):
    cleansed = []
    for word in words:
        no_punc = word.strip(string.punctuation)
        cleansed.append(no_punc.lower())
    return cleansed


def count_words(filename):
    with open(filename) as f:
        contents = f.read()
        words = contents.split()
        cleansed_words = _sanitize(words)
        word_counts = {}
        for word in cleansed_words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
        return word_counts


def write_word_counts(word_counts, filename, sort_by_count=False):
    with open(filename, 'w') as f:
        if sort_by_count:
            sort_key = operator.itemgetter(1)
        else:
            sort_key = operator.itemgetter(0)

        sorted_word_counts = sorted(word_counts.items(), key=sort_key)

        for word, count in sorted_word_counts:
            f.write(word)
            f.write('\t')
            f.write(str(count))
            f.write('\n')


def main():
    word_counts = count_words('Loremipsum.txt')
    write_word_counts(word_counts, 'counts_by_word.txt')
    write_word_counts(word_counts, 'counts_by_count.txt', sort_by_count=True)


if __name__ == '__main__':
    main()
