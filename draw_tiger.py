# coding=utf-8
from turtle import *
import time

COLOR = '#B2814D'


def set_start(x, y, w, c=COLOR):
    penup()
    setx(x)
    sety(y)
    setheading(towards(0, 0))
    width(w)
    pencolor(c)
    pendown()
    speed(0)


def left_rotate(time, angle, length):
    for i in range(time):
        left(angle)
        forward(length)


def right_rotate(time, angle, length):
    for i in range(time):
        right(angle)
        forward(length)


def draw_circle(radius, color, color2=''):
    if color2 == '':
        color2 = color
    penup()
    setheading(towards(0, 0))
    right(90)
    pencolor(color)
    pendown()
    begin_fill()
    circle(radius)
    fillcolor(color2)
    end_fill()


def fill_color(color):
    def decorator_all(func):
        def wrapper(*args, **kwargs):
            begin_fill()
            func(*args, **kwargs)
            fillcolor(color)
            end_fill()
        return wrapper
    return decorator_all


def fill_color_patch(x, y, c='#fffffb'):
    set_start(x, y, 1, c=c)
    forward(1)


def head_outline():
    set_start(0, -40, 2.5)
    right(90)
    left_rotate(5, 3, 14)
    left_rotate(5, 8, 8)
    left_rotate(10, 5, 6.5)
    left_rotate(5, 5.5, 10)
    left_rotate(25, 4, 10)
    left_rotate(6, 5.5, 5)
    left_rotate(7, 3, 7)
    left_rotate(5, 10, 8)
    left_rotate(5, 3, 14)


@fill_color('#fdb933')
def draw_head():
    head_outline()
    pencolor('#CDCDCD')
    goto(0, -40)


@fill_color('#fffffb')
def draw_face():
    set_start(0, -40, 2.5)
    right(90)
    left_rotate(5, 3, 14)
    left_rotate(1, 80, 2.5)
    pencolor('#fffffb')
    left_rotate(12, 5, 6.5)
    left_rotate(5, 6, 15)
    left_rotate(5, 5, 10)
    left_rotate(5, 12, 10)
    backward(0.5)
    left(65)
    pencolor(COLOR)
    backward(3)
    left_rotate(5, 3, 14)
    forward(5)


def draw_moustache():
    fill_color_patch(-41, -31)
    begin_fill()
    set_start(-41, -31, 2.5)
    right(180)
    left_rotate(4, 20, 4)
    left_rotate(1, 90, 8)
    right(150)
    left_rotate(4, 25, 3)
    forward(6)
    left_rotate(1, 110, 5.5)
    right(165)
    left_rotate(4, 15, 3.2)
    left(150)
    right_rotate(3, 30, 2.2)
    right_rotate(1, 105, 5)
    left(130)
    right_rotate(6, 5, 1.8)
    right_rotate(1, 130, 2)
    left(60)
    left_rotate(2, 30, 1)
    left_rotate(4, 28, 4)
    fillcolor('#fffffb')
    end_fill()
    set_start(-45, -28, 2.5)
    right(70)
    left_rotate(5, 2.5, 4)
    left_rotate(4, 9, 3)
    left_rotate(5, 3, 4.5)


