def main(cnt,num,L):
    for i in num:
        v = L - i
        for j in num:
            if v == j:
                cnt += 1
                num.remove(i)
                num.remove(j)
                break
            else:
                num.remove(i)
                cnt += 1
                break
    return cnt

num = list(map(int,input().split()))
L = num[-1]  # 木材の長さ
num.pop()    # 木材の長さを取り除いたもの
cnt = num.count(L)
num = [i for i in num if i != L]   # 木材の長さと同じなら先にリストから削除
num = sorted(num, reverse=True)   # 逆ソート
print(main(cnt,num,L))