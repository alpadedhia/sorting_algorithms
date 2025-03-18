def merge_sort(arr):
    if len(arr) > 1:
        return helper(arr, 0, len(arr) - 1)
    return arr


def helper(arr, start, end):
    if start == end:
        return [arr[start]]

    mid = (start + end) // 2
    left = helper(arr, start, mid)
    right = helper(arr, mid + 1, end)

    i, j = 0, 0
    aux = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            aux.append(left[i])
            i += 1
        else:
            aux.append(right[j])
            j += 1

    while i < len(left):
        aux.append(left[i])
        i += 1

    while j < len(right):
        aux.append(right[j])
        j += 1

    return aux


if __name__ == '__main__':
    print(merge_sort([5, 4, 3, 2, 1]))