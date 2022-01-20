grade = int(input('grade = '))
if 90 >= grade >= 100 :
    print('Your mark is A')
elif 75 <= grade:
    print('Your mark is B')
elif 60 <= grade:
    print('Your mark is C')
elif 0 < grade:
    print('Your mark is D')
else:
    print("Error")
print('Well done!')
