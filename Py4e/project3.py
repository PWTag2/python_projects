### This program returns the product of the two numbers inputed, only if it equals to, or is less than 1000. If not, it returns the sum.
# num1 = int(input("Give me a number. "))
# num2 = int(input("Give me another number. "))
# product = num1 * num2
# sum = num1 + num2
#
# if product == 1000:
#     print(product)
# elif product < 1000:
#     print("The product of your numbers is:", product)
# else:
#     print("Since the product of your numbers is greater than 1000, the sum is:", sum)

### This program switches the users first and last name.
# firstname = str(input("What is your first name? "))
# lastname = str(input("What is your last name? "))
# print(lastname, firstname)

### This program spells your name backwards
firstname = str(input("What is your first name? "))
lastname = str(input("What is your last name? "))
def backwardsName(name1, name2):
    string = name1 + " " + name2
    s = string[::-1]
    return "Your name backwards is:" + s

print(backwardsName(firstname, lastname))

### This program is specific to Coursera's libary. It extracts the floating point
#values from each of the lines and computes the average of those values
# # Use the file name mbox-short.txt as the file name
# #fname = input("Enter file name: ")
# #fh = open(fname)
# #count = 0
# total = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     t = line.find("0")
#     number = float(line[t:])
#     count += 1
#     total += number
#
# average = total/count
# print("Average spam confidence:", average)
