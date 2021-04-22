# calculator that politely tell you when you will turn 100!!! :D

name = input("What's your name? ")

if len(name) >= 1:
    print ("Thank you, " + name + "!")
    time.sleep(1)
else:
    name = input("what's your name?")
    
birthyear = input("Now, what year were you born? ")
birthyear = int(birthyear)

output = 100 + birthyear

#Had a bit of trouble here
#Before figuring out that I had to turn the int back to str
print ("You will turn 100 in " + str(output) + "!")
