import random

options = ["Rock", "paper", "scisser"]

computer_score = 0
user_score = 0
Name = input(" Please Insert Name : ")


print("0-Rock")
print("1-paper")
print("2-scisser")

while True:
    computer_choise = random.choice(options)
    u_choice_index = int(input())
    user_choice = options[u_choice_index]


    if computer_choise == "Rock" and user_choice == "scisser" :
        print("computer Win")
        computer_score += 1
        print("COMPUTER :",computer_score ," VS " , Name," :", user_score)

    elif computer_choise == "Rock" and user_choice == "paper" :
        print("user Win")
        user_score += 1
        print("COMPUTER :",computer_score ," VS " , Name," :" ,user_score)

    elif computer_choise == "Rock" and user_choice == "Rock" :
        print("Draw")
        print("COMPUTER :",computer_score ," VS " , Name," :" ,user_score)

    elif computer_choise == "scisser" and user_choice == "paper" :
        print("computer Win")
        computer_score += 1
        print("COMPUTER :",computer_score ," VS " , Name," :" ,user_score)

    elif computer_choise == "scisser" and user_choice == "Rock" :
        print("user Win")
        user_score += 1
        print("COMPUTER :",computer_score ," VS " , Name," :" ,user_score)

    elif computer_choise == "scisser" and user_choice == "scisser" :
        print("Draw")
        print("COMPUTER :",computer_score ," VS " , Name," :" ,user_score)

    elif computer_choise == "paper" and user_choice == "Rock" :
        print("computer Win")
        computer_score += 1
        print("COMPUTER :",computer_score ," VS " , Name," :" ,user_score)

    elif computer_choise == "paper" and user_choice == "scisser" :
        print("user Win")
        user_score += 1
        print("COMPUTER :",computer_score ," VS " , Name," :" ,user_score)

    elif computer_choise == "paper" and user_choice == "paper" :
        print("Draw")
        print("COMPUTER :",computer_score ," VS " , Name," :" ,user_score)

    if computer_score == 3:
        print(Name," Game Over")
        break

    elif user_score == 3 :
        print(Name," Winer")
        break





