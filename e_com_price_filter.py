prices = [15000, 20000, 35000, 50000, 65000, 80000]
filter = 50000

left = 0
right = len(prices) - 1
ans = -1

while left <= right:
    mid = (left + right) // 2

    if prices[mid] >= filter:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

if ans != -1:
    print("First product >= target:", prices[ans])
else:
    print("No product found")