myDataCollection= ("Dymmy value")
print(type(myDataCollection))

myDataCollection= ("Dymmy value",)
print(type(myDataCollection))

fruits={"apple", "banana", "Cherry"}
print(fruits.add("kiwi")) #The print(fruit.add("kivi")) statement will print None 
#because the add method of a set does not return the set itself but None. #
# You should call fruit.add("kivi") on a separate line and then print the fruit set.
print(fruits)