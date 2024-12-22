# First I need to Sort left list and right list in ascending order from top to bottom
# Then I need to calculate the difference between the two lists each row
# Then I need to sum the differences

fhand = open('Location_ID\'s.txt')

list1 = []
list2 = []
for line in fhand:
    ids = line.split('   ')
    list1.append(int(ids[0]))
    list2.append(int(ids[1]))

sortedlist1 = sorted(list1)
sortedlist2 = sorted(list2)

total = 0
for i in range(len(sortedlist1)):
    total += abs(sortedlist1[i] - sortedlist2[i])

print(total)