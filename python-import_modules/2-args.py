#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv) -1
    args = sys.argv
    a = 1
    print("{} Arguments:".format(count))
    for i in args:
        if i == args[0]:
            continue
        print("{}: {}".format(a, i))
        a += 1
