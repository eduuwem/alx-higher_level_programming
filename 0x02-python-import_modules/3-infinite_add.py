#!/usr/bin/python3

if __name__ == "__main__":
    """print the addition of all arguments."""
    import sys, math

    result = 0

    for i in sys.argv:

        result += int(i)

        print("{}".format(result))
