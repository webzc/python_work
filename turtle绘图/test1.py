import turtle as tt
from random import randint
tt.TurtleScreen._RUNNING = True
tt.speed(0)  
tt.bgcolor("black")  
tt.setpos(-25, 25)  
tt.colormode(255)  
cnt = 0
while cnt < 1000:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tt.pencolor(r, g, b)  
    tt.forward(50 + cnt)
    tt.right(91)
    cnt += 1
tt.done()
