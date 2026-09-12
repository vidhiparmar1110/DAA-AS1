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
        if left[i][2] < right[j][2]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


employees = [
    (101, "Rahul", 55000),
    (102, "Priya", 72000),
    (103, "Amit", 48000),
    (104, "Neha", 65000),
    (105, "Karan", 90000),
    (106, "Sneha", 58000)
]

print("Original employee records:")

for employee in employees:
    print(employee)

sortedEmployees = merge_sort(employees)

print("\nEmployees sorted by salary:")

for employee in sortedEmployees:
    print(employee)
