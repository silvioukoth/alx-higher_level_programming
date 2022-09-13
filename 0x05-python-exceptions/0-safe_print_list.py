#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list."""
    re = 0
    for j in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            re += 1
        except:
            break
    print("")
    return (re)
