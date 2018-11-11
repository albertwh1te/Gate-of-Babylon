from random import randint
from algorithms.acm.sort import (
    quick_sort,
    sort_colors
)


def test_quick_sort():
    assert(quick_sort([])) == []

    array = [11, 2, 3, 4, 1, 7]
    assert(quick_sort(array)) == sorted(array)

    length = randint(1, 103)
    array = [randint(1, 1311) for i in range(length)]
    assert(quick_sort(array)) == sorted(array)


def test_sort_colors():
    # test case 1
    assert(sort_colors([], 0) == [])
    # test case 2
    array = [11, 2, 3, 4, 1, 7]
    pivot = 2
    result = sort_colors(array, pivot)
    p_index = result.index(pivot)
    for i, v in enumerate(result):
        if v > pivot:
            print(v, i)
            assert(i > p_index)
        elif v < pivot:
            assert(i < p_index)

    # test case 3
    array = [11, 2, 3, 4, 4, 1, 7]
    pivot = 4
    result = sort_colors(array, pivot)
    p_index = result.index(pivot)
    for i, v in enumerate(result):
        if v > pivot:
            print(v, i)
            assert(i > p_index)
        elif v < pivot:
            assert(i < p_index)
