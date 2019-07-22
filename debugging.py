Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##In order complete this challenge you need to debug the following code.
##It may be easier to do so if you improve the code quality. 
##copy and paste this code into a new file named “debugging.py”

import tutle # imports the turtle library

yp7 = turtle.clone() #this creates a new turtle and stores it in a variable
t = 200
b = -200

#draw the letter ‘A’

turtle.hideturtle() # this hides the arrow of the turtle called turtle


yp7.pendown()


yp7.goto(-1000,0)


yp7.penup()

a,c = yp7.pos()

yp7.goto(a,c)

yp7.pendown()
yp7.goto(a+100, c+300)
yp7.goto(a+200, c)
yp7.goto(a+30, c+100)


yp7.goto(a+300, c+100)

turtle.manloop() # all turtle commands must go before this line!!!

SyntaxError: multiple statements found while compiling a single statement
>>> 
