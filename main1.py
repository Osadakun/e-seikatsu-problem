def main(cnt,num):
    for i in range(cnt):
        x = num.count(num[i])
        if x >= 4:
            return "Yes"
        else:
            if i == cnt:
                return "No"
            pass
# if __name__ == '__main__':
cnt = int(input()) - 3
print(cnt)
num = list(map(int, input().split()))
print(main(cnt,num))