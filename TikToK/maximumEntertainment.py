'''
In the TikTok feed, there are n videos available for a user to watch, each with a specific entertainment score. The user can choose three videos to watch in a sequence, 
With the option to rewatch a particular video twice or even thrice.

Specifically, the user will select three indices i,j,k such that 0 <= i < j < k < n, where i, j, k represent the indices of the videos chosen. The user can select videos in the following ways:

- Watch the same video three times (i.e., i = j = k).
- Watch the same video twice and a different one once (i = j < k or i<j= k).
- Watch three different videos (i < j < k).

Each video has an entertainment score represented as an array entertainment of integers. The user's total enjoyment for watching the selected videos is calucluated as follows:
- The enjoyment from the first vidfeo is entertainment[i].
- The enjoyment from the second video is multiplied by a factor r. contributing r * entertainment[j].
- The enjoyment from the third video is multiplied by a factor r^2, contributing r^2 * entertainment[k].

Given the array entertainment and the integer r, your task is to determine the maximum possible enterntainment score the user can achieve by selecting the videos optimallly selecting indices i,j,k.


'''

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
