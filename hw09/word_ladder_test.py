from word_ladder import WordLadder


def test_make_ladder():
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                # Add to an existing set
                valid_words[len(w)].add(w)
            else:
                # Initialize a set with one element
                valid_words[len(w)] = {w}
    wl = WordLadder("cat", "hat", valid_words[len("cat")])
    assert wl.make_ladder().items[0] == "cat"
    wl = WordLadder("love", "hate", valid_words[len("love")])
    assert wl.make_ladder().items[-1] == "hate"
    wl = WordLadder("data", "code", valid_words[len("data")])
    assert len(wl.make_ladder().items) == 5
    wl = WordLadder("angel", "devil", valid_words[len("angel")])
    assert "anger" in wl.make_ladder().items
