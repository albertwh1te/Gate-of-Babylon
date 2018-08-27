from algorithms.acm.kmp import find_next, kmp, bruteforce_match


def test_find_next():
    assert find_next("a") == [-1]
    assert find_next("ab") == [-1, 0]
    test_str1 = "abcabc"
    assert find_next(test_str1) == [-1, 0, 0, 0, 1, 2]


def test_kmp():
    assert kmp("", "") == -1
    s1 = "abcabc"
    s2 = "bc"
    assert kmp(s1, s2) == s1.find(s2)


def test_bruteforce_match():
    assert bruteforce_match("", "") == -1
    s1 = "abcabc"
    s2 = "bc"
    assert bruteforce_match(s1, s2) == s1.find(s2)
