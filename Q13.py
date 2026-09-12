def activity_selection(start, finish):
    activities = list(zip(start, finish))
    activities.sort(key=lambda x: x[1])
    selected = []
    last_end = 0

    for s, f in activities:
        if s >= last_end:
            selected.append((s, f))
            last_end = f
    return selected

n = int(input("Enter number of activities: "))

start = []
finish = []

for i in range(n):
    print("\nActivity", i + 1)
    s = int(input("Enter start time: "))
    f = int(input("Enter finish time: "))
    start.append(s)
    finish.append(f)

result = activity_selection(start, finish)

print("\nSelected activities:")

for activity in result:
    print("Start:", activity[0], "Finish:", activity[1])

print("\nMaximum number of activities:", len(result))
