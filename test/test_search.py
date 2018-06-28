from random import randint
from algorithms.acm import search


def test_topk():
    array = [randint(1, 1000) for i in range(11, 200)]
    k = randint(1, 10)
    print(sorted(array)[:k], k, array)
    assert sorted(array)[:k] == sorted(search.topk_min_stack(array, k))
    assert sorted(array)[:k] == sorted(search.topk_quick(array, k))
    # make code coverage 100%
    assert [1] == search.topk_min_stack([1], 100)
    assert [1] == search.topk_quick([1], 100)
