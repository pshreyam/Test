import random
list=['rock','paper','scissors']
print('The first element is : ',list[0])
print('The second element is : ',list[1])
print('The last element of a list is : ',list[-1])
print('The second last element of a list is : ',list[-2])
print("The initial list is: ",list)
##add new elements
list.append('hello')
print('The first element is : ',list[0])
print('The last element of a list is : ',list[-1])
print("The new list is: ",list)

boys=[]
boys.append('Eoin Morgan')
boys.append('Jos Buttler')
boys.append('Ajyinka Rahane')
boys.append('Rohit Sharma')
print('The last element is: ',boys[-1])
print('The new list is: ',boys)
##insert at a new position i.e. second position (index=1)
boys.insert(1,'Shreyas Iyer')
boys.insert(0,'Virat Kohli')
print(boys)
##delete first elements from list
del list[0]
print (list)
##pop removes the element from the list from the end
print(list.pop())
print(list)
##pop removing the element from the list from the first position 
print(list.pop(0))

#remove a value if value is knbown and not the position 
hero=['superman','spiderman','batman','hitman','kohliman','MSDman']
hero.remove('spiderman')
print(hero)
## sorts in alphabetical order
hero.sort()
print(hero)
##reverse sorts a list
hero.sort(reverse=True)
print(hero)
## to temprorarily show a sorted list but not change itself
print(sorted(hero))
#print in reverse order
hero.reverse()
print (hero)
#prints the length of the list
print(len(hero))