def draw_mouth():
    set_start(-17, 22, 2.5)
    right_rotate(1, 45, 14)
    left_rotate(1, 85, 35)
    left_rotate(1, 70, 7)
    set_start(-17, 22, 2.5)
    right_rotate(1, 45, 14)
    right_rotate(1, 78, 36)
    right_rotate(1, 65, 6)
    set_start(-17, 22, 2.5)
    right_rotate(1, 45, 14)
    left_rotate(1, 85, 30)
    right_rotate(1, 108, 12)
    right_rotate(1, 140, 5)
    set_start(-17, 22, 2.5)
    right_rotate(1, 45, 14)
    right_rotate(1, 75, 28)
    left_rotate(1, 85, 10)
    left_rotate(1, 130, 8)
    set_start(3, 0, 2.5)
    left(90)
    right_rotate(5, 5, 4.8)
    right_rotate(4, 18, 1.8)
    left_rotate(1, 3, 27)
    right_rotate(4, 18, 1)
    right_rotate(1, 15, 22)
    right(88)
    right_rotate(9, 1, 4.5)
    begin_fill()
    set_start(3, 0, 2.5)
    left(90)
    right_rotate(4, 5, 4.8)
    right_rotate(1, 5, 2)
    right_rotate(1, 67, 37)
    right_rotate(1, 86, 18)
    fillcolor('#f15a22')
    end_fill()
    begin_fill()
    set_start(3, 0, 2.5)
    pencolor('#aa2116')
    left(90)
    right_rotate(2, 5, 6)
    right(120)
    left_rotate(10, 6, 2)
    right(55)
    left_rotate(11, 5.5, 1.8)
    right_rotate(1, 110, 10)
    right(100)
    right_rotate(9, 1, 4.5)
    fillcolor('#aa2116')
    end_fill()
    set_start(3, 0, 2.5)
    left(90)
    right_rotate(5, 5, 4.8)
    right_rotate(4, 18, 1.8)
    left_rotate(1, 3, 27)
    right_rotate(4, 18, 1)
    right_rotate(1, 15, 22)
    right(88)
    right_rotate(9, 1, 4.5)
    set_start(21, 10, 1, c='#fdb933')
    draw_circle(2.3, '#fdb933')
    set_start(10, 16, 1, c='#fdb933')
    draw_circle(2.3, '#fdb933')
    set_start(21, 19, 1, c='#fdb933')
    draw_circle(2.3, '#fdb933')
    set_start(-57, 16, 1, c='#fdb933')
    draw_circle(2.3, '#fdb933')
    set_start(-51, 24, 1, c='#fdb933')
    draw_circle(2.3, '#fdb933')
    set_start(-64, 24, 1, c='#fdb933')
    draw_circle(2.3, '#fdb933')


def draw_nose():
    set_start(6, 37, 1)
    pencolor('#e0861a')
    right(150)
    begin_fill()
    left_rotate(6, 3, 4)
    left_rotate(6, 15, 3)
    left_rotate(6, 3, 4)
    fillcolor('#e0861a')
    end_fill()
    set_start(6, 37, 1.5)
    right(120)
    begin_fill()
    left_rotate(5, 4, 4)
    left_rotate(3, 10, 3)
    left_rotate(5, 4, 4)
    left_rotate(7, 15, 0.8)
    left_rotate(5, 4, 4)
    left_rotate(5, 8, 2)
    left_rotate(5, 4, 4)
    left_rotate(7, 15, 0.8)
    fillcolor('#b4532a')
    end_fill()
    set_start(-16, 36, 1)
    pencolor('#d1923f')
    right(75)
    begin_fill()
    right_rotate(4, 15, 2)
    right_rotate(5, 26, 1)
    right_rotate(4, 15, 2)
    right_rotate(5, 26, 1)
    fillcolor('#d1923f')
    end_fill()
    set_start(-25, 25, 1)
    pencolor('#130c0e')
    left(110)
    begin_fill()
    left_rotate(6, 15, 1.5)
    left_rotate(5, 15, 1)
    fillcolor('#130c0e')
    end_fill()
    set_start(-10, 24, 1)
    pencolor('#130c0e')
    left(175)
    begin_fill()
    right_rotate(6, 15, 1.2)
    right_rotate(5, 15, 1)
    fillcolor('#130c0e')
    end_fill()


def draw_eye():
    set_start(-50, 34, 1, c='#130c0e')
    left(115)
    begin_fill()
    left_rotate(8, 6.5, 7)
    left_rotate(5, 15, 7)
    left_rotate(5, 10, 5.5)
    left_rotate(5, 15, 6)
    left_rotate(5, 5, 9.5)
    left_rotate(4, 30, 2)
    fillcolor('#130c0e')
    end_fill()
    set_start(-57, 40, 1, c='#fffffb')
    left(112)
    begin_fill()
    left_rotate(8, 6.5, 5)
    left_rotate(5, 15, 6)
    left_rotate(5, 10, 4.5)
    left_rotate(5, 15, 5)
    left_rotate(5, 6.5, 7)
    left_rotate(4, 15, 2)
    fillcolor('#fffffb')
    end_fill()
    set_start(-90, 62, 1, c='#563624')
    draw_circle(15, '#563624')
    set_start(-84, 59, 1, c='#130c0e')
    draw_circle(9, '#130c0e')
    set_start(-90, 63, 1, c='#fffffb')
    draw_circle(3.5, '#fffffb')
    set_start(16, 25, 1, c='#130c0e')
    right(150)
    begin_fill()
    right_rotate(8, 6.5, 7)
    right_rotate(5, 15, 7)
    right_rotate(5, 10, 5.5)
    right_rotate(5, 15, 6)
    right_rotate(5, 5, 9.5)
    right_rotate(4, 30, 2)
    fillcolor('#130c0e')
    end_fill()
    set_start(24, 28, 1, c='#fffffb')
    right(135)
    begin_fill()
    right_rotate(8, 7, 5)
    right_rotate(5, 15, 5.5)
    right_rotate(5, 10, 4.5)
    right_rotate(5, 15, 4.5)
    right_rotate(5, 6.5, 6.5)
    right_rotate(4, 13, 2)
    fillcolor('#fffffb')
    end_fill()
    set_start(57, 48, 1, c='#563624')
    draw_circle(15, '#563624')
    set_start(53, 44, 1, c='#130c0e')
    draw_circle(9, '#130c0e')
    set_start(38, 47, 1, c='#fffffb')
    draw_circle(3.5, '#fffffb')


