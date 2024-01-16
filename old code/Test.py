A = [list(map(int, input().split())) for i in range(10)]
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end = ' ')
    print()