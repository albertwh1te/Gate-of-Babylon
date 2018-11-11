from random import randint
from algorithms.acm.sort import (
    quick_sort
)


def test_quick_sort():
    assert(quick_sort([])) == []

    array = [11, 2, 3, 4, 1, 7]
    assert(quick_sort(array)) == sorted(array)

    length = randint(1, 103)
    array = [randint(1, 1311) for i in range(length)]
    assert(quick_sort(array)) == sorted(array)
