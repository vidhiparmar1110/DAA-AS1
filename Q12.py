def activity_selection(start, finish):
    activities = list(zip(start, finish))
    activities.sort(key=lambda x: x[1])
    selected = []
    last_finish = 0
    for start_time, finish_time in activities:
        if start_time >= last_finish:
            selected.append((start_time, finish_time))
            last_finish = finish_time
    return selected

start = [2, 1, 3, 0, 5, 8, 5]
finish = [3, 4, 5, 6, 7, 9, 9]

selected = activity_selection(start, finish)

print("Given activities:")
for activity in zip(start, finish):
    print(activity)
print("\nSelected activities:")

for activity in selected:
    print(activity)
print("\nMaximum activities:", len(selected))
