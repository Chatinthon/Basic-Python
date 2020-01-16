import turtle

my_turtle = turtle.Turtle()

#my_turtle.forward(100) #test
#my_turtle.right(90)    #test
#my_turtle.forward(100) #test

def square(lenght,angle):
    
    for i in range(0,4):
        my_turtle.forward(lenght)
        my_turtle.right(angle)

def circle(lenght,angle):
    for n in range(0,100):
        square(lenght,angle)
        my_turtle.right(10)
        

circle(100,90)

