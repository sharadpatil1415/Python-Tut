import random

choo =[ """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
,
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
,

 """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""" ]





print ("Welcome to Rock, paper, Scissor")
user_input = input ("what You Choose rock = r, paper = p, Scissor = s :")


if user_input == "r":
    user_choice = 0
elif user_input == "p":
    user_choice = 1
elif user_input == "s":
    user_choice = 2
else:
    print("choose valid option")
    exit()


comp_choice = random.randint(0, 2)


print("\nuser choice : ")
print(choo[user_choice])

print("computer choice :")
print(choo[comp_choice])


if user_choice == comp_choice:
    print("Tie")
elif (user_choice == 0 and comp_choice == 2) or \
     (user_choice == 1 and comp_choice == 0) or \
     (user_choice == 2 and comp_choice == 1):
    print("You win!")
else:
    print("Computer wins!")