def draw_brow():
    set_start(12, 88, 1, c='#130c0e')
    right(82)
    begin_fill()
    left_rotate(3, 3, 5)
    right_rotate(5, 4, 6)
    right_rotate(7, 24, 2.3)
    right_rotate(3, 5, 4.5)
    left_rotate(1, 90, 8)
    left(95)
    left_rotate(3, 8, 5)
    right_rotate(3, 25, 1.2)
    right_rotate(3, 11, 1.5)
    right_rotate(3, 25, 1.2)
    right_rotate(3, 3, 4.5)
    left_rotate(1, 85, 7)
    left_rotate(1, 90, 15)
    right_rotate(5, 30, 2.2)
    right_rotate(3, 9, 6)
    right_rotate(6, 3, 5)
    right_rotate(8, 18, 1.3)
    right_rotate(3, 10, 5.3)
    left_rotate(1, 90, 8)
    left(112)
    right_rotate(3, 3, 4.5)
    right_rotate(3, 25, 1)
    right_rotate(3, 10, 1.5)
    right_rotate(3, 28, 1)
    left_rotate(3, 5, 3)
    left_rotate(3, 25, 1)
    left_rotate(3, 5, 1.8)
    left_rotate(1, 90, 17)
    right_rotate(3, 35, 0.8)
    right_rotate(3, 10, 3)
    fillcolor('#130c0e')
    end_fill()
    set_start(88, -16, 1, c='#130c0e')
    begin_fill()
    right_rotate(5, 15, 3)
    right_rotate(4, 5.5, 3)
    right_rotate(3, 28, 1)
    right_rotate(5, 6, 4)
    fillcolor('#130c0e')
    end_fill()
    set_start(106, 9, 1, c='#130c0e')
    right(15)
    begin_fill()
    right_rotate(5, 5, 5.5)
    right_rotate(5, 29, 3)
    right_rotate(5, 5, 4.5)
    fillcolor('#130c0e')
    end_fill()
    set_start(110, 36, 1, c='#130c0e')
    left(20)
    begin_fill()
    right_rotate(3, 10, 2)
    right_rotate(3, 10, 6)
    right_rotate(5, 29, 2)
    forward(20)
    fillcolor('#130c0e')
    end_fill()
    set_start(75, 76, 1, c='#130c0e')
    right(105)
    begin_fill()
    left_rotate(5, 10, 4)
    right_rotate(6, 28, 2)
    right_rotate(5, 10, 5)
    right_rotate(6, 25, 2)
    fillcolor('#130c0e')
    end_fill()
    set_start(-75, 100, 1, c='#130c0e')
    right(108)
    begin_fill()
    right_rotate(3, 3, 8)
    right_rotate(4, 35, 2)
    right_rotate(8, 9, 3.2)
    fillcolor('#130c0e')
    end_fill()
    set_start(-145, 58, 1, c='#130c0e')
    right(30)
    begin_fill()
    left_rotate(5, 15, 5)
    left_rotate(3, 18, 3)
    left(92)
    right_rotate(4, 5, 6)
    right_rotate(1, 5, 4)
    fillcolor('#130c0e')
    end_fill()
    set_start(-148, 46, 1, c='#130c0e')
    left(40)
    begin_fill()
    right_rotate(5, 10, 6.5)
    right_rotate(4, 32, 2)
    right_rotate(4, 10, 6.5)
    fillcolor('#130c0e')
    end_fill()
    set_start(-138, 7, 1, c='#130c0e')
    left(10)
    begin_fill()
    left_rotate(5, 8, 4)
    left_rotate(6, 20, 1.5)
    left_rotate(4, 8, 4.5)
    fillcolor('#130c0e')
    end_fill()
    head_outline()


