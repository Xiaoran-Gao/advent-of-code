with open("advent-of-code/2025/day7/input.txt", "r") as f:
    lines = f.read().splitlines()

n_split = 0
beam_pos = [lines[0].find('S')]

for i in range(2, len(lines), 2):
    splitter_pos = [j for j, ch in enumerate(lines[i]) if ch == '^']
    hit = []

    for b in beam_pos:
        if b in splitter_pos:
            n_split += 1
            hit.append(b)
            
    for b in hit:
        if b - 1 not in beam_pos:
            beam_pos.append(b - 1)
        if b + 1 not in beam_pos:
            beam_pos.append(b + 1)

        beam_pos.remove(b)

print(n_split)