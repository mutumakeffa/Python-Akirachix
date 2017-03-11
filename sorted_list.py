"""problem set No.5 
function that accepts a list of words then 
prints them sorted in alphabetical order"""


list = []
def sorted_list(list):
	word = str(input("Enter a Word :"))
	list.append(word)
	list.sort()
	return list
