"""problem set No.10 -List Comprehension
program that takes the list below and makes 
a new list that has only the even elements of this list in it."""

lists = [1,4,9,16,25,36,49,64,81,100]
even_lists = [x%2==0 for x in lists]
