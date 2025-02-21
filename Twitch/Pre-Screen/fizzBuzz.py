def solution(n):
    result = []
    for i in range(1, n+1):
        if i % 15 == 0:        # i is a multiple of both 3 and 5
            result.append("FizzBuzz")
        elif i % 3 == 0:       # i is a multiple of 3 only
            result.append("Fizz")
        elif i % 5 == 0:       # i is a multiple of 5 only
            result.append("Buzz")
        else:                  # i is neither a multiple of 3 nor 5
            result.append(str(i))
    return result

print(solution(15))