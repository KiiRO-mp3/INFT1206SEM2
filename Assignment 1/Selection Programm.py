#Name: Isaiah Mugisha 
#Date: 30th September 2026
#Assignment Description: This is my programm demonstrating my knowledge on the use of 
#selection operators

#Problem 
# Make a selection-based code with a flow chart validating the input from the user and making sure everything is checked and uploaded

# I asked for an idea for my program, Password validator, basically it will be “Anatato” that is what will be asked for the password, what we will be validating, number of letters to be 7, if it has a validated A

# Pseudo Code
# Input
# userpassword = input()

# Output
# Success Message
# Print(Welcome to the system, User)

# Fail messages
# Print(sorry the first letter isn’t capitalized
# Print(Please try again)

# Process
# If user password == string that is true
# if userpassword [0].isupper()
# else = sorry the first letter isn’t capitalized
# Else = sorry please try again

set_password = "anatato" #supposed to be typed as Anatato, made it small in order for the second if statement to be impactful and make a proper check

print("Hello welcome to the system")
print("Please enter the correct password to enter the System")
user_password = input()
#password is Anatato

if user_password.islower()==set_password: #lowered the user password incase 
    if user_password[0]=="A":
        print("Welcome to the System")
    else:
        print("Sorry but something is not capitalized")
else:
    print("Please try again")

