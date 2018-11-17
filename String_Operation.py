import re
str1=input('Enter any string:')
print('You have entered \''+str1+"\' String")
s1 = "#Hello Abhilash Sharma is a good boy @viratkohli "
s2 = "Abhi"
#print(len(s1))
#for i in s1:
#    print(i)

print(s1[0])
s2 = s1.find(s2)
print(s2)

n = int(input())
for i in range(1,n+1):
    print(i,end="")

s3 = re.sub('[#@]', '', s1)
print(s3)