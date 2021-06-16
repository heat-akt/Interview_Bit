def nTriangle(A, i):
    MOD = 1000000007
    lo = 0
    hi = i - 1
    ans = 0
    while lo < hi:
        if A[lo] + A[hi] > A[i]:
            ans = (ans + hi - lo) % MOD
            hi = hi - 1
        else:
            lo = lo + 1
    return ans


A = [4, 3, 6, 7]
MOD = 1000000007
n = len(A)
A.sort()
ans = 0
for i in range(n-1, 1, -1):
    ans =(ans+nTriangle(A, i))%MOD
print(ans)
