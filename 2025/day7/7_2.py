with open("advent-of-code/2025/day7/input.txt", "r") as f:
    lines = f.read().splitlines()

beam_dict = {lines[0].find('S'): 1}

for i in range(2, len(lines), 2):
    splitter_pos = [j for j, ch in enumerate(lines[i]) if ch == '^']
    hit = []

    for b in beam_dict:
        if b in splitter_pos:
            hit.append(b)
            
    for b in hit:
        beam_dict[b - 1] = beam_dict.get(b - 1, 0) + beam_dict[b]
        beam_dict[b + 1] = beam_dict.get(b + 1, 0) + beam_dict[b]
        beam_dict[b] = 0

n_tl = sum(beam_dict.values())
print(n_tl)