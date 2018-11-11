"""Sorting Algorithms In Python
"""


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    left = [i for i in numbers[1:] if i <= pivot]
    right = [i for i in numbers[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
