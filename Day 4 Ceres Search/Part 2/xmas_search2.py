fhand = open('word_database2.txt')

lines = []
count_x = 0
for line in fhand:
    lines.append(list(line.strip()))  
    if len(lines) == 3:
        previous_line = lines[0]
        current_line = lines[1]
        next_line = lines[2]
        for col in range(len(previous_line)):
            if col+2 < len(previous_line):
                # both MAS
                if (previous_line[col] == 'M' and
                    previous_line[col + 2] == 'S' and
                    current_line[col + 1] == "A" and
                    next_line[col] == "M" and
                    next_line[col + 2] == "S"):
                        count_x += 1
                #  both SAM
                if (previous_line[col] == 'S' and
                    previous_line[col + 2] == 'M' and
                    current_line[col + 1] == "A" and
                    next_line[col] == "S" and
                    next_line[col + 2] == "M"):
                        count_x += 1
                # Top MAS bottom SAM    
                if (previous_line[col] == 'M' and
                    previous_line[col + 2] == 'M' and
                    current_line[col + 1] == "A" and
                    next_line[col] == "S" and
                    next_line[col + 2] == "S"):
                        count_x += 1
                # Top SAM bottom MAS    
                if (previous_line[col] == 'S' and
                    previous_line[col + 2] == 'S' and
                    current_line[col + 1] == "A" and
                    next_line[col] == "M" and
                    next_line[col + 2] == "M"):
                        count_x += 1
        lines.pop(0) 

print("Total X matches:", count_x)