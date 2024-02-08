#!/usr/bin/python3
import sys
file_name = sys.argv[1]
if file_name.endswith(".py"):
    try:
        f = open(file_name, "x")
        f.write("#!/usr/bin/python3\n")
        f.close()
        print("Success!")
    except FileExistsError as e:
        print("This file already Exists.")
elif file_name.endswith(".txt"):
    try:
        f = open(file_name, "x")
        try:
            f.write(sys.argv[2] + '\n')
            print("Success!")
        except IndexError:
            print("Succesfully created an empty file.")
        f.close()
    except FileExistsError as e:
        print("This file already Exists.")
else:
    try:
        f = open(file_name, "x")
        f.close()
        print("Success!")
    except FileExistsError as e:
        print("This file already Exists.")
