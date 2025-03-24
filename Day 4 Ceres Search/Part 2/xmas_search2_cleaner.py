fhand = open('word_database2.txt')

lines = []
count_x = 0
for line in fhand:
    lines.append(list(line.strip()))  
    if len(lines) == 3:
        for col in range(len(lines[0])):
            if col+2 < len(lines[0]):
                if lines[1][col+1] == 'A':
                    diagonal1 = lines[0][col] + lines[1][col+1] + lines[2][col+2]
                    diagonal2 = lines[0][col+2] + lines[1][col+1] + lines[2][col]

                    if(diagonal1 == "MAS" and diagonal2 == "MAS"):
                        count_x += 1
                    if(diagonal1 == "SAM" and diagonal2 == "SAM"):
                        count_x += 1
                    if(diagonal1 == "MAS" and diagonal2 == "SAM"):
                        count_x += 1
                    if(diagonal1 == "SAM" and diagonal2 == "MAS"):
                        count_x += 1

                
        lines.pop(0) 

print("Total X matches:", count_x)