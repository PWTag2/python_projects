import re
file = open("project4.txt")
sum = 0

for line in file:
    y = re.findall('[0-9]+', line)
    for number in y:
        num = int(number)
        sum += num

print(sum)
