import re
fhand = open("memory.txt")
total = 0
switch = True

for line in fhand:
    line = line.strip()
    lst = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
    
    
    for element in lst:
        if element == 'don\'t()':
            switch = False  
            continue

        if element == 'do()':
            switch = True
            continue

        elif switch == True :
            number1 = int(re.findall(r'mul\((\d{1,3})', element)[0])
            number2 = int(re.findall(r'\,(\d{1,3})\)', element)[0])
            total += (number1 * number2)

print(total)

  


# enables = line.find("do()")
# disables = line.find("don't()")