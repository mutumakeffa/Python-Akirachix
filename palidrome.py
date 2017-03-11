"""problem set 11 
program that determines if a string or a number is a palidrome"""
x = input ("Please Enter a word or a number :")
y = x[::-1]

if x == y:
	print ("Is a Palidrome")
else:
	print ("Is not a Palidrome")

