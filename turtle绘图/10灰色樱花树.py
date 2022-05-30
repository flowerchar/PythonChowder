
import turtle as T
from random import *
from math import *
def tree(n, l):
    T.pd()
    t = cos(radians(T.heading() + 45)) / 8 + 0.25
    T.pencolor(t, t, t)
    T.pensize(n / 4)
    T.forward(l)
    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 + 0.6)
        T.right(b)
        tree(n - 1, d)
        T.left(b + c)
        tree(n - 1, d)
        T.right(c)
    else:
        T.right(90)
        n = cos(radians(T.heading() - 45)) / 4 + 0.5
        T.pencolor(n, n, n)
        T.circle(2)
        T.left(90)
    T.pu()
    T.backward(l)
T.bgcolor(0.5, 0.5, 0.5)
T.ht()
T.speed(0)
T.tracer(0, 0)
T.left(90)
T.pu()
T.backward(300)
tree(13, 100)
T.done()
