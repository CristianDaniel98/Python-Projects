from turtle import Turtle, Screen

x_pos = 0
timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

for _ in range(10):
    timmy.setx(100)
    #timmy.fd(2)
    x_pos += 20


screen = Screen()
screen.exitonclick()