import time
name = input ("what's your name?")
name = name.capitalize()
print("Hello there, " + name)

name_len = len(name)

First_Letter= name[0]

Last_Letter= name[-1]

Missing_Letters = name[1:-1]

print ("Wow! your name is " + str(name_len) + " letters long!")
    
    
print ("The first letter of your name is " + str(First_Letter))

print ("The last letter of your name is " + str(Last_Letter).upper())


print ("The remaining letters of your name are " + str(Missing_Letters))







