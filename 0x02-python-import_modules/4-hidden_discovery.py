#!/usr/bin/python3
if __name__ == "__main__":
    """print all the names defined by the compiled module hidden_4.pyc."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if i[:2] != "__":
            print(name)