def draw_ear():
    set_start(101, 74, 2.5)
    left(150)
    begin_fill()
    left_rotate(5, 6, 3)
    left_rotate(5, 12, 5)
    left_rotate(3, 13, 12)
    left_rotate(5, 12, 7)
    left_rotate(4, 16, 5)
    fillcolor('#fdb933')
    end_fill()
    set_start(94, 89, 1, c='#f3715c')
    right(168)
    begin_fill()
    left_rotate(5, 17, 6)
    left_rotate(4, 20, 5)
    goto(94, 89)
    fillcolor('#f3715c')
    end_fill()
    set_start(-125, 98, 2.5)
    right(165)
    begin_fill()
    right_rotate(5, 6, 3)
    right_rotate(5, 12, 5)
    right_rotate(3, 13, 12)
    right_rotate(5, 12, 7)
    right_rotate(4, 16, 4.5)
    fillcolor('#fdb933')
    end_fill()
    set_start(-115, 110, 1, c='#f3715c')
    left(160)
    begin_fill()
    right_rotate(5, 17, 6)
    right_rotate(4, 20, 5.5)
    goto(-115, 110)
    fillcolor('#f3715c')
    end_fill()
    head_outline()


def draw_cap():
    set_start(55, 123, 2.5)
    right(150)
    left_rotate(13, 11, 12)
    set_start(18, 170, 2.5)
    right(180)
    begin_fill()
    left_rotate(10, 16, 4)
    fillcolor('#130c0e')
    end_fill()
    set_start(55, 123, 2.5)
    right(150)
    begin_fill()
    left_rotate(13, 11, 12)
    fillcolor('#FF0000')
    end_fill()
    set_start(55, 123, 2.5)
    right(113)
    begin_fill()
    left_rotate(15, 5, 8.6)
    fillcolor('#228B22')
    end_fill()
    set_start(30, 142, 2.5)
    right(170)
    left_rotate(18, 8.9, 5)
    set_start(-2, 150, 2.5)
    left(178)
    right_rotate(4, 5, 6)
    set_start(55, 123, 2.5)
    begin_fill()
    goto(50.13, 124.56)
    setheading(148.5)
    left_rotate(12, 4, 10)
    fillcolor('#fdb933')
    end_fill()


def draw_shadow():
    fill_color_patch(75, -155)
    _draw_shadow()


@fill_color('#fab27b')
def _draw_shadow():
    set_start(75, -155, 1, c='#fab27b')
    left_rotate(5, 8, 5)
    left_rotate(10, 4, 10)
    left_rotate(5, 6, 9)
    left_rotate(4, 30, 4.5)
    left_rotate(5, 3.5, 16)
    left_rotate(3, 3.5, 18)
    left_rotate(3, 8, 5)
    left_rotate(4, 20, 1.5)
    goto(75, -155)


