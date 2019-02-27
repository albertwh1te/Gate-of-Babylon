from random import choice


def topk_min_stack(array, k):
    if len(array) <= k:
        return array
    min_stack = sorted(array[:k])
    max_value = min_stack[k - 1]
    for i in array[k:]:
        if i < max_value:
            min_stack.append(i)
            min_stack.remove(max(min_stack))
            max_value = max(min_stack)
    return min_stack


def topk_quick(array, k):
    if len(array) <= k:
        return array
    if k == 1:
        return [min(array)]
    pivot = choice(array)
    left = []
    right = []
    for i in array:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    if len(left) < k:
        return left + topk_quick(right, k - len(left))
    if len(left) >= k:
        return topk_quick(left, k)


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        print(mid, left, right, left + ((right - left) >> 1))
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 20, 500, 2000]
    target = 3
    print(binary_search(nums, target))
