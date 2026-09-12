mc = [[0 for n in range(50)] for m in range(50)]

def Display(c, n):
    print("DP Table:")

    for i in range(1, n):
        for j in range(1, n):
            if j >= i:
                print(mc[i][j], end="\t")
            else:
                print("-", end="\t")
        print()

def DynamicProgramming(c, n):
    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            mc[i][j] = 999999

            for k in range(i, j):
                cost = (mc[i][k] + mc[k + 1][j] + c[i - 1] * c[k] * c[j])
                mc[i][j] = min(mc[i][j], cost)

        print()
        print("After iteration", length - 1)
        Display(c, n)

    return mc[1][n - 1]

n = int(input("Enter number of matrices: "))

arr = []

print("Enter dimensions:")

for i in range(n + 1):
    arr.append(int(input()))

print()
print("Minimum number of multiplications is:")
print(DynamicProgramming(arr, n + 1))
