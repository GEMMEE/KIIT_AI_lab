'''
4. Write a definition of a method count_now(places) to find and display those place names,
in which there are more than 5 characters. For example,
If the list places contains
['DELHI', 'LONDON', 'PARIS', 'NEW YORK', 'DUBAI']
The ff should get displayed:
LONDON
NEW YORK
'''

def display(lst):
	for a in lst:
		if len(a) > 5:
			print(a)

mylist = ['DELHI', 'LONDON', 'PARIS', 'NEW YORK', 'DUBAI']
display(mylist)

