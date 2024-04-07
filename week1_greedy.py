import sys

#input 여러 줄 입력 받기
n = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for i in range(n)]

#문제풀이
for i in range(n):
    amount = int(arr[i])
    coins = [25, 10, 5, 1]
    coin_count = []
    for coin in coins:
        count = amount // coin
        coin_count.append(count)
        amount %= coin
    print(*coin_count)

