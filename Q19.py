def fractional_knapsack(budget, investments):
    items = []

    for name, amount, return_value in investments:
        ratio = return_value / amount
        items.append((ratio, name, amount, return_value))

    items.sort(reverse=True)
    total_return = 0.0
    for ratio, name, amount, return_value in items:
        if budget >= amount:
            budget -= amount
            total_return += return_value
        else:
            fraction = budget / amount
            total_return += ratio * budget
            budget = 0
    return total_return

investments = [
    ("Project A", 20000, 30000),
    ("Project B", 10000, 18000),
    ("Project C", 30000, 36000),
    ("Project D", 15000, 21000)
]

budget = 40000
result = fractional_knapsack(budget, investments)
print("Maximum expected return:", result)
