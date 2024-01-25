#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    args = sys.argv
    a = 1
    if count == 1:
        print("0 arguments.")
        sys.exit()
    if count == 2:
        print("1 argument:\n1: {}".format(args[1]))
        sys.exit()
    print("{} arguments:".format(count))
    for i in args:
        if i == args[0]:
            continue
        print("{}: {}".format(a, i))
        a += 1
