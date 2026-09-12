def fractional_knapsack(capacity, weights, values):
    n = len(values)
    items = []

    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i], i + 1))

    items.sort(reverse=True)
    total_value = 0.0
    print("Items sorted by value/weight ratio:")

    for ratio, value, weight, item_no in items:
        print("Item", item_no,"Weight:", weight,"Value:", value,"Ratio:", ratio)
    print("\nSelection:")

    for ratio, value, weight, item_no in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
            print("Item", item_no, ": Full item taken")
        else:
            fraction = capacity / weight
            total_value += ratio * capacity
            print("Item", item_no,":", fraction,"of item taken")
            capacity = 0
            break
    return total_value

weights = [10, 20, 30, 40]
values = [60, 100, 120, 160]
capacity = 50
result = fractional_knapsack(capacity, weights, values)
print("\nMaximum value:", result)
