n,m = map(int, input().split())
mo = list(map(int,input().split()))
d = [float("inf") for i in range(n+2)]
d[0] = 0
for i in range(n+1):
    for j in mo:
        if i+j <= n:
            d[i+j] = min(d[i+j],d[i]+1)
print(d[n])