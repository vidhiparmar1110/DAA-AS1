def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

prices = [499.99, 1299.50, 799.00, 249.75, 999.99, 149.50, 599.25]
print("Original prices:", prices)
quick_sort(prices, 0, len(prices) - 1)
print("Sorted prices:", prices)
