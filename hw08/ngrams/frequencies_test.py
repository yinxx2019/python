from ngram_frequencies import NgramFrequencies

# I created a random list for testing because corpse bride is too long
test_list = ["random list for testing", "testing purposes list",
             "testing random list", "list for random testing",
             "list for random testing purposes", "random list",
             "random list for testing purposes", "done"]


def test_init():
    '''test if value passed properly in init'''
    txt = "this is a random string for testing purposes only"
    ngram = NgramFrequencies(txt)
    assert ngram.clean_txt == txt


def test_add_item():
    '''test if add_item adds items to dictionaries'''
    ngram = NgramFrequencies(test_list)
    ngram.add_item()
    assert ngram.unigrams == {'random': 6, 'list': 7, 'for': 4, 'testing': 6,
                              'purposes': 3, 'done': 1}
    assert ngram.bigrams == {'random_list': 4, 'list_for': 4, 'for_testing': 2,
                             'testing_purposes': 3, 'purposes_list': 1,
                             'testing_random': 1, 'for_random': 2,
                             'random_testing': 2}
    assert ngram.trigrams == {'random_list_for': 2, 'list_for_testing': 2,
                              'testing_purposes_list': 1,
                              'testing_random_list': 1, 'list_for_random': 2,
                              'for_random_testing': 2,
                              'random_testing_purposes': 1,
                              'for_testing_purposes': 1}


def test_top_n_counts():
    '''test if top_n_counts generates N-length sorted list'''
    ngram = NgramFrequencies(test_list)
    N = 5
    ngram.add_item()
    ngram.top_n_counts(N)
    assert ngram.sorted_uni_counts[:N] == [('list', 7), ('random', 6),
                                           ('testing', 6), ('for', 4),
                                           ('purposes', 3)]
    assert ngram.sorted_bi_counts[:N] == [('random_list', 4), ('list_for', 4),
                                          ('testing_purposes', 3),
                                          ('for_testing', 2),
                                          ('for_random', 2)]
    assert ngram.sorted_tri_counts[:N] == [('random_list_for', 2),
                                           ('list_for_testing', 2),
                                           ('list_for_random', 2),
                                           ('for_random_testing', 2),
                                           ('testing_purposes_list', 1)]
    assert ngram.top_n_counts(N) == [[('list', 7), ('random', 6),
                                      ('testing', 6), ('for', 4),
                                      ('purposes', 3)],
                                     [('random_list', 4), ('list_for', 4),
                                      ('testing_purposes', 3),
                                      ('for_testing', 2),
                                      ('for_random', 2)],
                                     [('random_list_for', 2),
                                      ('list_for_testing', 2),
                                      ('list_for_random', 2),
                                      ('for_random_testing', 2),
                                      ('testing_purposes_list', 1)]]


def test_frequency_top_n_freqs():
    '''test if frequency takes an item and returns its frequency with a N list
       I test these two functions together for efficiency concern, otherwise
       it will have a lot of repetitions'''
    ngram = NgramFrequencies(test_list)
    N = 3
    ngram.add_item()
    ngram.top_n_counts(N)
    ngram.frequency()
    assert ngram.uni_freqs == [('list', 0.259), ('random', 0.222),
                               ('testing', 0.222), ('for', 0.148),
                               ('purposes', 0.111), ('done', 0.037)]
    assert ngram.bi_freqs == [('random_list', 0.211), ('list_for', 0.211),
                              ('testing_purposes', 0.158),
                              ('for_testing', 0.105), ('for_random', 0.105),
                              ('random_testing', 0.105),
                              ('purposes_list', 0.053),
                              ('testing_random', 0.053)]
    assert ngram.tri_freqs == [('random_list_for', 0.167),
                               ('list_for_testing', 0.167),
                               ('list_for_random', 0.167),
                               ('for_random_testing', 0.167),
                               ('testing_purposes_list', 0.083),
                               ('testing_random_list', 0.083),
                               ('random_testing_purposes', 0.083),
                               ('for_testing_purposes', 0.083)]
    assert ngram.top_n_freqs(N) == [[('list', 0.259), ('random', 0.222),
                                     ('testing', 0.222)],
                                    [('random_list', 0.211),
                                     ('list_for', 0.211),
                                     ('testing_purposes', 0.158)],
                                    [('random_list_for', 0.167),
                                     ('list_for_testing', 0.167),
                                     ('list_for_random', 0.167)]]
