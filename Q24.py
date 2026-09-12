def knapsack(capacity, values, weights):
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

projects = [
    ("Project A", 60, 10),
    ("Project B", 100, 20),
    ("Project C", 120, 30),
    ("Project D", 80, 15)
]

values = []
weights = []

for name, value, weight in projects:
    values.append(value)
    weights.append(weight)

capacity = 50
result = knapsack(capacity, values, weights)
print("Maximum resource allocation benefit:", result)
