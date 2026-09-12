def activity_selection(classes):
    classes.sort(key=lambda x: x[2])
    selected = []
    last_end = 0
    for name, start, finish in classes:
        if start >= last_end:
            selected.append((name, start, finish))
            last_end = finish
    return selected

classes = [
    ("Math", 9, 10),
    ("English", 10, 11),
    ("Physics", 9, 12),
    ("Chemistry", 11, 12),
    ("Computer", 12, 1),
    ("Biology", 1, 2)
]

selected = activity_selection(classes)

print("Selected classes:")

for name, start, finish in selected:
    print(name, ":", start, "-", finish)

print("\nMaximum number of classes:", len(selected))
