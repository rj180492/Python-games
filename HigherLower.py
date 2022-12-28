import art
from game_data import data
import random
from replit import clear

print(art.logo)
score=0
def format_data(account):
  account_name=account["name"]
  account_descr=account["description"]
  account_country=account["country"]
  return f"{account_name} a {account_descr} from {account_country}"

def check_answer(guess,a_follower,b_follower):
  if (a_follower>b_follower):
    return guess=="a"
  else:
    return guess=="b"

account_b=random.choice(data)  
play_game=True

while play_game:
  account_a=account_b
  account_b=random.choice(data)
  if account_a==account_b:
    account_b=random.choice(data)

  print(f"Compare A {format_data(account_a)}")
  print(art.vs)
  print(f"Against B {format_data(account_b)}")
  
  guess=input('Who has higher follower A or B? ').lower()
  a_follower=account_a["follower_count"]
  b_follower=account_b["follower_count"]
  is_correct=check_answer(guess,a_follower,b_follower)

  if is_correct:
    score+=1
    clear()
    print(f'You are right.Current score: {score}')
    
  else:
    print(f'You are wrong.Final score: {score}')
    play_game=False
