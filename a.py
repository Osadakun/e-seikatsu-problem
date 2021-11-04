if __name__ == '__main__':
    num = list(map(int,input().split()))
    L = num[-1]  # 木材の長さ
    num.pop()    # 木材の長さを取り除いたもの
    cnt = num.count(L)
    num = [i for i in num if i != L]   # 木材の長さと同じなら先にリストから削除
    num = sorted(num, reverse=True)   # ソート
    for i in range(len(num)):
        for j in range(len(num)):
            if (len(num) == 1):
                cnt += 1
                num.remove(num[j])
                break
            if (num[i]+num[j] > L):
                pass
            elif (num[i]+num[j] == L):
                cnt += 1
                num.remove(num[i])
                num.remove(num[j])
                break
            if (j == len(num)-1):
                cnt += 1
                num.remove(num[i])

    print(cnt)