def draw_body():
    fill_color_patch(0, -40)
    set_start(0, -40, 2.5)
    right(90)
    begin_fill()
    left_rotate(2, 3, 14)
    width(2.4)
    goto(53, -74)
    pencolor('#87481f')
    left(20)
    right_rotate(5, 16, 1.3)
    right_rotate(4, 8, 8)
    right_rotate(1, 15, 2)
    right_rotate(1, 30, 7)
    right_rotate(3, 28, 2)
    right_rotate(1, 5, 4)
    right_rotate(1, 90, 6)
    right_rotate(1, 180, 10)
    right_rotate(3, 5, 8)
    right_rotate(3, 10, 6.5)
    right_rotate(2, 15, 2)
    right_rotate(4, 7, 4.5)
    left_rotate(2, 18, 1)
    left_rotate(4, 12, 5)
    left_rotate(4, 15, 3)
    left_rotate(4, 7, 4)
    right_rotate(1, 82, 2)
    right_rotate(4, 8, 7)
    right_rotate(2, 12, 2)
    right_rotate(4, 28, 1.5)
    right_rotate(1, 10, 6)
    right_rotate(1, 60, 4.5)
    right(170)
    right_rotate(5, 10, 5)
    right_rotate(10, 2.5, 5)
    goto(-71.81, -32.68)
    setheading(345.5)
    width(2.5)
    pencolor(COLOR)
    left_rotate(2, 3, 14)
    fillcolor('#fdb933')
    end_fill()
    set_start(0, -42, 1)
    right(90)
    pencolor('#fffffb')
    begin_fill()
    right_rotate(5, 12, 5)
    right_rotate(3, 13, 15)
    right_rotate(3, 25, 12)
    backward(1)
    right(23)
    left_rotate(3, 15, 6)
    right(5)
    right_rotate(3, 20, 11)
    right_rotate(3, 15, 12)
    right_rotate(3, 15, 10)
    right_rotate(1, 15, 20)
    fillcolor('#fffffb')
    end_fill()
    set_start(37, -125, 1)
    pencolor('#130c0e')
    begin_fill()
    right_rotate(1, 5, 8)
    right_rotate(4, 30, 1.5)
    right_rotate(1, 20, 6)
    fillcolor('#130c0e')
    end_fill()
    set_start(29, -130, 1)
    pencolor('#130c0e')
    begin_fill()
    left(20)
    right_rotate(2, 5, 5)
    left_rotate(4, 30, 1.5)
    left_rotate(2, 10, 4)
    right_rotate(3, 20, 2)
    left(155)
    left_rotate(3, 8, 5)
    fillcolor('#130c0e')
    end_fill()
    set_start(-62, -139, 1)
    pencolor('#130c0e')
    begin_fill()
    right(65)
    left_rotate(2, 10, 4)
    left_rotate(3, 25, 1.5)
    left_rotate(1, 10, 2)
    left_rotate(3, 28, 1.5)
    right_rotate(3, 10, 3.5)
    fillcolor('#130c0e')
    end_fill()
    set_start(-71, -118, 1)
    pencolor('#130c0e')
    begin_fill()
    right(50)
    left_rotate(4, 10, 2.5)
    left_rotate(5, 28, 1.5)
    right_rotate(3, 10, 2.5)
    fillcolor('#130c0e')
    end_fill()
    set_start(-75, -94, 1)
    pencolor('#130c0e')
    begin_fill()
    right(30)
    left_rotate(4, 10, 2.5)
    left_rotate(5, 28, 1.5)
    right_rotate(3, 10, 2.5)
    fillcolor('#130c0e')
    end_fill()


def draw_left_hand():
    set_start(0, -40, 2.5)
    right(90)
    left_rotate(4, 3, 14)
    left_rotate(1, 3, 8)
    right_rotate(1, 33, 3)
    begin_fill()
    left_rotate(1, 0, 4)
    left_rotate(3, 7, 7)
    left_rotate(4, 18, 3.8)
    set_start(103, -26, 2.5)
    right_rotate(3, 20, 4.5)
    right_rotate(3, 20, 2.5)
    right_rotate(2, 20, 2)
    right_rotate(2, 18, 5)
    right_rotate(5, 30, 1.5)
    right_rotate(1, 5, 8)
    right_rotate(1, 180, 2)
    right_rotate(2, 40, 3.5)
    set_start(106, -8, 2.5)
    right(90)
    right_rotate(2, 10, 4)
    right_rotate(4, 24, 3)
    right_rotate(2, 10, 4)
    right_rotate(2, 20, 5)
    right_rotate(5, 26, 1.2)
    right_rotate(2, 10, 4)
    right_rotate(1, 190, 4)
    right_rotate(1, 90, 3)
    set_start(128, -12, 2.5)
    left(155)
    right_rotate(3, 20, 5.5)
    right_rotate(2, 25, 1.5)
    right_rotate(1, 25, 4)
    right_rotate(3, 25, 2)
    right_rotate(2, 10, 3)
    set_start(124, -30, 2.5)
    left(150)
    right_rotate(8, 25, 2)
    right_rotate(1, 15, 3)
    right_rotate(2, 28, 2)
    set_start(115, -35, 2.5)
    left(100)
    right_rotate(5, 26, 1.8)
    right_rotate(1, 25, 5)
    set_start(103, -31, 2.5)
    left(135)
    right_rotate(5, 10, 5)
    right_rotate(4, 15, 6)
    left_rotate(1, 100, 7)
    right(120)
    right_rotate(3, 12, 2.5)
    left(170)
    right_rotate(3, 15, 3)
    right(110)
    right_rotate(3, 12, 3)
    left(140)
    right_rotate(3, 12, 3)
    right(120)
    right_rotate(3, 10, 3.5)
    left_rotate(1, 125, 10)
    right_rotate(3, 23, 3)
    right_rotate(3, 9, 9.5)
    fillcolor('#fdb933')
    end_fill()
    set_start(115, -35, 2.5)
    left(100)
    begin_fill()
    right_rotate(5, 26, 1.8)
    right_rotate(1, 25, 5)
    pencolor('#fffffb')
    width(1)
    left(90)
    right_rotate(4, 40, 2)
    left(90)
    right_rotate(4, 40, 1)
    left_rotate(1, 135, 5)
    right(80)
    right_rotate(3, 26, 4.5)
    right(130)
    left_rotate(3, 28, 3)
    fillcolor('#fffffb')
    end_fill()
    set_start(61, -33, 1)
    left(118)
    pencolor('#130c0e')
    begin_fill()
    right_rotate(3, 5, 3.5)
    right_rotate(4, 32, 1.5)
    right_rotate(3, 12, 2.7)
    fillcolor('#130c0e')
    end_fill()
    set_start(78, -36, 1)
    left(110)
    pencolor('#130c0e')
    begin_fill()
    left_rotate(3, 5, 3.5)
    right(50)
    right_rotate(4, 20, 1)
    right_rotate(5, 10, 3)
    fillcolor('#130c0e')
    end_fill()
    set_start(94, -35, 1)
    left(125)
    pencolor('#130c0e')
    begin_fill()
    left_rotate(3, 5, 2)
    right(50)
    right_rotate(4, 25, 2)
    right_rotate(3, 10, 2.2)
    fillcolor('#130c0e')
    end_fill()


