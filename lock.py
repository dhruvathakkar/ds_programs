def generate(code, used):
    if len(code) == 3:
        print("".join(code))
        return

    for digit in ['1', '2', '3']:
        if digit not in used:
            used.add(digit)
            generate(code + [digit], used)
            used.remove(digit)

generate([], set())