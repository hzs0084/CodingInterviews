from math import gcd
from collections import defaultdict

def solution(a):
    """
    Given a list of lists 'a', group the indices of 'a' that have the same mean.
    Return a list of these index-groups, where:
      - Each group is sorted in ascending order.
      - The groups themselves are sorted by the smallest index in each group.
    """

    # Dictionary: (numerator, denominator) of the mean in simplest form -> list of indices
    mean_groups = defaultdict(list)

    for i, arr in enumerate(a):
        s = sum(arr)       # sum of elements
        length = len(arr)  # number of elements
        g = gcd(s, length) # greatest common divisor

        # Reduce (s, length) to simplest form to avoid floating-point issues
        s //= g
        length //= g

        mean_groups[(s, length)].append(i)

    # Sort indices within each group
    for key in mean_groups:
        mean_groups[key].sort()

    # Collect and sort the groups by the first (smallest) index in each
    result = list(mean_groups.values())
    result.sort(key=lambda group: group[0])

    return result

# ----
# Example usage:
if __name__ == "__main__":
    # Example 1
    a1 = [[3, 3, 4], [2, 2, 2], [2, 5], [3, 3], [1, 5]]
    print(solution(a1))  
    # Output might look like:
    # [
    #   [0],     # If [3,3,4] has a unique mean
    #   [1],     # If [2,2,2] has a unique mean
    #   [2],     # etc.
    #   [3, 4]   # If [3,3] and [1,5] share the same mean (which is 3)
    # ]
    
    # Example 2
    a2 = [[3,3,4], [2,3,2], [3,1], [3,3], [2,5]]
    print(solution(a2))
    # According to some statements, might yield [[0, 4], [1, 3], [2]] if certain pairs share the same mean.


# Humanize it 

# from math import gcd
# from collections import defaultdict

# def solution(a):

#     mean_groups = defaultdict(list)

#     for i, arr in enumerate(a):
#         sumOfElements = sum(arr)       
#         lengthOfThoseElements = len(arr) 
#         greatestCommonDivisor = gcd(sumOfElements, lengthOfThoseElements) 
#         sumOfElements //= greatestCommonDivisor
#         lengthOfThoseElements //= greatestCommonDivisor

#         mean_groups[(sumOfElements, lengthOfThoseElements)].append(i)

#     for key in mean_groups:
#         mean_groups[key].sort()

#     result = list(mean_groups.values())
#     result.sort(key=lambda group: group[0])

#     return result