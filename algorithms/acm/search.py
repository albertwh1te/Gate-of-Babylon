def topk(array, k):
    if len(array) == 1:
        return array[0]
    min_stack = sorted(array[:k])
    max_value = min_stack[k-1]
    for i in array[k:]:
        if i < max_value:
            min_stack.append(i)
            min_stack.remove(max(min_stack))
            max_value = max(min_stack)
    return min_stack
