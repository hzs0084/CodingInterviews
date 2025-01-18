def maximumEntertainment(entertainment, r):
    n = len(entertainment)
    
    # If there is only one video, the result is its entertainment score
    if n == 1:
        return entertainment[0] + r * entertainment[0] + r * r * entertainment[0]
    
    # Step 1: Precompute the maximum values from left to right for `i`
    max_left = [0] * n
    max_left[0] = entertainment[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], entertainment[i])
    
    # Step 2: Precompute the maximum values from right to left for `k`
    max_right = [0] * n
    max_right[-1] = entertainment[-1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], entertainment[i])
    
    # Step 3: Iterate through `j` and calculate the maximum score
    max_score = float('-inf')
    
    # Case when j is strictly between i and k
    for j in range(1, n - 1):
        left = max_left[j - 1]
        right = max_right[j + 1]
        score = left + r * entertainment[j] + r * r * right
        max_score = max(max_score, score)
    
    # Handle edge cases for j == i == k
    for j in range(n):
        score = entertainment[j] + r * entertainment[j] + r * r * entertainment[j]
        max_score = max(max_score, score)
    
    return max_score


if __name__ == '__main__':
    entertainment = [1, 2, 3, 4, 5]
    r = 2
    print(maximumEntertainment(entertainment, r))  # Example Output: 35
