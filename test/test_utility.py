import os
from random import randint
import py

TESTNUM = randint(1, 100)
FILENAMES = ["testfiles{x}.csv".format(x=x) for x in range(1, TESTNUM)]
PATH = os.getcwd()


def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    for f in FILENAMES:
        f = open(f, "a+")
        f.write("test,1,2")
        f.close()


def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    for f in FILENAMES:
        os.remove(PATH + f)


def test_dir2df():
    # check part
    df_list = py.utility.dir2df(PATH)
    assert len(df_list) == len(filenames)
