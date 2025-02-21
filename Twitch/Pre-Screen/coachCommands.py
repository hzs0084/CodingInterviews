def solution(commands):
    count = 0  # Tracks how many times they face the same direction
    rotation = 0  # Tracks the total "rotation" offset

    for command in commands:
        if command == 'L':
            rotation += 1  # "L" is misheard as "R"
        elif command == 'R':
            rotation -= 1  # "R" is misheard as "L"
        elif command == 'A':
            rotation += 2  # "A" is a 180° flip

        # Check alignment right after each command
        if rotation % 4 == 0:
            count += 1

    return count

# Test it out
print(solution("LLARL"))  # Expected: 3
print(solution("RAAL"))   # Expected: 2
print(solution("L"))      # Expected: 0
print(solution("A"))      # Expected: 1

