"""Test for model_util.py
"""
from random import randint
import pandas as pd
from algorithms.machinelearning import model_util


def test_split():
    """
    1. test if two DataFrame has similar distribution
    2. test if two DataFrame sum numbers
    """
    n = randint(79, 103)
    test_size = randint(1, 9) / 10
    X = pd.DataFrame([[randint(1, 42), randint(1, 42)] for _ in range(n)])
    y = pd.DataFrame([randint(0, 1) for _ in range(n - 4)] + [1, 1, 1, 1])
    X_train, y_train, X_test, y_test = model_util.split(X, y, test_size)
    # test priciple 1
    train_distr = sum(y_train[0]) / len(y_train)
    test_distr = sum(y_test[0]) / len(y_test)
    assert abs(train_distr - test_distr) < 0.5
    # test priciple 2
    assert len(y_test) + len(y_train) == n


def test_TrainTestValidation():
    """
    1. test if tran test validation remain the similar distribution
    2. test if tran test validation sum numbers
    3. test if tran test validation ratio numbers
    """
    n = randint(79, 103)
    X = pd.DataFrame([[randint(1, 42), randint(1, 42)] for _ in range(n)])
    y = pd.DataFrame([randint(0, 1) for _ in range(n - 4)] + [1, 1, 1, 1])
    X_train, y_train, X_test, y_test, X_val, y_val =\
        model_util.TrainTestValidation(X, y)
    train_distr = sum(y_train[0]) / len(y_train)
    test_distr = sum(y_test[0]) / len(y_test)
    val_distr = sum(y_val[0]) / len(y_val)
    # test 1
    assert abs(train_distr - test_distr) < 0.5
    assert abs(train_distr - val_distr) < 0.5
    assert abs(val_distr - test_distr) < 0.5
    # test 2
    assert len(y_test) + len(y_train) + len(y_val) == n
    # test 3
    test_ration = len(y_test) / n
    assert abs(test_ration - 0.2) < 0.1
    val_ration = len(y_val) / (len(y_train) + len(y_val))
    assert abs(val_ration - 0.2) < 0.1
