fhand = open('Reports.txt')
safecount = 0

for line in fhand:
    report = [int(x) for x in line.split()]
    is_valid = True
    movement_type = None  
    
    for level in range(len(report) - 1):
        increasing = (report[level] < report[level + 1] and abs(report[level] - report[level + 1]) <= 3)
        decreasing = (report[level] > report[level + 1] and abs(report[level] - report[level + 1]) <= 3)
        
    
        if level == 0:
            if increasing:
                movement_type = "increasing"
            elif decreasing:
                movement_type = "decreasing"
            else:
                is_valid = False
                break
       
        else:
            if movement_type == "increasing" and not increasing:
                is_valid = False
                break
            elif movement_type == "decreasing" and not decreasing:
                is_valid = False
                break
    
    if is_valid:
        safecount += 1

print(f"The number of safe reports are: {safecount}")
fhand.close()
