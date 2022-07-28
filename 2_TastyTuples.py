"""TastyTuples,  created on the day after JEE Mains 2nd attempt, check dates :) """
# Tuples : Immutable unlike lists, sometimes more efficient #

myTuple = ("Sonu", "Monu", "Gonu")
print(type(myTuple))
print(myTuple)

print("\n-------------------\n")

#Single element Tuples should include comma at end, otherwise a STRING !!
notATuple = ("Sonu")
print(type(notATuple))
print(notATuple)
print("----------------")
nowATuple = ("Sonu",)
print(type(nowATuple))
print(nowATuple)

print("\n-------------------\n")


#Creating Tuples from lists and vice-versa
fruits = ["Apple", "Orange", "Banana"]
tupleFromList = tuple(fruits) #Tuple from List using tuple() function
print(fruits)
print(type(fruits))
print("----------------")
print(tupleFromList)
print(type(tupleFromList))
listFromTuple = list(tupleFromList) #List from List using list() function
print(listFromTuple)
print(type(listFromTuple))

print("\n-------------------\n")

#Indexing same as lists
thisIsATuple = ("Alpha", "Beta", "Gamma", "Delta")
print(thisIsATuple[2]) #Gamma
print(thisIsATuple[-1]) #Delta
for element in thisIsATuple:
    print("I Love",element) #Space automatically added for comma concatenation !
    
print("\n-------------------\n")


#Other Methods
years = [2019, 2020, 2021, 2022, 2022, 2022]
print(len(years)) #6
print(years.count(2022)) #3
print(years.index(2022)) #First occurence of 2022 is at index 3, #3

print("\n-------------------\n")

#Slicing same as lists
favs = ("Biriyani", "Fuchka", "Chicken", "Rasogolla", "Kachori")
print(favs)
first3Favs = favs[0:3] #include 0th and exclude 3rd (upto 2nd index)
print(first3Favs) #Everything is Tuple otherwise

print("\n-------------------\n")

#Reverse with trick
houses = ("Mine", "her", "His")
reversedHouses = houses[::-1]
print(houses)
print(reversedHouses) # One doesnt affect other, same as Lists !

print("\n-------------------\n")

#Unpacking Tuples
subjects = ("Physics", "Chemistry", "Mathematics")
p, c, m = subjects #Number of elements must match !!!
print(p)
print(c)
print(m)

print("\n-------------------\n")

#Unpacking with one bunch as List
phyTopics = ("Mechanics", "Heat", "Waves", "Electrodynamics", "Optics", "Modern Physics")
mecha, *remainingTopics = phyTopics #NOTE: Multiple Star Operations Not Allowed !!!!
print(mecha)
print(remainingTopics)


#List vs Tuple MEMORY_USAGE
import sys
foodList = ["Rice", "Moong Dal", "Mixed Veg", "Rasogolla"] # Lovely Vegan Indian :)
foodTuple = ("Rice", "Moong Dal", "Mixed Veg", "Rasogolla") 
print("Memory used by List is", sys.getsizeof(foodList),"bytes.")
print("Memory used by Tuple is", sys.getsizeof(foodTuple),"bytes.")
print("Tuple WINS !")


print("\n-------------------\n")


#List vs Tuple TIME_OF_EXECUTION
import timeit # Nothing to worry about it now, creates a thing 'number' number of times and prints time needed for it
print(timeit.timeit(stmt="[0, 1, 2]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2)", number=1000000))
print("Tuple Wins !")

