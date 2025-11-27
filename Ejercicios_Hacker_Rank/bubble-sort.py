def countSwaps(a):
    n = len(a)
    numSwaps = 0

    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                numSwaps += 1

    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

a = [64, 34, 25, 12, 22, 11, 90,100]
countSwaps(a)
