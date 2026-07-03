def climb(n):
    if n == 0 or n == 1:
        return 1

    return climb(n - 1) + climb(n - 2)


n = int(input("Enter Number of Stairs: "))

print("Total Ways =", climb(n))