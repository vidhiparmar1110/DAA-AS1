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
    return dp[n][w]


n = int(input("Enter number of items: "))
val = []
wt = []

for i in range(n):
    print("\nItem", i + 1)
    value = int(input("Enter value: "))
    weight = int(input("Enter weight: "))
    val.append(value)
    wt.append(weight)

w = int(input("\nEnter knapsack capacity: "))
result = knapsack(w, val, wt)
print("\nMaximum profit:", result)
