print("Made by Luna Molina")
print("---------------------------------------------")
import time
loose = ("The computer wins")
win = ("You win")
tie = ("It´s a tie")
lives = 5
score = 0
draw = 0
computerLives = 7
passwordList = []
while True:
    print("To begin fill in the below information")
    username = input("Please enter your username    ")
    password = input("Please enter your password    ")
    searchfile = open("accounts.txt", "r")
    for line in searchfile:
        passwordList.append(line.strip())
        if username and password in passwordList:
            print("Access granted")
            time.sleep(0.5)
            print("Loading...")
            print("---------------------------------------------")
            print("Welcome!")
            print("You start with ",lives," lives")
            print("If you win you get an extra live.")
            print("If you loose you loose a live")
            print("If you draw the lives stay the same")
            print("To see a list of the rules type Rules")
            print("If you want to leave at any point type exit")
            print("The computer's lives have the same rules as yours")
            print("---------------------------------------------")
            while True:
                        rps = input("rock, paper, scissor?")
                        rps = rps.title()
                        import random
                        computer = ("rock", "paper", "scissor")
                        computer = random.choice(computer)
                #rock possibilites
                        if rps == "Rock" and computer =="paper":
                            print("The computer chose ", computer)
                            print("")
                            print(loose)
                            lives-=1
                            print("You have ",lives," lives remaining. You tied ",draw," times and won ",score," times")
                        if rps == "Rock" and computer =="scissor":
                            print("The computer chose ", computer)
                            print("")
                            print(win)
                            lives+=1
                            score+=1
                            print("You have ",lives," lives remaining. You tied ",draw," times and won ",score," times")
                        if rps == "Rock" and computer =="rock":
                            print("The computer chose ", computer)
                            print("")
                            print(tie)
                            draw+=1
                            print("You have ",lives," lives remaining. You tied ",draw," times and won ",score," times")
                #paper possibilities
                        if rps == "Paper" and computer =="scissor":
                            print("The computer chose ", computer)
                            print("")
                            print(loose)
                            lives-=1
                            print("You have ",lives," lives remaining. You tied ",draw," times and won ",score," times")
                        if rps == "Paper" and computer =="rock":
                            print("The computer chose ", computer)
                            print("")
                            print(win)
                            lives+=1
                            score+=1
                            print("You have ",lives," lives remaining. You tied ",draw," times and won ",score," times")
                        if rps == "Paper" and computer =="paper":
                            print("The computer chose ", computer)
                            print("")
                            print(tie)
                            draw+=1
                            print("You have ",lives," lives remaining. You tied ",draw," times and won ",score," times")
                    #scissor possibilities
                        if rps == "Scissor" and computer =="rock":
                            print("The computer chose ", computer)
                            print("")
                            print(loose)
                            lives-=1
                            print("You have ",lives," lives remaining. You tied ",draw," times and won ",score," times")
                        if rps == "Scissor" and computer =="paper":
                            print("The computer chose ", computer)
                            print("")
                            print(win)
                            lives+=1
                            score+=1
                            print("You have ",lives," lives remaining. You tied ",draw," times and won ",score," times")
                        if rps == "Scissor" and computer =="scissor":
                            print("The computer chose ", computer)
                            print("")
                            print(tie)
                            draw+=1
                            print("You have ",lives," lives remaining. You tied ",draw," times and won ",score," times")
                    #system
                        if rps == "Rules":
                            print("**********************************************")
                            print("Rules")
                            print("**********************************************")
                            print("-Rock looses against Paper")
                            print("-Rock beats Scissors")
                            print("-Paper beats Rock")
                            print("-Paper looses against Scissors")
                            print("-Scissors beats Paper")
                            print("-Scissors looses against Rock")
                            print("**********************************************")
                    #ending
                        if rps == "Test" or lives == 0:
                            print("You have ran out of lives")
                            print("You won ",score," matches")
                            print("Thats all, thanks for playing")
                            stop= input("Press enter to exit")
                            exit()
                        if computerLives == 0:
                            print("You beated the computer!")
                            print("You won ",score," matches")
                            print("Thats all, thanks for playing")
                            stop= input("Press enter to exit")
                            import time
                            time.sleep(900)
                            exit()
                    #exit
                        if rps == "exit":
                            break
    else:
        print("Your username or password is incorrect.")
        print("---------------------------------------")
