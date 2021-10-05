#A set is an arrange of elements unique and without order

my_set = {2, 4, 5, 8}
# my_set1 = {'hello', 28, True, 57, False, 'bye'}
my_set2 = {3, 5, 7, 2, 3} 


#When the console prints the sets, it will show them in different order
print(my_set)
# print(my_set1)
print(my_set2) #It will print only one 3

my_list = [1, 2, 4, 6, 6, 7, 8]
my_setlist = set(my_list) #It will convert the list into a set, and will eliminate the repeated element
print(list(my_setlist)) #It will convert the set into a list, again, but without the repeated elements

my_set3 = my_set | my_set2 #This operation will add all the elements of both sets, in a new set, eliminating the repeated 
print(my_set3)

my_set4 = my_set & my_set2 #This will add only the repeated elements into the new set
print(my_set4)

my_set5 = my_set - my_set2 #This will eliminate the elements of the set2 that exist in the set, will eliminate the repeated
print(my_set5)

my_set6 = my_set2 - my_set #Will eliminate the elements of the set that exist in the set2
print(my_set6)

my_set7 = my_set ^ my_set2 #This will add the elements of the both sets that aren't repeated
print(my_set7)