with open("advent-of-code/2025/day3/input.txt", "r") as f:
    banks = f.read().splitlines()

total = 0

for b in banks:
    stack = []
    n_drop = len(b) - 12

    for num in b:
        while n_drop > 0 and len(stack) > 0 and num > stack[-1]:
            stack.pop()
            n_drop -= 1
        
        stack.append(num)
    
    total += int(''.join(stack[:12]))

print(total)