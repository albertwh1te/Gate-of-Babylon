a = [0]


def modify_array_fail(arr):
    arr = [1, 2, 3]


# this will fail
modify_array_fail(a)
print(a)


def modify_array_success(arr):
    arr[:] = [1, 2, 3]


# this will success
modify_array_success(a)
print(a)