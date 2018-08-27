"""Python implementataion of KMP
https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
"""


def kmp(s1: str, s2: str)->int:
    if s1 == None or s2 == None or len(s2) < 1 or len(s1) < len(s2):
        return -1
    pmt = find_pmt(s2)
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i = i + 1
            j = j + 1
        else:
            if pmt[j] == -1:
                i = i + 1
            else:
                j = pmt[j]

    if j == len(s2):
        # return the start index of substring
        return i - j
    else:
        # sadly we donot find it :(
        return -1


def find_pmt(s: str)->[int]:
    """
    input:string
    output:the partial match table of string
    """
    if len(s) == 1:
        return [-1]
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
    return result


def main():
    assert find_next("ab") == [-1, 0]
    test_str1 = "abcabc"
    assert find_next(test_str1) == [-1, 0, 0, 0, 1, 2]


if __name__ == '__main__':
    main()
