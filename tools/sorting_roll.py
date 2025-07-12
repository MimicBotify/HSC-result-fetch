import re

input_file = "tools/rolls.txt"
output_file = "tools/sorted_rolls.txt"

rolls = set()

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        # Extract the roll number at the start of the line (before any non-digit)
        match = re.match(r"(\d+)", line.strip())
        if match:
            rolls.add(match.group(1))

sorted_rolls = sorted(rolls, key=int)

with open(output_file, "w", encoding="utf-8") as f:
    for roll in sorted_rolls:
        f.write(roll + "\n")

print(f"Sorted {len(sorted_rolls)} roll numbers written to {output_file}")