"""Python implementataion of KMP
https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
"""


def find_next(s: str)->[int]:
    """
    input:string
    output:the next array of string
    """
    result = [0 for i in range(len(s))]
    result[0] = -1
    result[1] = 0
    i = 2
    cn = 0
    while i < len(result):
        if s[i-1] == s[cn]:
            cn += 1
            result[i] = cn
        elif cn > 0:
            cn = result[cn]
        else:
            result[i+1] = 0
        i = i + 1
    print(result)
    return result


def main():
    assert find_next("ab") == [-1, 0]
    test_str1 = "abcabc"
    assert find_next(test_str1) == [-1, 0, 0, 0, 1, 2]


if __name__ == '__main__':
    main()
