import turtle
import time
from random import randint
from turtle import Turtle
#window
window= turtle.Screen()
window.title("Turtle Race")
window.bgcolor("lightgreen")

turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)

turtle.write("Turtle Race",font=("Arial",30,"bold"))
turtle.penup()

#Racing Track

turtle.setpos(-270,120)
turtle.color("sky blue")
turtle.begin_fill()
turtle.pendown()
turtle.forward(600)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(200)
turtle.end_fill()

#winnig line


stamp_size=20
square_size=15
finish_line=200

turtle.color('white')
turtle.shape('square')
turtle.shapesize(square_size / stamp_size)

turtle.penup()

for i in range(20):
   turtle.setpos(finish_line,(150-(i*square_size*1)))
   turtle.stamp()

turtle.hideturtle()



#turtle1

turtle1=Turtle()
turtle1.speed(0)
turtle1.color('black')
turtle1.shape('turtle')
turtle1.penup()
turtle1.goto(-250,100)
turtle1.pendown()



#turtle2

turtle2=Turtle()
turtle2.speed(0)
turtle2.color('yellow')
turtle2.shape('turtle')
turtle2.penup()
turtle2.goto(-250,50)
turtle2.pendown()


#turtle3

turtle3=Turtle()
turtle3.speed(0)
turtle3.color('pink')
turtle3.shape('turtle')
turtle3.penup()
turtle3.goto(-250,0)
turtle3.pendown()


#turtle4

turtle4=Turtle()
turtle4.speed(0)
turtle4.color('red')
turtle4.shape('turtle')
turtle4.penup()
turtle4.goto(-250,-50)
turtle4.pendown()



flag=0
time.sleep(1)

#lets start the Race.

for i in range (150):
   turtle1.forward(randint(1,5))
   #print (turtle1.pos()) 
   turtle2.forward(randint(1,5))
   turtle3.forward(randint(1,5))
   turtle4.forward(randint(1,5))
   if flag ==0 and turtle1.xcor()>200:
      flag =1
      print ("turtle 1( black) won the race")
      for turn in range(10):
        turtle1.right(36)
   if flag==0 and turtle2.xcor()>200:
      flag=1
      print ("turtle 2( yellow) won the race")
      for turn in range(10):
        turtle2.right(36)
   if flag==0 and turtle3.xcor()>200:
      flag=1
      print ("turtle 3( pink) won the race")
      for turn in range(10):
        turtle3.right(36)     
   if flag ==0 and turtle4.xcor()>200:
      flag =1
      print ("turtle 4( red) won the race")
      for turn in range(10):
        turtle4.right(36)

  
turtle.exitonclick()   
