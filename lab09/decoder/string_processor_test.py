from string_processor import StringProcessor


def test_process_string():
    """Test for process_string function"""
    sp = StringProcessor()
    # Include the following cases
    # "ab" should yield "" as ouptut
    assert sp.process_string("ab") == ""
    # "ab*" should yield "b" as output
    sp = StringProcessor()
    assert sp.process_string("ab*") == "b"
    # "ab^" should yield "ba" as output
    sp = StringProcessor()
    assert sp.process_string("ab^") == "ba"
    # "^" should yield "" as output
    sp = StringProcessor()
    assert sp.process_string("^") == ""
