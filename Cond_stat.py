is_male = True
is_tall = False

if is_male:
    print("You are a male")
else:
    print('You are a female')

if is_male and is_tall:
    print("you are male and tall")
elif is_male and not is_tall:
    print('you are male and not tall')
elif not is_male and is_tall:
    print('you are not male and tall')
else:
    print("you are not male or not tall")





