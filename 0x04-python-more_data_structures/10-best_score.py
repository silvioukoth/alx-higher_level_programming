#!/usr/bin/python3
#This functionreturns a key with the biggest integer value.

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    var = list(a_dictionary.keys())[0]
    max = a_dictionary[var]
    for x, y in a_dictionary.items():
        if y > max:
            max = y
            var = x
    return (var)
