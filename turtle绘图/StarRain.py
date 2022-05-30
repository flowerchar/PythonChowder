from turtle import *
from random import random,randint
from time import sleep
import pygame
pygame.init()
# pygame.mixer.music.load(r'C:\Users\DELL\PycharmProjects\StageTwo\game\dist\WTT\bg1.mp3')
# pygame.mixer.music.play(-1,0.0)
title('圣诞礼物')
def tree(d, s):
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    right(120)
    tree(d - 3, s * .5)
    right(120)
    color()
    backward(s)
    color(colors[randint(0, len(colors) - 1)])
colors = ['black','dimgray','grey','darkgrey','silver','lightgray','gainsboro',
          'whitesmoke','white','snow','rosybrown','lightcoral','indianred',
          'brown','firebrick','maroon','darkred','red','mistyrose','salmon',
          'tomato','darksalmon','coral','orangered','lightsalmon','sienna',
          'seashell','chocolate','saddlebrown','sandybrown','peachpuff','peru',
          'linen','bisque','darkorange','burlywood','antiquewhite','tan','navajowhite',
          'blanchedalmond','papayawhip','moccasin','orange','wheat','oldlace',
          'floralwhite','darkgoldenrod','goldenrod','cornsilk','gold','lemonchiffon',
          'khaki','palegoldenrod','darkkhaki','ivory','beige','lightyellow','lightgoldenrodyellow',
          'olive','yellow','olivedrab','yellowgreen','darkolivegreen','greenyellow',
          'chartreuse','lawngreen','honeydew','darkseagreen',
          'palegreen','lightgreen','forestgreen','limegreen','darkgreen','green','lime',
          'seagreen','mediumseagreen','springgreen','mintcream','mediumspringgreen',
          'mediumaquamarine','aquamarine','turquoise','lightseagreen','mediumturquoise',
          'azure','lightcyan','paleturquoise','darkslategray','teal','darkcyan','cyan',
          'aqua','darkturquoise','cadetblue','powderblue','lightblue','deepskyblue','skyblue',
          'lightskyblue','steelblue','aliceblue','dodgerblue','lightslategrey','slategray',
          'slategrey','lightsteelblue','cornflowerblue','royalblue','ghostwhite','lavender',
          'midnightblue','navy','darkblue','mediumblue','blue','slateblue','darkslateblue',
          'mediumslateblue','mediumpurple','blueviolet','indigo','darkorchid','darkviolet',
          'mediumorchid','thistle','plum','violet','purple','darkmagenta','fuchsia','magenta',
          'orchid','mediumvioletred','deeppink','hotpink','lavenderblush','palevioletred',
          'crimson','pink','lightpink']
number = numinput('不要关闭此弹窗哦', '请输入数字选择星星的颜色啦：\n'+
                                         '0->都有\n'+
                         '1->红色\n'+
                         '2->橙色\n'+
                         '3->黄色\n'+
                         '4->绿色\n'+
                         '5->青色\n'+
                         '6->蓝色\n'+
                         '7->紫色\n'+
                         "8->圣诞礼物"+
                  '什么也不选就是默认0啦', 0, 0, 8)
screen = Screen()
width ,height = 800,600
screen.setup(width,height)
screen.bgcolor("black")
screen.mode("logo")
screen.delay(0)#这里要设为0，否则很卡
t = Turtle(visible = False,shape='circle')
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.setheading(-90)
t.goto(width/2,randint(-height/2,height/2))
stars = []
if number == 0 :
    for i in range(141):
        star = t.clone()
        s =random() /3
        star.shapesize(s*2,s*2)
        star.speed(int(s*10))
        star.setx(width/2 + randint(1,width))
        star.sety( randint(-height/2,height/2))
        star.showturtle()
        star.color(colors[randint(0,len(colors)-1)])
        stars.append(star)
elif number == 1:
    for i in range(141):
        star = t.clone()
        s = random() / 3
        star.shapesize(s, s)
        star.speed(int(s * 10))
        star.setx(width / 2 + randint(1, width))
        star.sety(randint(-height / 2, height / 2))
        star.showturtle()
        star.color(colors[colors.index('red')])
        stars.append(star)
elif number == 2:
    for i in range(141):
        star = t.clone()
        s = random() / 3
        star.shapesize(s, s)
        star.speed(int(s * 10))
        star.setx(width / 2 + randint(1, width))
        star.sety(randint(-height / 2, height / 2))
        star.showturtle()
        star.color(colors[colors.index('orange')])
        stars.append(star)
