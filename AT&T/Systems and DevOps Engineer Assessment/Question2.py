def countIncreasingSegments(yCoordinates, k):
    n = len(yCoordinates)
    count = 0
    
    # Loop through the array to find all segments of length k
    for i in range(n - k + 1):
        is_increasing = True
        # Check if the segment is increasing
        for j in range(i, i + k - 1):
            if yCoordinates[j] >= yCoordinates[j + 1]:
                is_increasing = False
                break
        if is_increasing:
            count += 1

    return count

if __name__ == '__main__':
    # Input
    n = int(input())  # Number of elements in yCoordinates
    yCoordinates = [int(input()) for _ in range(n)]  # Y-coordinates
    k = int(input())  # Number of consecutive points

    # Output
    print(countIncreasingSegments(yCoordinates, k))
