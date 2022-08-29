#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in range(len(matrix)):
        for o in range(len(matrix[n])):
            print("{:d}".format(matrix[n][o]), end="")
            if o != (len(matrix[n]) - 1):
                print(" ", end="")

        print("")
