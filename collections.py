myList = ["sam", "bob", "carl", ["sam", "sarah", "sindalia"]]
myDict = {
    "bob" : "Loves Chocolate",
    "sam" : "Loves Cream Cheese on a bagel",
    "carl" : "Devout Sushi Lover"
  }
myTuple = (55, 44, 33, 22, 11, 00)

#Accessing myList
firstListValue = myList[1]
secondListValue = myList[3][1]
print(firstListValue)
print(secondListValue)
print()

#Accessing myDict
firstDictItem = myDict["bob"]
print(firstDictItem)
print()

#Changing Dict value
myDict["sam"] = "Loves crackers"
print(myDict["sam"])
print()

#Accessing my tuple
print(myTuple[3])
