def fractional_knapsack(capacity, weights, profits):
    n = len(profits)
    items = []

    for i in range(n):
        ratio = profits[i] / weights[i]
        items.append((ratio, profits[i], weights[i]))

    items.sort(reverse=True)
    total_profit = 0.0
    
    for ratio, profit, weight in items:
        if capacity >= weight:
            capacity -= weight
            total_profit += profit
        else:
            total_profit += ratio * capacity
            break
    return total_profit

profits = [40, 100, 120, 60]
weights = [5, 20, 30, 10]
capacity = 50
result = fractional_knapsack(capacity, weights, profits)
print("Maximum profit:", result)
