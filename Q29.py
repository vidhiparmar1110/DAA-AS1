mc = [[-1 for n in range(50)] for m in range(50)]

def DynamicProgramming(c, i, j):
    if i == j:
        return 0

    if mc[i][j] != -1:
        return mc[i][j]

    mc[i][j] = 999999

    for k in range(i, j):
        mc[i][j] = min(mc[i][j], DynamicProgramming(c, i, k) +DynamicProgramming(c, k + 1, j) + c[i - 1] * c[k] * c[j])

    return mc[i][j]

def Matrix(c, n):
    return DynamicProgramming(c, 1, n - 1)

n = int(input("Enter number of matrices: "))

arr = []

print("Enter matrix dimensions:")

for i in range(n + 1):
    arr.append(int(input()))

print("Matrix dimensions are:")

for i in range(n):
    print("A" + str(i + 1) + " = " + str(arr[i]) + " x " + str(arr[i + 1]))

print("Minimum number of multiplications is:")
print(Matrix(arr, n + 1))
