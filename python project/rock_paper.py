import random
print()
print("~~~~~~----WELCOME IN THE ROCK--*--PAPER---**--SCISSOR---*--GAME---~~~~~~")
print()
members = int(input("HOW MANY MEMBERS ARE THERE IN YOUR PROJECT WORK ARE:-  "))
for i in range(1,members+1):
    a = input("Enter The "+ str(i)+" Member Name Of This Project Is :- " )
user_score = 0
comp_score = 0
ties = 0
print("""
WINNING RULES ARE:
1.Paper Vs Rock ---> Paper
2.Rock Vs Scissors ---> Rock
3.Paper Vs Scissors ---> Scissors """)
print()
print("""
Choices are:
1.Rock
2.Paper
3.Scissors""")
print()
while True:
    choice = int(input("Enter your choice from 1-3: "))
    print()
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input"))
    if choice == 1:
        user_choice = "Rock"
    elif choice ==2:
        user_choice = "Paper"
    else:
        user_choice = "Scissors"

    print("The user's choice is",user_choice)
    print("Now it is Computer's turn")

    computer = random.randint(1,3)

    if computer == 1:
        comp_choice ="Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"

    print("The computer's choice is ",comp_choice)

    if ((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
        print("Paper wins")
        result = "Paper"
    elif ((user_choice == "Rock" and comp_choice == "Scissors")or (user_choice == "Scissors" and comp_choice == "Rock")):
        print("Rock wins")
        result = "Rock"
    elif (user_choice == comp_choice):
        print("its a tie")
        result = "Tie"
    else:
        print("Scissors wins")
        result = "Scissors"
    if result == "Tie":
        ties +=1
    elif result == user_choice:
        print("user wins")
        user_score +=1
    else:
        print("computer win")
        comp_score +=1

    print("Scores are")
    print("user's score is",user_score)
    print("computer's score is",comp_score)
    print("ties are ",ties)
    repeat = input("do you want to play again?")
    print()
    if repeat == "No" or repeat == "NO" or repeat == "no" :
        break
print("Game over !!")
print("Thanks")