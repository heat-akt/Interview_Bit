A = [5, 10, 3, 2, 50, 80]
B = 78
A.sort()
print(A)
i = 0
j = 1
while j < len(A):
    if A[j] - A[i] < B:
        j += 1
    elif A[j] - A[i] > B:
        i += 1
    else:
        print("1")
        break
print("0")
