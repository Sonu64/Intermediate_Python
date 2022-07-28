"""
Lesson 1: Lovely Lists, prepared and uploaded the day after JEE Main 2nd attempt !
Describes Lists with the most useful List methods !

"""

myList = ["apple", "orange"]
print(myList)
myList.append("lemon")
myList.insert(1, "blueberry")
print(myList)

popped = myList.pop()
print(popped)
print(myList)

myList.remove("blueberry")
# print(blueberryRemoved)
print(myList)

newList = list()
newList = myList # Simple assigning like this refers to address, change to any one affects the other
print(newList)

# myList.clear()
# print(myList)

myList.reverse()
print(myList)
print(newList)

print("-----------------------------")

newList.append("this was added to newList !")
print(newList)
print(myList)


new = list()

for element in myList:
    new.append(element)
    
new.insert(0, "New element only added to 'new' !! ")
print("myList is : ", myList)
print("newList is : ", newList)
print("new is ", new)


toBeAddedList = ["Sonu"] * 5
new = new + toBeAddedList
print(new)


print("\n\n")
print("--------------------------------")

favs = ["Biriyani", "Fuchka", "Chicken", "Rasogolla", "Kachori"]
print(favs)
first3Favs = favs[0:3] #include 0th and exclude 3rd (upto 2nd index)
print(first3Favs)


favsReversed = favs[::-1] #step of -1 reverses list
print(favsReversed)

print("\n\n---------------------")

#Different way of copying than for loop without pointer issue to original List, just us the ''list()'' function ! EASY !!
copyOfFavs = list(favs)
copyOfFavs.append("Appended to copyOfFavs only")
print(favs)
print(copyOfFavs)

print("\n\n---------------------")
# ~~~~~ LIST COMPREHENSION ~~~~~ #
nums = [1, 2, 3, 4, 5]
squares = [number*number for number in nums] # pretty good one-liner syntax, isn't it ?
print(nums)
print(squares)
