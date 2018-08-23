from algorithms.acm.kmp import find_next


def test_find_next():
    assert find_next("ab") == [-1, 0]
    test_str1 = "abcabc"
    assert find_next(test_str1) == [-1, 0, 0, 0, 1, 2]
