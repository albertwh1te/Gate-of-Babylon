"""Test for lgb_util.py
TODO:
    test_split
    test_TrainTestValidation
    test_runLGB
"""
from random import randint
import pandas as pd
from algorithms.machinelearning import lgb_util


def test_split():
    """
    1. test if two DataFrame has similar distribution
    2. test if two DataFrame numbers are right
    """
    n = randint(9, 103)
    test_size = randint(1, 9) / 10
    X = pd.DataFrame([[randint(1, 42), randint(1, 42)] for _ in range(n)])
    y = pd.DataFrame([randint(0, 1) for _ in range(n - 4)] + [1, 1, 1, 1])
    X_train, y_train, X_test, y_test = lgb_util.split(X, y, test_size)
    # test priciple 1
    train_distr = sum(y_train[0]) / len(y_train)
    test_distr = sum(y_test[0]) / len(y_test)
    assert abs(train_distr - test_distr) < 0.5
    # test priciple 2


def test_TrainTestValidation():
    """
    test if tran test validation remain the similar distribution
    """
    pass
