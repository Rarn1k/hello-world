def first_bigger(arr, target):
    start = 0
    end = len(arr) - 1

    ans = len(arr)
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            ans = mid
            end = mid - 1
    return ans


n = int(input())
price = [int(_) for _ in input().split()]
days = int(input())
price.sort()
for i in range(days):
    money = int(input())
    print(first_bigger(price, money))
