from turtle import Turtle,Screen
import random
race_start=False
screen=Screen()
screen.setup(height=400,width=500)
user_choice= screen.textinput(title='Make your bet',prompt='Which turtle will win race? Enter your choice')
colors=['red','blue','green','yellow','orange','purple']
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]
for turtle_index in range(0,6):
  t=Turtle(shape='turtle')
  t.color(colors[turtle_index])
  t.penup()
  t.goto(x=-230,y=y_positions[turtle_index])
  all_turtles.append(t)

if user_choice:
  race_start=True
while race_start:
  for turtle in all_turtles:
    if turtle.xcor()>230:
      race_start=False
      winning_color=turtle.pencolor()
      if winning_color==user_choice:
        print(f'You won! The winner is {winning_color}')
      else:
        print(f'You Lose! The winner is {winning_color}')
  
    turtle.forward(random.randint(1,10))
    
screen.exitonclick()
