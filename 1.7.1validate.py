user_name = input("Enter the user name(less than 12 characters,must not contain space/digit) : ")

if len(user_name) >= 12:
    print("User name can not contain more than or equal to 12 characters")
elif not user_name.find(" ") == -1:
    print("User name cot not contain spaces")
elif not user_name.isalpha():
    print("User name can not contain digits")
else:
    print("Welcome, Your password is valid!!!")