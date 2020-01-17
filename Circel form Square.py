import turtle

my_turtle = turtle.Turtle()

#my_turtle.forward(100) #test
#my_turtle.right(90)    #test
#my_turtle.forward(100) #test

def square(size):
    
    for i in range(0,4):
        my_turtle.forward(size)
        my_turtle.right(90)

def circle(size):
    for n in range(0,100):
        square(size)
        my_turtle.right(10)
        

circle(100)
