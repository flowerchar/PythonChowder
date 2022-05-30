# 导入所依赖的库
from turtle import *
import random
import time
import pygame
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
pygame.init()
# pygame.mixer.music.load(r'C:\Users\DELL\PycharmProjects\StageTwo\game\dist\WTT\bg1.mp3')
# pygame.mixer.music.play(-1,0.0)
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
    color(colors[random.randint(0, len(colors) - 1)])

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
time.sleep(60)
