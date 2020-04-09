import string
import random
# user data
def get_details():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email address: ")
    details = [first_name,last_name,email]
    return details

#generating random password with user data
def gen_password(details):

    characters = string.ascii_letters
    length = 5
    random_password = ''.join(random.choice(characters) for i in range(length))

    password = str(details[0][0:2] + details [1][-2:] + random_password)
    return password

#program
status = True
container = []

while status:
    #getting user details
    details = get_details()

    #showing generated password
    password = gen_password(details)
    print("Your password is: " + str(password))

    #ask if user would like to continue
    password_like = input(str("Are you satisfied with the password generated? If yes, enter Yes. If no, enter No new password: "))

    password_loop = True
    while password_loop:
       if password_like == 'Yes':
           details.append(password)
           #password to be added to user details

           #adding user details to the container
           container.append(details)

           password_loop = False;
           break

       else:
           #user enters password greater than or equal to 7
           user_password = input(str("Enter password longer than or equal to 7: "))

           #password length loop
           password_length = True

           while password_length:
               if len(user_password) >= 7:
                   details.append(user_password)
                   #adding password to user data

                   #adding details to container
                   container.append(details)

                   #breaking out of password lenght loop and password loop
                   password_length = False
                   password_loop = False

               else:
                   print("Your password is less than 7")
                   user_password = input(str("Please enter a longer password, which is longer or equal to 7 characters: "))
#adding a new user
new_user = input(str("Would you like to create a new user profile?) Yes or No: "))
if (new_user == "No"):
    status = False
    for item in container:
        print(item)

else:
    status = True