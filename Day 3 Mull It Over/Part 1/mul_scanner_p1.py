import re
fhand = open("memory.txt")

total = 0
for line in fhand:
    line = line.strip()
    lst = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
    
    for element in lst:
        number1 = int(re.findall(r'mul\((\d{1,3})', element)[0])
        number2 = int(re.findall(r'\,(\d{1,3})\)', element)[0])
        # print(number1, number2)
        total += (number1 * number2)

print(total)

  


