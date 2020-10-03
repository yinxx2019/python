from bracket_match import BracketMatch


def test_brackets_match():
    """Test brackets_match method"""
    bm = BracketMatch()
    # Include the following cases in your test:
    # "()" should succeed
    assert bm.brackets_match("()") is True
    # "a(a[a])a({a})" should succeed
    assert bm.brackets_match("a(a[a])a({a})") is True
    # "(" should not succeed
    assert bm.brackets_match("(") is False
    # "(}" should not succeed
    assert bm.brackets_match("(}") is False
    # "a(a(a)a(a)" should not succeed
    assert bm.brackets_match("a(a(a)a(a)") is False
    # "aa(a))a(a)" should not succeed
    assert bm.brackets_match("aa(a))a(a)") is False
