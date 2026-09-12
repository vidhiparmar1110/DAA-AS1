mc = [[-1 for n in range(50)] for m in range(50)]

def DynamicProgramming(c, i, j):
    if i == j:
        return 0

    if mc[i][j] != -1:
        return mc[i][j]

    mc[i][j] = 999999

    for k in range(i, j):
        cost = (DynamicProgramming(c, i, k) + DynamicProgramming(c, k + 1, j) + c[i - 1] * c[k] * c[j])
        mc[i][j] = min(mc[i][j], cost)

    return mc[i][j]

def Matrix(c, n):
    return DynamicProgramming(c, 1, n - 1)

n = int(input("Enter number of matrices: "))

arr = []

for i in range(n + 1):
    arr.append(int(input("Enter dimension: ")))

print("Minimum number of scalar multiplications is:")
print(Matrix(arr, n + 1))
