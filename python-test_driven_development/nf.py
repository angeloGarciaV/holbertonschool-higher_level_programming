#!/usr/bin/python3
import sys
file_name = sys.argv[1]
try:
    f = open(file_name, "x")
    f.write("#!/usr/bin/python3\n")
    f.close()
    print("Success!")
except FileExistsError as e:
    print("This file already Exists.")
