import random
#To count your Total score
score = []
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
stop = False
#Below range(n): n denotes how many times you wanna play
for i in range(6):
    print("your choice 1.rock 2.paper 3.scissor")
    choice = int(input("enter your choice"))
    
    if choice == 1:
        you = "rock"
        your_choice = 1
        print("your choice is rock")
    elif choice == 2:
        you = "paper"
        your_choice = 2
        print("your choice is paper")
    elif choice == 3:
        you = "scissor"
        your_choice = 3
        print("your choice is scissor")

    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp = "rock"
        print("computer choice is rock")
    elif comp_choice == 2:
        comp = "paper"
        print("computer choice is paper")
    elif comp_choice == 3:
        comp = "scissor"
        print("computer choice is scissor")
    print(you,"vs",comp)
    
    if comp_choice == your_choice:
        print("you won")
        score.append(1)
    else:
        print("you lose")
total_score = score.count(1)
print("your total score is",total_score)