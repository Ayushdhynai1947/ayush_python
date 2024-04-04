# more turtle Graphics , event listen ,state and multiple instaces


from turtle import Turtle,Screen


tim= Turtle()
screen = Screen()

def move_forword():
    tim.forward(10)
def move_backword():
    tim.backward(10)
def turn_left():
    # new_heading = tim.heading() +10
    # tim.setheading(new_heading)
    tim.left(10)
def turn_right():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forword,"w")
screen.onkey(move_backword,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")
"""onkey having two value key,fun used for perfoeming some action on screeen when user press a key"""
screen.exitonclick()