numbers = [5, 12, 7, 3, 18, 9]
x = 18
idx = 0
for num in numbers:
    if x == num:
        print(f"{x} found at index={idx}")
        break
    idx += 1