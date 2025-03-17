def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    print(selection_sort(arr))