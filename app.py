userInput = input("Enter your username: ")
userPassword = input("Enter your password: ")
print(userInput + "You have succesfully Registered!" )

print("Welcome to the login page!")
loginInput = input("Enter your username: ")
loginPassword = input("Enter your password: ")

if userInput == loginInput and userPassword == loginPassword:
    print("Welcome back " + userInput + "!")
else:
    print("Incorrect username or password!")
