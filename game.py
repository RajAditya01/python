from turtle import *
import turtle

t=turtle.Turtle()

turtle.screensize(canvwidth=1000, canvheight=1000)


t.getscreen().bgcolor('white')
t.pencolor("white")


t.goto(250,50)
t.pencolor('black')
t.pensize(10)
t.pendown()
t.left(90)
t.forward(120)

t.circle(200,extent = 180)
t.forward(120)


t.left(30)
t.forward(100)
t.left(30)
t.forward(80)
t.left(90)
t.forward(60)

## trace backward
t.penup()
t.goto(250,50)
t.pendown()
t.right(60)
t.right(90)
t.right(30)
t.forward(100)
t.right(30)
t.forward(80)
t.right(90)
t.forward(60)

### right side nose
t.right(30)
t.forward(40)
t.left(90)
t.left(45)
t.forward(25)
t.backward(25)
t.left(45)
t.forward(40)
t.right(45)
t.forward(70)
t.right(90)
t.forward(70)
t.right(45)
t.forward(40)
t.right(90)
t.right(45)
t.forward(25)
t.penup()
### face complete


t.pencolor('black')
t.goto(250,50)
t.pendown()
t.fillcolor('black')########################################
t.begin_fill()
t.right(45)
#t.left(5)
t.forward(80)
t.left(20)


def right_beard1():
    for i in range(10):
  
        # Defining step by step curve motion
        t.right(0.8)
        t.forward(10)

right_beard1()

def right_beard2():
    for i in range(55):
  
        # Defining step by step curve motion
        t.right(1)
        t.forward(2)


right_beard2()


t.forward(200)
t.end_fill()
t.penup()


## half beard complete

## second half left side
t.goto(-150,50)
t.pendown()
t.fillcolor('black')########################################
t.begin_fill()
t.left(45)
#t.left(5)
t.forward(80)
t.right(20)

def right_beard1():
    for i in range(10):
  
        # Defining step by step curve motion
        t.left(0.8)
        t.forward(10)

right_beard1()

def right_beard2():
    for i in range(60):
  
        # Defining step by step curve motion
        t.left(1)
        t.forward(2)


right_beard2()

t.forward(233)
t.circle(40 ,extent = 90)
t.forward(10)
t.goto(250,50)
t.left(10)
t.right(60)
t.right(90)
t.right(30)
t.forward(100)
t.right(30)
t.forward(80)
t.right(90)
t.forward(60)

### right side nose
t.right(30)
t.forward(40)
t.left(90)
t.left(45)
t.forward(25)
t.backward(25)
t.left(45)
t.forward(40)
t.right(45)
t.forward(70)
t.right(90)
t.forward(70)
t.right(45)
t.forward(40)
t.right(90)
t.right(45)
t.forward(25)
t.backward(25)
t.right(45)
t.forward(40)
t.right(30)
t.forward(60)
t.right(90)
t.forward(80)
t.right(30)
t.forward(100)
t.end_fill()
t.penup()

## lips 
t.goto(0,-120)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.right(70)
t.left(10)
t.forward(30)
t.right(60)
t.forward(80)
t.right(60)
t.forward(30)
t.right(90)
t.forward(20)
t.right(90)
t.forward(15)
t.left(60)
t.forward(65)
t.left(60)
t.forward(15)
t.right(90)
t.forward(15)
t.end_fill()
t.penup()

#red mark

t.goto(250,50)
t.pendown()
t.pencolor('black')
t.right(60)
t.forward(120)
t.circle(200,extent = 60)
t.left(90)
t.pencolor('red')
t.fillcolor('red')
t.begin_fill()
t.forward(180)
t.left(60)
t.forward(200)
t.left(90)
t.circle(180,extent=20)
t.left(70)
t.forward(150)
t.right(60)
t.forward(135.75)
t.pencolor('black')
t.forward(2.25)
t.left(70)
t.circle(180,extent=23)
t.end_fill()
t.penup()

