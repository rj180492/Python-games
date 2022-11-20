from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)


def highest_bidder(dict):
  max_amt=0
  winner=''
  for bidder in dict:
    bid_amount=dict[bidder]
    if bid_amount>max_amt:
      max_amt=bid_amount
      winner=bidder
  print(f"The winner is ${winner} and bidding amount is ${max_amt}")

dict={}
bidding_cont=True

while bidding_cont:
  name=input('Enter your name ')
  bid=int(input('Enter your bid $'))
  dict[name]=bid
  next=input('Are there any other bidders?')
  if next=='yes':
    clear()

  else:
    bidding_cont=False
    highest_bidder(dict)
