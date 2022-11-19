#   Write a function in Python that accepts a decimal number and returns the equivalent binary number. To make this
#   simple, the decimal number will always be less than 1,024, so the binary number returned will always be less
#   than ten digits long.

binary = ""


while True:
    user_input = input("Give me a number equal to or less than 1024\n")
    user_input = int(user_input)
    if user_input <= 1024:
        break
    else:
        print("Try again")


print(user_input)

#	more edits
