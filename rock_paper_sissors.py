import random

user = input("Enter r for rock | p for paper | s for scissors: ")
if user == 'r':
    user_output = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
elif user == 'p':
    user_output = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
elif user =='s':
    user_output = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
else:
    user_output = "Please enter either r | p | s, You Lose"
    
rand_num = random.randint(1,12)
if rand_num <=4:
    computer = 'r'
elif rand_num <=8:
    computer = 'p'
else:
    computer = 's'

if computer == 'r':
    computer_output = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
elif computer == 'p':
    computer_output = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
elif computer =='s':
    computer_output = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("You are {}".format(user_output))
print("Computer is: {}".format(computer_output))

#Logic
if user == computer:
    print()
    print("It is a draw")
    print()
elif user == 'r' and computer == 's':
    print()
    print("You Win")
    print()
elif user == 's' and computer == 'p':
    print()
    print("You Win")
    print()
elif user == 'p' and computer == 'r':
    print()
    print("You Win")
    print()
else:
    print()
    print("You Lose")
    print()

# print("You are {}".format(user))
# print("Computer is: {}".format(computer))

#rock > scissors
#scissors > paper
#paper > rock


