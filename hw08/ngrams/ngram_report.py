from text_cleaner import TextCleaner
from ngram_frequencies import NgramFrequencies


def main():
    '''read the file and process by calling methods'''
    file_name = "corpse_bride.txt"
    global N  # so that N can be called in print_output()
    N = 10
    # open the file
    try:
        f = open(file_name, encoding="utf8")
    except Exception:
        print("Can't open corpse_bride.txt")
        return
    # handle TextCleaner class
    clean = TextCleaner(f)
    # handle NgramFrequencies class
    ngram = NgramFrequencies(clean.format())
    ngram.add_item()
    ngram.top_n_counts(N)
    ngram.frequency()
    # call print_output
    print_output(ngram.top_n_freqs(N))


def print_output(collection):
    '''formatting print output'''
    print("Top", N, "unigrams:")
    for item in collection[0]:
        print("\t", item)
    print("Top", N, "bigrams:")
    for item in collection[1]:
        print("\t", item)
    print("Top", N, "trigrams:")
    for item in collection[2]:
        print("\t", item)


main()