elif number == 3:
    for i in range(141):
        star = t.clone()
        s = random() / 3
        star.shapesize(s, s)
        star.speed(int(s * 10))
        star.setx(width / 2 + randint(1, width))
        star.sety(randint(-height / 2, height / 2))
        star.showturtle()
        star.color(colors[colors.index('yellow')])
        stars.append(star)
elif number == 4:
    for i in range(141):
        star = t.clone()
        s = random() / 3
        star.shapesize(s, s)
        star.speed(int(s * 10))
        star.setx(width / 2 + randint(1, width))
        star.sety(randint(-height / 2, height / 2))
        star.showturtle()
        star.color(colors[colors.index('green')])
        stars.append(star)
elif number == 5:
    for i in range(141):
        star = t.clone()
        s = random() / 3
        star.shapesize(s, s)
        star.speed(int(s * 10))
        star.setx(width / 2 + randint(1, width))
        star.sety(randint(-height / 2, height / 2))
        star.showturtle()
        star.color(colors[colors.index('chartreuse')])
        stars.append(star)
elif number == 6:
    for i in range(141):
        star = t.clone()
        s = random() / 3
        star.shapesize(s, s)
        star.speed(int(s * 10))
        star.setx(width / 2 + randint(1, width))
        star.sety(randint(-height / 2, height / 2))
        star.showturtle()
        star.color(colors[colors.index('blue')])
        stars.append(star)
elif number == 7:
    for i in range(141):
        star = t.clone()
        s = random() / 3
        star.shapesize(s, s)
        star.speed(int(s * 10))
        star.setx(width/2 + randint(1,width))
        # star.setx(width)
        star.sety( randint(-height/2,height/2))
        # star.sety(0)
        star.showturtle()
        star.color(colors[colors.index('magenta')])
        stars.append(star)
elif number==8:
    n = 80.0
    # 设置速度快
    title("圣诞树")
    speed("fastest")
    # 背景颜色 海贝壳色，偏粉色
    screensize(bg='seashell')
    left(90)
    forward(3 * n)
    color("orange", "yellow")
    # color('black','dimgray','grey','darkgrey','silver','lightgray','gainsboro')

    begin_fill()
    left(126)

    for i in range(5):
        forward(n / 5)
        right(144)
        forward(n / 5)
        left(72)
    end_fill()
    right(126)

    color("dark green")
    backward(n * 4.8)
    tree(15, n)
    backward(n / 2)

    for i in range(200):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        up()
        forward(b)
        left(90)
        forward(a)
        down()
        if randint(0, 1) == 0:
            color('tomato')
        else:
            color('wheat')
        circle(2)
        up()
        backward(a)
        right(90)
        backward(b)
    sleep(60)
else:
    # for i in range(141):
    #     star = t.clone()
    #     s =random() /3
    #     star.shapesize(s,s)
    #     star.speed(int(s*10))
    #     star.setx(width/2 + randint(1,width))
    #     # star.setx(width)
    #     star.sety( randint(-height/2,height/2))
    #     # star.sety(0)
    #     star.showturtle()
    #     star.color(colors[randint(0,len(colors)-1)])
    #     stars.append(star)
    n = 80.0
    # 设置速度快
    title("圣诞树")
    speed("fastest")
    # 背景颜色 海贝壳色，偏粉色
    screensize(bg='seashell')
    left(90)
    forward(3 * n)
    color("orange", "yellow")
    # color('black','dimgray','grey','darkgrey','silver','lightgray','gainsboro')

    begin_fill()
    left(126)

    for i in range(5):
        forward(n / 5)
        right(144)
        forward(n / 5)
        left(72)
    end_fill()
    right(126)

    color("dark green")
    backward(n * 4.8)
    tree(15, n)
    backward(n / 2)

    for i in range(200):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        up()
        forward(b)
        left(90)
        forward(a)
        down()
        if random.randint(0, 1) == 0:
            color('tomato')
        else:
            color('wheat')
        circle(2)
        up()
        backward(a)
        right(90)
        backward(b)
    sleep(60)
while True:
    for star in stars:
        star.setx(star.xcor() - 3 * star.speed())
        if star.xcor()<-width/2:
            star.hideturtle()
            star.setx(width/2 + randint(1,width))
            star.sety( randint(-height/2,height/2))
            star.showturtle()
            # write("E", move=False, align='center', font=("微软雅黑", 30, 'normal'))

