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
        while i <= j and arr[i].lower() <= p.lower():
            i += 1
        while i <= j and arr[j].lower() >= p.lower():
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

text = "QUICKSORT"
characters = list(text)
print("Original string:", text)
quick_sort(characters, 0, len(characters) - 1)
sorted_string = "".join(characters)
print("Alphabetical order:", sorted_string)
