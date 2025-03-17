def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i, -1):
            print(j)
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


if __name__ == '__main__':
    arr = [5,6,8,9,2]
    print(bubble_sort(arr))