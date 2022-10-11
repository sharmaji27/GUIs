import turtle
turtle.getscreen()
chess = turtle.Turtle()
chess.penup()
chess.goto(-300, 330)
chess.pendown()
print('enter the n value and name of two colors')
n = int(input())
c1 = input()
c2 = input()
chess.speed(15)
for i in range(n):
    for j in range(n):
        if (j + i) % 2 == 0:
            chess.color('black',c1)
        else:
            chess.color('black', c2)
        chess.begin_fill()
        for k in range(4):
            chess.forward(80)
            chess.right(90)
        chess.end_fill()
        chess.forward(80)
    chess.penup()
    chess.goto(-300, 330 - (i + 1) * 80)
    chess.pendown()

turtle.done()
