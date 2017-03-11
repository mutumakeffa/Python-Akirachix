"""problem set no.1
program that accepts a list of numbers and returns the largest number"""

firstNo = int(input("Enter a number :"))
secondNo = int(input("Enter a number :"))
ThirdNo = int(input("Enter a number :"))
fourthNo = int(input("Enter a number :"))
FifthNo = int(input("Enter a number :"))

list_of_numbers = [firstNo, secondNo, ThirdNo, fourthNo, FifthNo]
for number in list_of_numbers:
	return max(list_of_numbers)
	print (max(list_of_numbers))