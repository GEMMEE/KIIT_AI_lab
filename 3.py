# 3. Write a method in python to display the elements of list thrice if it is a number and display
# the element terminated with '#' if it is not a number. For example, if the content of list
# is as follows: ThisList = ['41', 'DROND', 'GIRIRAJ', '13', 'ZARA']
# The output should be 
# 414141
# DROND#
# GIRIRAJ#
# 131313
# ZARA#

lst = eval(input("Enter a list:- "))
for i in lst:
	if i.isdigit():
		print(i*3)
	elif i.isalpha():
		print(i + "#")
