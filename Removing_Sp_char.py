import re
s1 = "#Hello Abhilash Sharma is a good boy @viratkohli12334 "
s3 = re.sub('[#@]','',s1)   #removing the special characters
print(s3)

#removing alnum
s4 = re.sub('a.','',s1)    #a. is matches with a and its consecutive character
print(s4)

s5 = re.sub('[a+b]','',s1)    #replaces characters a or b with the spaces.
print(s5)
s6 = re.sub('[a*|b*]','',s1)    #replaces entire string after a with spaces. i.e [a,aa,aaa,....]
print(s6)
s7 = re.sub('@.*','',s1)    #remove entire content after @ character meet.
print(s7)
s8 = re.sub('@..','',s1)    #remove entire content after @ character meet.
print(s8)
s9 = re.sub('vi.*','',s1)
print(s9)
#...
if re.search("inform","We need to inform him with the latest information"):
    print('There is inform')

#finding the words from the regular expression
allinform = re.findall('inform','We need to inform him with the latest information')  #returns the list of all the occurances
for i in allinform:
    print(i)

#finding or making an iterator for starting and ending
for i in re.finditer('inform','We need to inform him with the latest information'):
    locup = i.span()
    print(locup)