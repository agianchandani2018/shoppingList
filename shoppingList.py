#Author: Ami
#Date: Feb 23
#Assignment: Shopping List

f = open("list.txt", "r+")
list = f.readlines()
length = len(list)
#open and read the file. determined how many items are on the list initially
if length > 0:
	list[length-1] = list[length-1] + '\n'
#print(list)

print("You currently have {} items in your list".format(length))
item = "   "
#it does not matter what item equals at this point

#main body of program
while item != "":
	
	#this will now print the item to the list/screen
	print("Your shopping list contains: \n")
	number = 0
	while number < length:
		print ("{}. {}".format(number + 1, list[number]))
		number += 1
	
	
	item = input("What would you like to add? ")
	
	if len(item) > 0:  #if the user has entered an item
		list.append(item + "\n")   #add this item to ongoing list
		length += 1		

		if length == 1:
			f.write(item)
		else:
			f.write("\n" + item)
		#length += 1		

f.close()
#closes file

print("Your shopping list contains: \n")
#print(list) #just used for testing
#print(length) just used for testing
number = 0

while number < len(list):
	print ("{}. {}".format(number + 1, list[number]))
	number += 1
	#creates numbered list of items
