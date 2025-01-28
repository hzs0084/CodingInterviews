def getTripletCount(a, d):
    n = len(a)
    count = 0
    # Iterate through all possible triplets
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % d == 0:
                    count += 1
    return count

if __name__ == '__main__':
    # Input
    n = int(input())  # Number of elements in the array
    a = [int(input()) for _ in range(n)]  # Array elements
    d = int(input())  # Divisor

    # Output
    print(getTripletCount(a, d))
