"""Sorting Algorithms In Python
"""

"""
Dutch national flag problem
https://en.wikipedia.org/wiki/Dutch_national_flag_problem
"""


def sort_colors(nums: [int], pivot: int)->[int]:
    small = 0
    current = 1
    big = len(nums)-1
    while current < big:
        if nums[current] == pivot:
            current += 1
        elif nums[current] > pivot:
            nums[big], nums[current] = nums[current], nums[big]
            big -= 1
        else:
            nums[current], nums[small] = nums[small], nums[current]
            small += 1
            current += 1
    return nums


def quick_sort(numbers: list):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    left = [i for i in numbers[1:] if i <= pivot]
    right = [i for i in numbers[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
