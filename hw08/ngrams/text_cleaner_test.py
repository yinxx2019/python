from text_cleaner import TextCleaner


def test_init():
    '''test if text cleaner opens file properly'''
    f = open("corpse_bride.txt", encoding="utf8")
    tc = TextCleaner(f)
    assert tc.f == f
    return tc


def test_format():
    '''test if format method converts the text properly'''
    op = test_init()
    COMMA_SIGN = ","
    COMMA = "COMMA"
    MR = "mr."
    PERIOD = "."
    punctuations = ["\"", "(", ")"]
    # test items in list - the entire list is too long!
    item_0 = "it's a dead scene COMMA but that's a good thing\n"
    assert op.format()[0] == item_0
    assert COMMA in op.format()[7]
    # check words in each sentence
    for i in op.format():
        assert COMMA_SIGN not in i  # all "," should have been converted
        assert MR not in i  # all prefixes should have been converted
        assert PERIOD not in i  # all "." should have been converted / splited
        for mark in punctuations:
            assert mark not in i  # they should have been converted
