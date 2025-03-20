fhand = open('word_database.txt')
import re

previous_lines = []
# Types of matches

# Horizontal + Backwards
count_horizontal = 0
count_vertical = 0
count_diagonal = 0

for line in fhand:
    xmas = re.findall('XMAS', line)
    samx = re.findall('SAMX', line)
    count_horizontal += len(xmas) + len(samx)

    previous_lines.append(list(line.strip()))  
    if len(previous_lines) == 4:
        # Vertical + Backwards
        for col in range(len(previous_lines[0])):
            if (previous_lines[0][col] == 'X' and
                previous_lines[1][col] == 'M' and
                previous_lines[2][col] == 'A' and
                previous_lines[3][col] == 'S'):
                count_vertical += 1
            if (previous_lines[0][col] == 'S' and
                previous_lines[1][col] == 'A' and
                previous_lines[2][col] == 'M' and
                previous_lines[3][col] == 'X'):
                count_vertical += 1

            # Diagonal + Downwards (Left to Right)
            # Check bounds for positive direction
            if col + 3 < len(previous_lines[0]):  
                if (previous_lines[0][col] == 'X' and
                    previous_lines[1][col + 1] == 'M' and
                    previous_lines[2][col + 2] == 'A' and
                    previous_lines[3][col + 3] == 'S'):
                    count_diagonal += 1

            # Diagonal + Upwards (Left to Right)
            # Check bounds for negative direction
            if col - 3 >= 0:  
                if (previous_lines[0][col] == 'X' and
                    previous_lines[1][col - 1] == 'M' and
                    previous_lines[2][col - 2] == 'A' and
                    previous_lines[3][col - 3] == 'S'):
                    count_diagonal += 1

            # Diagonal + Downwards (Right to Left)
            # Check bounds for negative direction
            if col - 3 >= 0:  
                if (previous_lines[3][col - 3] == 'X' and
                    previous_lines[2][col - 2] == 'M' and
                    previous_lines[1][col - 1] == 'A' and
                    previous_lines[0][col] == 'S'):
                    count_diagonal += 1

            # Diagonal + Upwards (Right to Left)
            # Check bounds for positive direction
            if col + 3 < len(previous_lines[0]): 
                if (previous_lines[3][col + 3] == 'X' and
                    previous_lines[2][col + 2] == 'M' and
                    previous_lines[1][col + 1] == 'A' and
                    previous_lines[0][col] == 'S'):
                    count_diagonal += 1

        previous_lines.pop(0) 

total = count_diagonal + count_horizontal + count_vertical

print("Horizontal matches:", count_horizontal)
print("Vertical matches:", count_vertical)
print("Diagonal matches:", count_diagonal)
print("Total matches:", total)