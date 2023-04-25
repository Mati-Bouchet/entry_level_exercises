
# Enter a password that has at least 8 characters, 1 number,  1 special character, 1 uppercase and 1 lowercase
password = input("Please enter a password: ")
    
has_eight_char = False
has_lower_case = False
has_upper_case = False
has_digit = False
has_special_char = False


if (len(password) >= 8) and (len(password) <= 16):

    has_eight_char = True

    for i in password:

        if (i.islower()):
            has_lower_case = True

        if (i.isupper()):
            has_upper_case = True

        if (i=="@" or i=="$" or i=="_" or i== "#" or i=="&"):
          has_special_char = True

        if (i.isdigit()):
           has_digit = True
           

if (has_eight_char == True and has_lower_case == True and has_upper_case == True and has_special_char == True and has_digit == True):
    print("Your password is correct")
else:
    print("Password should have at least 8 characters and include a number, a special character, an uppercase and a lowercase")



