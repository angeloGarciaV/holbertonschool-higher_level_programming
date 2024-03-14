#!/usr/bin/python3
import sys
import os
file_name = sys.argv[1:]
for i, file in enumerate(file_name):
    if file.endswith(".py"):
        try:
            with open(file, "x") as f:
                f.write("#!/usr/bin/python3\n")
                os.chmod(file, 0o744)
                print(f"Successfully created {file}")
        except FileExistsError as e:
            print(f"{file} already exists.")
    if file.endswith(".txt"):
        try:
            with open(file, "x") as f:
                if i+1 < len(file_name) and not (file_name[i+1].endswith('.txt') or file_name[i+1].endswith('.py')):
                    f.write(f"{file_name[i+1]}\n")
                    print(f"Successfully created {file} with content.")
                else:
                    print(f"Successfully created an empty file {file}.")
        except FileExistsError as e:
            print(f"{file} already exists.")
    if not file.endswith(('.txt', '.py')) and file_name[i-1] not file.endswith('.txt'):

