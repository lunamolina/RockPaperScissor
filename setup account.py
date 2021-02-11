print("Rock, paper, scissors account setup")
while True:
        username = input("Pick your username  ")
        password = input("Pick your password  ")
        confirmPassword = input("Please confirm your password  ")
        if password == confirmPassword:
            print("Your account has been setup successfully")
            text_file = open("accounts.txt","a")
            text_file.write("\n")
            text_file.write(username)
            text_file.write("\n")
            text_file.write(password)
            text_file.close()
        
        if password != confirmPassword:
            print("Your password does not match")
        break