def draw_right_hand():
    fill_color_patch(-44.24, -37.54)
    set_start(-44.24, -37.54, 2.5)
    setheading(351.5)
    begin_fill()
    right(177)
    right_rotate(4, 3, 14)
    right(3)
    goto(-106, -22)
    set_start(-106, -22, 2.5)
    right(175)
    right_rotate(3, 5, 5.5)
    right_rotate(3, 22, 4)
    right(80)
    left_rotate(2, 25, 4)
    left_rotate(4, 35, 5.5)
    left_rotate(3, 30, 1.5)
    left_rotate(3, 20, 2)
    left_rotate(1, 10, 2.5)
    right(120)
    left_rotate(3, 20, 2.5)
    set_start(-143, -2, 2.5)
    left(120)
    left_rotate(4, 25, 3.5)
    left_rotate(1, 35, 3)
    left_rotate(2, 15, 3)
    left_rotate(5, 22, 3.5)
    left_rotate(2, 20, 2.5)
    set_start(-155, -7, 2.5)
    left(170)
    left_rotate(2, 35, 3.5)
    left_rotate(2, 12, 4.5)
    left_rotate(3, 28, 4)
    left_rotate(3, 10, 3)
    left_rotate(3, 28, 3.5)
    set_start(-158, -27, 2.5)
    right(130)
    left_rotate(3, 30, 2.5)
    left_rotate(4, 13, 4)
    left_rotate(4, 35, 2.5)
    set_start(-135, -25, 2.5)
    right(95)
    left_rotate(3, 12, 9)
    left_rotate(4, 12, 4)
    right_rotate(1, 90, 8)
    left(120)
    left_rotate(3, 12, 3)
    right(160)
    left_rotate(3, 10, 4)
    left(120)
    left_rotate(3, 12, 3.5)
    right(145)
    left_rotate(3, 10, 3.5)
    left(125)
    left_rotate(3, 10, 3.5)
    right_rotate(1, 135, 10)
    fillcolor('#fdb933')
    end_fill()
    fill_color_patch(-107, -23)
    begin_fill()
    set_start(-107, -23, 1)
    pencolor('#130c0e')
    right(90)
    right_rotate(3, 3, 3.5)
    left_rotate(5, 25, 1)
    left_rotate(3, 15, 3.2)
    fillcolor('#130c0e')
    end_fill()
    fill_color_patch(-122, -25)
    begin_fill()
    set_start(-122, -25, 1)
    pencolor('#130c0e')
    right(120)
    left_rotate(3, 5, 2)
    left_rotate(4, 30, 1.4)
    left_rotate(3, 15, 3)
    fillcolor('#130c0e')
    end_fill()


