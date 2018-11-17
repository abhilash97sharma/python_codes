# while loop
num1 = input('Enter the no:')
i = 1
print("the table of " + num1 + ":")
while i <= 10:
    print(num1 + '*' + str(i) + '=' + str(int(num1) * i))
    i += 1

# for loop
for letter in "Abhilash":  # with string
    print(letter)

name = ["Abhilash", "Sharma", "Sonu"]  # for list
for nam in name:
    print(nam)

for num in range(2,10):  # range of number
    print(num)

for num1 in range(len(name)):  # printing names
    print(name[num1])
