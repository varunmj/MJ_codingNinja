# Write a program that takes a character as input and prints 1,0,-1 according to the following rules:
# 1 if the character is an uppercase
# 0 if the character is lowercase
# -1 if the character is not an alphabet

a  = input()

if a.isalpha() == True:
    if a.islower() ==True:
        print('0')
    else:
        print('1')
else:
    print('-1')