def draw_clothes():
    set_start(0, -40, 2.5)
    right(90)
    begin_fill()
    left_rotate(3, 3, 14)
    goto(47.57, -36.43)
    setheading(94.25)
    left(171)
    left_rotate(3, 9, 9.5)
    left_rotate(1, 9, 3)
    left_rotate(2, 23, 2.5)
    right(150)
    left_rotate(3, 10, 5)
    right_rotate(3, 10, 10)
    right_rotate(1, 20, 4)
    right_rotate(2, 10, 4)
    right(90)
    left_rotate(5, 5, 10)
    fillcolor('#FF0000')
    end_fill()
    set_start(0, -40, 2.5)
    right(90)
    begin_fill()
    left_rotate(1, 3, 14)
    left_rotate(1, 3, 13)
    right(88)
    right_rotate(5, 5, 10)
    goto(21.85, -91.11)
    setheading(197.25)
    right_rotate(1, 20, 4)
    right_rotate(2, 10, 4)
    right(90)
    left_rotate(5, 5, 10)
    fillcolor('#228B22')
    end_fill()
    set_start(-44.24, -37.54, 2.5)
    setheading(351.5)
    begin_fill()
    right(177)
    right_rotate(2, 3, 14)
    right_rotate(1, 3, 7)
    left(65)
    left_rotate(4, 7, 10)
    left_rotate(3, 6, 10)
    left_rotate(1, 0, 2)
    left(128)
    right_rotate(6, 7, 6.1)
    right_rotate(2, 7, 6.1)
    left(125)
    right_rotate(5, 4, 11)
    fillcolor('#FF0000')
    end_fill()
    set_start(-44.24, -37.54, 2.5)
    setheading(351.5)
    begin_fill()
    right(177)
    right_rotate(1, 3, 14)
    right_rotate(1, 3, 8)
    left(92)
    left_rotate(4, 8, 7)
    right(10)
    right_rotate(4, 3, 6)
    goto(-59.29, -87.30)
    setheading(2.5)
    right_rotate(2, 7, 6.1)
    left(125)
    right_rotate(5, 4, 11)
    fillcolor('#228B22')
    end_fill()


def draw_tail():
    set_start(53, -74, 2.4, c='#87481f')
    begin_fill()
    setheading(26)
    right_rotate(5, 16, 1.3)
    right_rotate(1, 8, 8)
    right_rotate(1, 8, 4)
    left(60)
    right_rotate(1, 3, 3)
    pencolor(COLOR)
    forward(5)
    right_rotate(4, 3, 8)
    left_rotate(3, 3, 7)
    left_rotate(2, 5, 3)
    left_rotate(5, 6, 6)
    left_rotate(3, 8, 7)
    left_rotate(5, 12, 6)
    left_rotate(5, 10, 6)
    left_rotate(5, 15, 2)
    left_rotate(2, 20, 2)
    left_rotate(3, 10, 3)
    right_rotate(2, 13, 5)
    right_rotate(2, 20, 6)
    right_rotate(2, 12, 6)
    right_rotate(5, 7.5, 5)
    right_rotate(6, 3, 4)
    left_rotate(4, 2, 8.5)
    fillcolor('#fdb933')
    end_fill()
    set_start(53, -74, 2.4, c='#87481f')
    begin_fill()
    setheading(26)
    right_rotate(5, 16, 1.3)
    right_rotate(1, 8, 8)
    right_rotate(1, 8, 3)
    left(60)
    right_rotate(1, 3, 2)
    pencolor('#130c0e')
    left_rotate(3, 25, 2)
    left_rotate(3, 5, 1.8)
    left_rotate(1, 78, 8.5)
    fillcolor('#130c0e')
    end_fill()
    set_start(83, -81, 1, c='#130c0e')
    begin_fill()
    left(140)
    right_rotate(5, 8, 2)
    left_rotate(1, 105, 5)
    right_rotate(2, 3, 5.5)
    left(50)
    left_rotate(3, 15, 4.1)
    fillcolor('#130c0e')
    end_fill()
    set_start(109, -89, 1, c='#130c0e')
    begin_fill()
    left(150)
    right_rotate(3, 5, 2)
    right_rotate(4, 15, 2)
    left_rotate(1, 125, 6)
    left_rotate(2, 3, 7)
    left(85)
    left_rotate(3, 15, 6.05)
    left(68)
    right_rotate(3, 5, 5)
    fillcolor('#130c0e')
    end_fill()
    set_start(132, -88, 1, c='#130c0e')
    begin_fill()
    left(180)
    right_rotate(5, 10, 4.1)
    left_rotate(1, 100, 6)
    left_rotate(2, 5, 7)
    left(75)
    left_rotate(5, 10, 5)
    left(75)
    right_rotate(3, 8, 4.5)
    fillcolor('#130c0e')
    end_fill()
    set_start(150, -71, 1, c='#130c0e')
    begin_fill()
    right(140)
    right_rotate(5, 15, 5.8)
    left_rotate(1, 130, 6)
    left_rotate(2, 10, 5)
    left(30)
    left_rotate(5, 15, 5.6)
    left(81)
    right_rotate(3, 8, 3)
    fillcolor('#130c0e')
    end_fill()
    set_start(147, -51, 1, c='#130c0e')
    begin_fill()
    right(125)
    right_rotate(5, 10, 4)
    left(145)
    left_rotate(2, 10, 6.5)
    left_rotate(6, 14, 2)
    left_rotate(4, 22, 2)
    fillcolor('#130c0e')
    end_fill()


