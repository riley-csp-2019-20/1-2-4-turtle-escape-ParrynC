import turtle as trtl
import random 

maze_painter = trtl.Turtle()
player = trtl.Turtle()
maze_painter.speed(100)
path_width = 10
distance = 30
wall_width = 15
door_width = 15

def drawDoor():
    maze_painter.penup()
    maze_painter.forward(door_width)
    maze_painter.pendown()

def drawBarrier():
    maze_painter.left(90)
    maze_painter.forward(wall_width*2)
    maze_painter.backward(wall_width*2)
    maze_painter.right(90)

#Maze
for i in range(25):
    if i > 4:
        door = random.randint(door_width,distance-2*door_width)
        barrier = random.randint(2*wall_width,distance-2*door_width)

        #Door First
        if door < barrier:
            maze_painter.forward(door)
            drawDoor()
            maze_painter.forward(barrier-door-door_width)
            drawBarrier()   
            maze_painter.forward(distance-barrier)
        
        #Barrier First
        else:
            maze_painter.forward(barrier)
            drawBarrier()
            maze_painter.forward(door-barrier)
            drawDoor()
            maze_painter.forward(distance-door-door_width)


    maze_painter.left(90)
    distance += wall_width


#player
def playerup():
    maze_painter.setheading(90)
    maze_painter.forward(10)



def playerdown():
    maze_painter.setheading(270)
    maze_painter.forward(10)




def playerleft():
    maze_painter.setheading(180)
    maze_painter.forward(10)



    
def playerright():
    maze_painter.setheading(0)
    maze_painter.forward(10)



wn = trtl.Screen()

wn.onkeypress(playerup, "Up")
wn.onkeypress(playerdown, "Down")
wn.onkeypress(playerleft, "Left")
wn.onkeypress(playerright, "Right")
wn.listen()
wn.mainloop()