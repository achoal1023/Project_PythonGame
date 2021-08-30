import turtle as t
import random


screen = t.Screen()
screen.bgpic("01.gif")

# 울타리 그리기
mypen = t.Turtle()
mypen.penup()
mypen.setposition(-300, 300)
mypen.pendown()
mypen.pensize(3)

for x in range(4):
    mypen.speed(6)
    mypen.forward(600)
    mypen.right(90)

mypen.hideturtle()

########################################

### 기본 설정? ###

def r(): t.setheading(0)
def u(): t.setheading(90)
def l(): t.setheading(180)
def d(): t.setheading(270)


def z(): t.clear(), play()

def play():
    while True:
        t.forward(10)   # 내 속도 설정
        
        if t.xcor() > 270 or t.xcor() < -270:
            t.right(45)
        if t.ycor() > 270 or t.ycor() < -270:
            t.right(45)

        for count in range(maxBugs):        
            bugs[count].forward(5)

        for x in range(maxBugs):
            bugs[x]
            if bugs[x].xcor() > 270 or bugs[x].xcor() < -270:
                bugs[x].right(45)
            if bugs[x].ycor() > 270 or bugs[x].ycor() < -270:
                bugs[x].right(45)
        
        if (t.distance(bugs[0]) < 14) | (t.distance(bugs[1]) < 14) | (t.distance(bugs[2]) < 14)  | (t.distance(bugs[3]) < 14) | (t.distance(bugs[4]) < 14) | (t.distance(bugs[5]) < 14) | (t.distance(bugs[6]) < 14) | (t.distance(bugs[7]) < 14) | (t.distance(bugs[8]) < 14) | (t.distance(bugs[9]) < 14):
                # t.ontimer(play, 100)
                break

### 벌레 생성###
screen.addshape("pp1.gif")
maxBugs = 10
bugs = []
colors = ["red"]
shapes = ["pp1.gif"]

for count in range(maxBugs):
    c = random.randint(0,0)
    s = random.randint(0,0)
    bugs.append(t.Turtle())
    bugs[count].color(colors[c])
    bugs[count].shape(shapes[s])
    bugs[count].penup()
    bugs[count].speed(0)
    bugs[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
    bugs[count].right(random.randint(0, 360))
    if bugs[count].xcor() > 270 or bugs[count].xcor() < -270:
        bugs[count].right(45)
    if bugs[count].ycor() > 270 or bugs[count].ycor() < -270:
        bugs[count].right(45)




## player ##
screen.addshape("Red1.gif")
t.shape("Red1.gif")
t.color("black")
t.speed(0)
t.up()
t.onkey(r, "Right")
t.onkey(u, "Up")
t.onkey(l, "Left")
t.onkey(d, "Down")
t.onkey(z,"space")
t.listen()

# play()

t.mainloop()
