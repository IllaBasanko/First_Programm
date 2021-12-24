from turtle import *
from random import *
''' отправляет черепах на заданные координаты'''
def start(default_turtle, x, y):
    default_turtle.goto(x,y)
'''заставляет черепах двигатся на рандомные растояния'''
def move(meme):
    meme.forward(randint(2,7))
''' 3 черепаха рисует финиш'''
def draw_finish():
    wasd.penup()
    wasd.goto(450,500)
    wasd.right(90)
    wasd.pendown()
    wasd.forward(1000)
'''заставляет выигравшию черепаху повернутся на 360 градусов'''
def winner(default):
    default.right(360)
'''создаёт трёх черепах'''
wasd = Turtle()
cactus = Turtle()
zmeya =  Turtle()
'''задаёт внешний вид черепахам'''
wasd.shape('turtle')
cactus.shape('turtle')
zmeya.shape('turtle')
wasd.color('red')
cactus.color('green')
zmeya.color('yellow')
cactus.penup()
zmeya.penup()

draw_finish()

start(cactus,- 450, 67)
start(zmeya,- 450, -67)
'''заставляет черепах двигатся пока одна из них не достигнет финиша'''
while zmeya.xcor()<=450 and cactus.xcor()<=450:
    move(cactus)
    move(zmeya)
"""если кактус достиг финиш первым то он выиграл иначе змея выиграла"""
if cactus.xcor() > zmeya.xcor():
    winner(cactus)
elif zmeya.xcor() > cactus.xcor():
    winner(zmeya)

exitonclick()

