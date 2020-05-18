#checks in something is valid

import re

# Data to be outputted
data = ['first','second','third','fourth','fifth','sixth','seventh']

has_error = "yes"
while has_error == "yes":
    print()
    filename = input("Enter a filename: ")
    has_error = "no"
    problem = ""

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
                problem = "(no spaces allowed)"
        else:
            problem = ("(no {}'s allowed) ".format(letter))

    if filename == "":
        problem = "can't be bank"

    if problem != "":
        print("Invalid filename - {}".format(problem))
    else:
        print("You entered a vaild filename")
        has_error = "no"

        # add .txt suffix!
        filename += ".txt"

        # create file to hold data
        f = open(filename, "w+")

        # add new line at end of each item
        for item in data:
            f.write(item + "\n")

         # close file
        f.close()
