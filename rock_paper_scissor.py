import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images=[rock,paper,scissors]
u_choice=int(input('Enter your choice :0-Rock,1-Paper,2-Scissor '))
if u_choice>2 or u_choice<0:
  print('Invalid input')
else:
  print(game_images[u_choice])
  c_choice=random.randint(0,2)
  print(f'Computer choice {c_choice}')
  print(game_images[c_choice])

  if u_choice>2 or u_choice<0:
    print('Invalid input')
  elif u_choice==0 and c_choice==2:
    print('You win!')
  elif c_choice==0 and u_choice==2:
    print('You Lose!')
  elif u_choice>c_choice:
    print('You win!')
  elif u_choice==c_choice:
    print('Its a draw!')


  
