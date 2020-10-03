def main():
    total_uni_count = 0
    total_bi_count = 0
    total_tri_count = 0
    unigrams = {}
    bigrams = {}
    trigrams = {}

    test_list = ["random list for testing", "testing purposes list",
                 "testing random list", "list for random testing",
                 "list for random testing purposes", "random list",
                 "random list for testing purposes", "done"]
    for item in test_list:
        words = item.split()
        for unigram in words:
            total_uni_count += 1
            if unigram in unigrams.keys():
                unigrams[unigram] += 1
            else:
                unigrams[unigram] = 1
        all_bigrams = zip(words, words[1:])
        for bigram in all_bigrams:
            total_bi_count += 1
            bigram = bigram[0] + "_" + bigram[1]
            if bigram in bigrams.keys():
                bigrams[bigram] += 1
            else:
                bigrams[bigram] = 1

        all_trigrams = zip(words, words[1:], words[2:])
        for trigram in all_trigrams:
            total_tri_count += 1
            trigram = trigram[0] + "_" + trigram[1] + "_" + trigram[2]
            if trigram in trigrams.keys():
                trigrams[trigram] += 1
            else:
                trigrams[trigram] = 1
    sorted_uni_counts = sorted(unigrams.items(),
                               key=lambda x: x[1],
                               reverse=True)
    print(sorted_uni_counts[:10])

    uni_freqs = [(item, round((count/total_uni_count), 3))
                 for (item, count) in sorted_uni_counts]
    print(uni_freqs[:10])

    sorted_bi_counts = sorted(bigrams.items(),
                              key=lambda x: x[1],
                              reverse=True)
    print(sorted_bi_counts[:10])
    bi_freqs = [(item, round((count/total_bi_count), 3))
                for (item, count) in sorted_bi_counts]
    print(bi_freqs[:10])

    sorted_tri_counts = sorted(trigrams.items(),
                               key=lambda x: x[1],
                               reverse=True)
    print(sorted_tri_counts[:10])
    tri_freqs = [(item, round((count/total_tri_count), 3))
                 for (item, count) in sorted_tri_counts]
    print(tri_freqs[:10])
    print("ha")
    print([uni_freqs[:3], bi_freqs[:3], tri_freqs[:3]])


main()
