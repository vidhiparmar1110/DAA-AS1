comparisons = 0
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    sortedleft = merge_sort(lefthalf)
    sortedright = merge_sort(righthalf)

    return merge(sortedleft, sortedright)


def merge(left, right):
    global comparisons
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


array = [
    12.5, 3.2, 8.7, 1.4, 15.6,
    6.3, 9.8, 2.1, 11.9, 4.5,
    7.6, 14.2, 5.8, 10.3, 0.9
]

print("Original array:")
print(array)

sortedArray = merge_sort(array)

print("\nSorted array:")
print(sortedArray)
print("\nNumber of comparisons:", comparisons)
