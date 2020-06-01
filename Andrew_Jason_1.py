
#1   Notice that if you use a "#" that comments out the line and that code wont be run!

#2   save your name to a variable 

D = "Dustin"

#3    print your name to the console, using the variable and the string of your name. 

#print(D)
#print("Dustin")

#4    Notice that a string is iterable, meaning that you can count through the characters of it. The first letter is in the zero position

print(D[0])
print(D[1])
print(D[3])

#5    How many letters do you have in your name? save that to a variable called nameLength

nameLength = len(D)
print("I have this many letters in my name:")
print(nameLength)

#6    you can add (concatenate) strings together. 

FirstName = "Dustin"
LastName = "Perry"
Middle = "M"

Fullname = FirstName + Middle + LastName + "IV"
print(Fullname)

#7     you cannot add a string and a interger together

#K = Fullname + 6
#print(K)


#8     you can add intergers together, math is all that is. 


four_plus_five = 4 + 5

four_times_five = 4 * 5 

print("Four + Five is :")
print(four_plus_five)
print("Four times Five is :")
print(four_times_five)


#9   Do you think this will work?   Isn't that a string + an integer? Make the integer a string and it should work.

#print("Four plus five is " + four_plus_five)
#print("Four times five is " + four_times_five)












#git init
#git add README.md
#git commit -m "first commit"
#git remote add origin https://github.com/2dperry24/PythonIntro.git
#git push -u origin master