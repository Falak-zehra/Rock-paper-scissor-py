import random
items = ["Rock" , "Paper ", "Scissor"]

user_choice= input("Choose Rock , Paper or Scissor\n")

comp_choice = random.choice(items)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice :
    print("Match Tie")

elif user_choice == "Rock"  :
    if comp_choice == "Paper":
        print("Computer won")

    else:
        print("You Won")
        
elif user_choice == "Paper" :
    if comp_choice == "Rock" :
        print("You won")
    else :
        print("Computer won")
        
elif user_choice == "Scissor" :
    if comp_choice == "Rock":
        print("Computer won")
    else :
        print("You won")
else :
    print("Wrong input")
    