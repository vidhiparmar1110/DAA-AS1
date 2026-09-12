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
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].lower() < right[j].lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


students = ["Rahul","Amit","Priya","Neha","Karan","Sneha","Vivek","Anjali"]

print("Original names:", students)
sortedStudents = merge_sort(students)
print("Alphabetical order:", sortedStudents)
