# Loops For loop and While Loop 
# For loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.

# for i in rnge (1, 50):
#     print(i)

#i=1
# while i < 50:
#     print(i)
#     i += 1
#     if i == 15:
#         break
#     else:
#         continue
#     print("I am inside the loop")



n=5
result = 1 

# for i in range(1, n + 1): 
#     result *= i 
#     print(result)
# print(result)


# while n > 0:
#     result *= n
#     n -= 1
# print(result)

# 5=5*4*3*2*1=120
# 10=10*9*8*7*6*5*4*3*2*1=3628800


userInput = int(input("Enter a number: "))
for i in range(1, userInput + 1): 
    result *= i 
    print("inside loop: ",result)
print(result)