## right eyes
t.goto(100,130)
t.pendown()
t.pencolor('black')
t.left(60)
t.circle(15,extent=180)
t.left(10)
t.forward(50)
t.right(25)
t.forward(30)
t.right(10)
t.forward(20)
t.left(180)
t.right(20)
t.forward(20)
t.left(25)
t.forward(30)
t.left(30)
t.forward(50)
t.right(10)
t.forward(10)
t.right(10)
t.forward(10)
t.backward(10)

t.left(90)
t.forward(20)
t.left(30)
t.forward(25)
t.left(20)
t.forward(30)
t.left(60)
t.forward(32)
t.left(10)
t.forward(20)
t.penup()

t.fillcolor('white')
t.begin_fill()

t.goto(120,110)
t.right(55)
t.pendown()
t.pensize(8)
t.forward(45)
t.right(45)
t.forward(15)
t.right(90)
t.forward(15)
t.right(45)
t.forward(45)
t.right(45)
t.forward(25)
t.end_fill()
t.right(135)
t.pensize(8)
t.forward(30)
t.right(180)
t.fillcolor('black')
t.begin_fill()
t.circle(5)
t.end_fill()
t.penup()

### left eye
t.goto(-100,150)
t.pendown()
t.pensize(10)

t.right(180)
t.left(30)
t.forward(25)
t.right(45)
t.forward(40)
t.right(30)
t.forward(40)
t.left(10)
t.forward(10)
t.circle(15,extent=180)
t.penup()


t.goto(-80,158)
t.pendown()
t.right(180)
t.left(40)

t.right(20)
t.forward(30)
t.right(20)
t.forward(10)
t.right(10)
t.forward(30)
t.right(5)
t.forward(22)
t.left(90)
t.forward(5)
t.left(90)
t.forward(5)

## bootom part left eye

t.right(240)
t.forward(20)
t.right(30)
t.forward(25)
t.right(20)
t.forward(30)
t.right(60)
t.forward(32)
t.right(10)
t.forward(20)
t.penup()
t.goto(-10,115)
t.pendown()
t.left(50)

t.pensize(8)
t.forward(55)
t.left(45)
t.forward(15)
t.left(90)
t.forward(15)
t.left(50)
t.forward(45)
t.left(45)
t.forward(15)
t.left(90)
t.forward(10)
t.right(135)
t.pensize(8)
t.left(180)
t.forward(20)
t.fillcolor('black')
t.begin_fill()
t.circle(6)
t.end_fill()
t.penup()

### Ears right side

t.goto(250,50)
t.pendown()
t.right(90)
t.right(50)
t.circle(150,extent=45)
t.circle(20,extent=180)
t.forward(100)
t.penup()
t.goto(250,90)
t.pendown()
t.right(180)
t.right(45)
t.forward(30)
t.penup()

## left ear
t.goto(-153,40)
t.pendown()
t.right(135)
t.right(180)
t.forward(100)

t.circle(20,extent=180)
t.circle(150,extent=45)
t.penup()
t.goto(-153,80)
t.pendown()
t.left(180)
t.forward(25)
t.penup()
## to write the text

t.goto(400,200)
t.pendown()
t.color('#DD0808')
t.write("Aditya", font=(
      "algerain", 70, "bold"))
t.penup()

t.goto(400,100)
t.pendown()
t.color('#DB00FF')
t.write("Raj", font=(
      "algerain", 70, "bold"))
t.penup()


t.goto(480,-80)
t.pendown()
t.pencolor('black')
t.fillcolor('black')
t.begin_fill()
t.left(48)
t.forward(50)
t.left(90)
t.forward(180)
t.left(90)
t.forward(450)
t.left(90)
t.forward(180)
t.left(90)
t.forward(400)
t.end_fill()
t.penup()

t.goto(500,-250)
t.pendown()
t.color('#FACE1B')
t.write("Boy!!", font=(
      "algerain", 100, "bold"))
t.penup()

  
turtle.done()

