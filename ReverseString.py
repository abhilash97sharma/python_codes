s1 = input('Enter the String')
s2 = s1[::-1]
if s1 == s2:
    print('Strings are palindrome')
else:
    print('String are not palindrome')
s3 = s1[::+2]
s4 = s1[::+3]  # for leaving a character in between
print(s2)
print(s3)
print(s4)
