
lines = []


print("Enter lines of text (type 'STOP' to end):")
while True:
    line = input()
    if line == "STOP":
        break
    lines.append(line)


capitalized_lines = [line.upper() for line in lines]


print("\nCapitalized Lines:")
for capitalized_line in capitalized_lines:
    print(capitalized_line)
