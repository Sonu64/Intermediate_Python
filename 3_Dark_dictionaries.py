"""
Dark_dictionaries, created 1 day after JEE Mains 2nd attempt :) Now time to grind hard for JEE Advanced and give one last try :)
"""
#Dictionaries, key-value pairs, mutable

#creating basics
data = {"name":"Sonu", "batch":"JEE 2022", "favSub":"Physics"}
print(data)
data2 = dict(name="Sonu", favChapter="Heat")
print(data2)

#mutating
data2["worstChapter"] = "Optics"
print(data2)
data2["worstChapter"] = "Waves"
print(data2)

#deleting
del(data2["worstChapter"])
print(data2)
data2.pop("favChapter") # or use data2.popelement() to remove last key value pair :)
print(data2)


#Checking a key exists or not
#use if in statements
exams = {"Sonu":"JEE", "Nimbu":"NEET", "Subha":"JEE", "Shanu":"NEET"}
if "Sonu" in exams:
    print("Sonu gives",exams["Sonu"],".")
else:
    print("No Sonu !")
#or use try except
try:
    print("Aakash gives ",exams["Aakash"],".")
except:
    print("No Aakash !")
    
    
#Looping through a dictionary
for element in exams.keys():
    print(element)
for element in exams.values():
    print(element)
for student, exam in exams.items():
    print(student,"will give",exam,"exam.")


#Copying dictionaries, SIMPLE ASSIGN. WILL REFER ADDRESS AGAIN, AND CHANGE IN ONE WILL AFFECT THE OTHER :(
copy1 = exams.copy()
copy1["new"] = "Value Added to copy1"
print(copy1)
print(exams)
copy2 = dict(exams)
copy2["new"] = "Value Added to copy2"
print(copy2)
print(exams)



#Updating dictionaries
info = {"name":"Sonu", "age":"19", "email":"sonusantu64@gmail.com"}
print(info)
updatedInfo = dict(name="Eshita", age="18") #skipped key is email, it isn't updated
info.update(updatedInfo)
print(info)


#Using numbers as keys
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print("Square of 5 is",squares[5],".")


#Using Tuples as keys
sums = {(2, 3):5, (3, 4):7, (4, 6):10}
print(sums[(3, 4)])
# But mind it you can't use Lists as keys as they are mutable
