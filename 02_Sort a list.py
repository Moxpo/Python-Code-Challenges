
#    Create a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter
#    will be a string that can be one of the following values: asc, desc, and none.

#    If the second parameter is "asc," then the function should return a list with the numbers in ascending order.
#    If it's "desc," then the list should be in descending order, and if it's "none," it should return the original
#    list unaltered.


response = ["asc", "desc", "none"]
command = ""

userInput = input("Give me a list of numbers seperated by a space\n")
numberList = userInput.split()
numberList = [int(x) for x in numberList]

print(numberList)

while command not in response:
    command = input("Sort lit by ascending, descending or none?\nType asc, desc or none : \n")
    command = command.lower()

if command == "asc":
    numberList.sort()
    print(numberList)
elif command == "desc":
    numberList.sort(reverse=True)
    print(numberList)
else:
    print(numberList)