def draw_drum():
    set_start(-136, -12, 2, c='#87481f')
    begin_fill()
    right_rotate(1, 78, 17)
    right_rotate(5, 30, 1.2)
    right_rotate(1, 30, 17)
    fillcolor('#FF0000')
    end_fill()
    set_start(-140, -2, 2, c='#87481f')
    begin_fill()
    left_rotate(1, 108, 10)
    right_rotate(1, 90, 4)
    left_rotate(5, 16, 7)
    left_rotate(5, 19, 6.5)
    forward(4)
    left_rotate(5, 18, 7.5)
    left_rotate(5, 18, 6.1)
    left_rotate(1, 180, 3)
    left_rotate(1, 95, 10)
    fillcolor('#FF0000')
    end_fill()
    set_start(-156.34, 48.19, 1, c='#87481f')
    setheading(199)
    left(12)
    left_rotate(10, 14.5, 5.8)
    set_start(-140, 12, 1, c='#87481f')
    setheading(20)
    begin_fill()
    left_rotate(5, 14, 5.2)
    left_rotate(3, 15, 4.5)
    left_rotate(5, 18, 5)
    left_rotate(5, 16, 5.5)
    left_rotate(3, 18, 5)
    fillcolor('#fffffb')
    end_fill()
    set_start(-143, 14, 2.5, c='#FF0000')
    left_rotate(1, 117, 17)
    left_rotate(1, 90, 9)
    left(90)
    left_rotate(3, 5, 3.5)
    set_start(-146.8, 14, 2.5, c='#FF0000')
    left_rotate(1, 120, 14)
    set_start(-150, 34, 2.5, c='#FF0000')
    left_rotate(1, 120, 8.5)
    left(100)
    left_rotate(3, 17, 4)
    set_start(-140, 16, 2.5, c='#FF0000')
    left_rotate(1, 115, 14)
    right_rotate(1, 90, 13)
    right(90)
    right_rotate(4, 16, 4.5)
    set_start(-136, 18, 2.4, c='#FF0000')
    left_rotate(1, 112, 12)
    set_start(-142, 24, 2.5, c='#FF0000')
    left_rotate(1, 35, 10)
    set_start(-145, 32, 2.5, c='#FF0000')
    left_rotate(1, 115, 6)
    right_rotate(1, 85, 10)
    right(40)
    right_rotate(3, 18, 2)
    right_rotate(1, 95, 10)
    set_start(-149, 44, 2.5, c='#FF0000')
    left(60)
    right_rotate(3, 22, 3)
    set_start(-166, 20, 2.4)
    right(100)
    right_rotate(4, 32, 3)
    right_rotate(2, 12, 3.5)
    left_rotate(2, 10, 4)
    left_rotate(4, 25, 2.5)
    set_start(-196, 35, 2.4)
    draw_circle(3.5, COLOR, '#FF0000')
    set_start(-127, 38, 2.4)
    left(60)
    right_rotate(4, 32, 3)
    right_rotate(2, 12, 3.5)
    left_rotate(6, 28, 2)
    left_rotate(3, 15, 2)
    set_start(-115, 33, 2.4)
    draw_circle(3.5, COLOR, '#FF0000')


if __name__ == '__main__':
    title('PythonDrawTiger(公众号：Python碎片)')
    setup(420, 400, 150, 150)
    screensize(400, 380, '#FFE4E1')
    time.sleep(3)
    draw_head()
    draw_face()
    draw_eye()
    draw_nose()
    draw_mouth()
    draw_ear()
    draw_cap()
    draw_brow()
    draw_shadow()
    draw_body()
    draw_moustache()
    draw_left_hand()
    draw_right_hand()
    draw_clothes()
    draw_tail()
    draw_drum()
    set_start(1000, 1000, 2.5)
    done()
