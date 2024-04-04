# # basic import
# import turtle
# tim = turtle.Turtle()


# # from import
# from turtle import Turtle,Screen,Shape

# tim = Turtle()
# tom =Turtle()
# teery = Turtle()
# tim.shape("turtle")
# tim.color("red")


# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

   
# # timmy_the_tutle.forward(100)
# # timmy_the_tutle.right(90)
# # timmy_the_tutle.forward(100)
# # timmy_the_tutle.right(90)
# # timmy_the_tutle.forward(100)

# # screen = Screen()
# # screen.exitonclick()
    

#     #from turtle start *
# from turtle import *



# # alia module 
# import turtle as t
# tim  = t.turtles()


# installing modules heroes
# import heroes

# print(heroes.gen())


####################################
# import turtle as t 


# tim = t.Turtle()
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


################petagon shape
# import turtle as t
# import random

# tim = t.Turtle()

# # num_sides = int(input("enter input"))


# colours =["teal","dark cyan","wheat","light steel blue"," bisque","plum","dark salmon"]

# def draw_shape(num_sides): 
#      angle =360 /num_sides
#      for _ in range(num_sides):

#         tim.forward(100)
#         tim.right(angle)


# for shape_side_n in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)



#############RANDOM WALK####################
# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)

# ########### Challenge 4 - Random Walk ########
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color


# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))



##### pattern######
# import turtle as t
# tim = t.Turtle()



# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#      tim.color(c)
#      tim.forward(steps)
#      tim.right(30)
#      tim.color('red')
#     tim.fillcolor('yellow')


# import turtle as t
# from random import random

# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)







########circle print########
import turtle as t
import random


tim = t.Turtle()
t.colormode(255)

########### Challenge 4 - Random Walk ########
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color



tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 /size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()

