def knapsack(w, val, wt):
    n = len(val)
    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for capacity in range(1, w + 1):
            if wt[i - 1] <= capacity:
                pick = val[i - 1] + dp[i - 1][capacity - wt[i - 1]]
                notPick = dp[i - 1][capacity]
                dp[i][capacity] = max(pick, notPick)
            else:
                dp[i][capacity] = dp[i - 1][capacity]

    print("DP Table:")
    for row in dp:
        print(row)
    return dp[n][w]
val = [1, 7, 11]
wt = [1, 2, 3]
w = 5
result = knapsack(w, val, wt)
print("\nMaximum value:", result)
