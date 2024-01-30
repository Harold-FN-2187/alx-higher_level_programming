#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    cnt = len(sys.argv) - 1
    if cnt == 0:
        print("{} arguments.".format(cnt))
    elif cnt == 1:
        print("{} argument:".format(cnt))
    else:d
        print("{} arguments".format(cnt))
    for i in range(cnt):
        print("{}: {}".format(i+1, sys.argv[i + 1]))
