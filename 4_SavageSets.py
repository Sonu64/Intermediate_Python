"""
Savage_Sets.py, created just after creation of Dark_Dictionaries.py
"""


#Sets, only unique elements, unindexed, mutable, unordered, order is completely random and changes everytime on printing :|

#Creation
my_set = {"apple", "banana", "cherry"}
print(my_set)
foodList = ["Rice", "Dal", "Sabjee", "Chicken", "Rasogolla", "Rice"]
foodTuple = ["Masala Dosa", "Sambar", "Dahi Vada", "Upma", "Upma"]
name = "Sourakanti Mandal"
setFromList = set(foodList) #No Order
setFromTuple = set(foodTuple)
setFromString = set(name)
print(setFromList)
print(setFromTuple)
print(setFromString)
try:
    print(setFromString[3])
except:
    print("Sets are non indexable !!!")
    
    
#Creating empty sets
a = {} 
print(type(a)) #String, empty curly braces by default indicate Dictionary :()
b = set()
print(type(b)) #Set



#Adding elements using .add() method
nums = {1, 2, 3, 4, 5}
nums.add(6)
nums.add(6) # Doesn't affect 
print(nums)


#Deleting, .remove(), .discard(), .clear(), .pop()
pens = {"Agni", "Linc", "Reynolds", "Parkour"}
pens.remove("Linc")
print(pens)
# .remove() raises keyError if element not present in Set
# pens.remove("Totem") # KeyError
pens.discard("Reynolds")
pens.discard("Lovely Radium") #No error by .discard() if element not present, IGNORED !
print(pens)
poppedItem = pens.pop() #.pop() removes random element and returns it
print(poppedItem,"is removed.")
print(pens)
pens.clear() #clears entire set
print(pens)


#Checking for existence
numbers = {10, 20, 30}
if 70 in numbers:
    print("YES")
else:
    print("NO")


# Iterating over a set by using a for in loop, Order Unimportant !!
for number in numbers:
    print(number)
    
    
    
# Union and Intersection, just like Maths
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = {10, 20, 30, 40, 50}
# union() : combine elements from both sets, no duplication
# note that this does not change the two sets
AunionB = A.union(B)
print(AunionB)
# intersection(): take elements that are in both sets
AintersectionB = A.intersection(B)
print(AintersectionB) #10


#Difference
AminusB = A.difference(B) #remove elements from A those are not in B, here removes 10
print(AminusB) #A-B not same as B-A
# symmetric_difference() : returns a set with all the elements that are in A and B but not in both
AsymmdiffB = A.symmetric_difference(B)
print(AsymmdiffB)


#Copying Sets
#Again, simple assignment refers to address and can be fatal, so try to avoid !
perfectSquares = {4, 9, 16, 25, 36, 49, 64}
anotherPerfectSquares = perfectSquares.copy()
anotherPerfectSquares.add(81) #Original is unaffected :)
print(perfectSquares)
print(anotherPerfectSquares)



#Updating sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
# update() : Update the set by adding elements from another set, can be called unionUpdate :)
setA.update(setB)
print(setA)
# intersection_update() : Update the set by keeping only the elements found in both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.intersection_update(setB)
print(setA)
# difference_update() : Update the set by removing elements found in another set.
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.difference_update(setB)
print(setA)
# symmetric_difference_update() : Update the set by only keeping the elements found in either set (like doing an union), but not in both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.symmetric_difference_update(setB)
print(setA)
# Note: all update methods also work with other iterables as argument, e.g lists, tuples





#Subset, Superset, and Disjoint
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
# issubset(setX): Returns True if setX contains the set
print(setA.issubset(setB))
print(setB.issubset(setA)) # True

# issuperset(setX): Returns True if the set contains setX
print(setA.issuperset(setB)) # True
print(setB.issuperset(setA))

# isdisjoint(setX) : Return True if both sets have a null intersection, i.e. no same elements
setC = {7, 8, 9}
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))








#Frozenset
# Frozen set is just an immutable version of normal set. While elements of a set can be modified at any time, elements of frozen set remains the same after creation. Creation with: my_frozenset = frozenset(iterable)
# The following is not allowed:
# a.add(5)
# a.remove(1)
# a.discard(1)
# a.clear()
# a.update([1,2,3])
# Other set operations work
odds = frozenset({1, 3, 5, 7, 9})
evens = frozenset({0, 2, 4, 6, 8})
print(odds.union(evens)) #.update() will not work
print(odds.intersection(evens)) #.intersection_update() will not work
print(odds.difference(evens)) #.difference_update() will not work 
try:
    odds.update({11, 13})
except:
    print("FrozenSets can't be updated at any cost !")
