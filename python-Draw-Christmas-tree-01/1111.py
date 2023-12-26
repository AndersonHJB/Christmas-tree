"""
长期招收编程一对一学员，微信：Jiabcdefh
公众号：AI悦创
"""

from turtle import *
import random
import time

n = 100.0
setup(500, 700, startx=None, starty=None)
# 画笔速度
speed("fastest")
# 背景颜色
screensize(bg='cornflowerblue')
# 画笔颜色，填充颜色
color("dark green")
fillcolor('yellow')
pensize(10)
# 画笔方向，向上
left(90)
# 每笔像素
forward(2.8*n)

# 随机生成颜色
def get_color():
    color_arr = ['light coral', 'tomato', 'orange red', 'red','brown',
    'firebrick','salmon', 'dark salmon','light salmon', 'orange',
    'chocolate','yellow','gold', 'goldenrod',
    'dark goldenrod', 'rosy brown','indian red', 'saddle brown',
    'dark orange','coral',  'hot pink', 'deep pink',
    'pink', 'light pink','pale violet red', 'maroon', 'medium violet red',
    'violet red','medium orchid']

    index = random.randint(0,len(color_arr)) - 1
    return color_arr[index]

# 画雪花
def snow(snow_count):
    hideturtle()
    pensize(2)
    for i in range(snow_count):
        pencolor("white")
        pu()
        goto(random.randint(-180, 180), random.randint(-180, 340))
        pd()
        dens = random.randint(10, 12)
        snowsize = random.randint(6, 10)
        for _ in range(dens):
            forward(snowsize)  # 向当前画笔方向移动snowsize像素长度
            backward(snowsize)  # 向当前画笔相反方向移动snowsize像素长度
            right(360 / dens)  # 顺时针移动360 / dens度

# 飘落名字
def name(name_count):
    hideturtle()
    pensize(2)
    for i in range(name_count):
        pencolor(get_color())
        pu()
        goto(random.randint(-220, 220), random.randint(-300, 340))
        pd()
        # 这里可以换成自己的名字、自己想要的词语
        name_arr = ['猫','宁一','平安','喜乐']
        namesize = random.randint(10, 15)
        index = random.randint(0,len(name_arr)) - 1
        dens = random.randint(10, 12)
        write(name_arr[index], align="right", font=("Arial", namesize, "bold"))

# 画星星
def koc(size):
  pensize(3)
  pencolor(get_color())
  begin_fill()
  fillcolor('yellow')
  for i in range(5):
      left(72)
      fd(size)
      right(144)
      fd(size)
  end_fill()

# 画树干
backward(n*4.8)
def tree(d, s):
    if d <= 0: return
    if d == 1:
        koc(5)
    pensize(d)
    forward(s)
    tree(d-1, s*.81)
    right(120)
    tree(d-3, s*.5)
    right(120)
    tree(d-3, s*.5)
    right(120)
    backward(s)
    color("dark green")

# 执行函数
tree(14, n)
snow(40)
name(15)

# 写Merry Christmas文字
penup()
seth(0)
goto(190, -305)
pendown()
color("red")
write("Merry Christmas", align="right", font=("Arial", 50, "bold"))

done()