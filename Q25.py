def knapsack_dp(capacity, values, weights):
    n = len(values)

    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    for i in range(1, n + 1):
        for current_capacity in range(1, capacity + 1):
            if weights[i - 1] <= current_capacity:
                pick = (values[i - 1] + dp[i - 1][current_capacity - weights[i - 1]])
                notPick = dp[i - 1][current_capacity]
                dp[i][current_capacity] = max(pick,notPick)
            else:
                dp[i][current_capacity] = (dp[i - 1][current_capacity])
    return dp[n][capacity]

def greedy_knapsack(capacity, values, weights):
    items = []

    for i in range(len(values)):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i]))

    items.sort(reverse=True)
    total_value = 0
    for ratio, value, weight in items:
        if weight <= capacity:
            capacity -= weight
            total_value += value
    return total_value

values = [100, 120, 60]
weights = [20, 30, 10]
capacity = 50
dp_result = knapsack_dp(capacity,values,weights)

greedy_result = greedy_knapsack(capacity,values,weights)
print("0/1 Knapsack using DP:", dp_result)
print("Greedy approach:", greedy_result)
