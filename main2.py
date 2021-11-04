def main(l,k,count):
    # for i in range(len(l)+1):
    for i in range(len(l)):
        if l[i] == '.':
            for j in range(k):
                if (i+j >= len(l)):
                    break
                l[i+j] = 'w'
            count += 1
        else:
            pass
    return(count)


n,k = map(int,input().split())
s = input()
count = 0
l = [0 for i in range(n)]
for i in range(n):
    l[i] = s[i:i+1]
print(main(l,k,count))
