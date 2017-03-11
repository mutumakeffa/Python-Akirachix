"""
Problem set No.7
program that asks the user for her name and age and greets her with
"Hello, name, you were born in 19xx." 

"""

import datetime

name = str(input("Please Enter Your Name : "))
age = int(input("Please Enter Your Age : "))

current_year = datetime.date.now().year
year_of_birth = current_year - age 

print ("Hello {}, You were born in {}".format(name, year_of_birth))