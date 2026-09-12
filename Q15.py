def activity_selection(meetings):
    meetings.sort(key=lambda x: x[2])

    selected = []
    last_end = 0

    for name, start, finish in meetings:
        if start >= last_end:
            selected.append((name, start, finish))
            last_end = finish
    return selected

meetings = [
    ("Meeting A", 9, 10),
    ("Meeting B", 9, 11),
    ("Meeting C", 10, 12),
    ("Meeting D", 11, 13),
    ("Meeting E", 12, 14),
    ("Meeting F", 13, 15),
    ("Meeting G", 14, 16)
]

selected = activity_selection(meetings)

print("Selected meetings:")

for name, start, finish in selected:
    print(name, ":", start, "-", finish)
print("\nMaximum number of meetings:", len(selected))
