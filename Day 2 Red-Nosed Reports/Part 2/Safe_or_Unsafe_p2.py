fhand = open('Reports.txt')
safecount = 0

for line in fhand:
    report = [int(x) for x in line.split()]
    n = len(report)

    def is_safe(sequence):
        """Check if a sequence is strictly increasing or decreasing."""
        increasing = all(1 <= (sequence[i+1] - sequence[i]) <= 3 for i in range(len(sequence) - 1))
        decreasing = all(1 <= (sequence[i] - sequence[i+1]) <= 3 for i in range(len(sequence) - 1))
        return increasing or decreasing
    
    if is_safe(report):
        safecount += 1
        continue

    for i in range(n):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            safecount += 1
            break
    
fhand.close()
print(f"The number of safe reports are:{safecount}")
    