def help_():
    
    print(">>Type help:<command> for more info.")
    print("\ncommand:")
    print("    input")
    print("    func")
    print("    build")
    print("    tree")
    print("    clr:  Clear the terminal.")
    print("    quit: Quit the terminal.\n")
    
def input_():

    print("\ninput:<function>")
    print("Input a list of numbers to load into the 'func' object.")
    print("Numbers must be separated by a whitespace.")
    print("Integers are the only valid input. Improper usage of whitespace may give undesirable results.\n")
    
def func():

    print("\nfunc:[<attribute>]")
    print("Display the 'func' object and its attributes.")
    print("attribute:")
    print("    attr:                    All attributes of the function.")
    print("    isPF:                    True if function is a parking function and False if not.")
    print("    length:                  Number of cars in the function.")
    print("    input:                   Input loaded into 'func'.")
    print("    outcome:                 Result of input.")
    print("    outcomeInv:              Inverse of outcome.")
    print("    nonDecArr:               Non-decreasing order of input.")
    print("    spec:                    Number of cars that prefer a position.")
    print("    specDetail [<position>]: Detailed spec.")
    print("    orderPerm:               Order permutation of function.")
    print("    orderPermInv:            Inverse of order permutation.")
    print("    error:                   Error associated with the function during input processing.\n")
    
def build():
    
    print("\nbuild:func [<process>]")
    print("Build tree using 'func' object to load into 'tree' object.")
    print("Tree represents the inverse of the outcome of 'func'.")
    print("process:")
    print("    up: Unprocessed tree.")
    print("    p:  Processed tree.")
    print("process 'up' by default.\n")
    
def tree():

    print("\ntree:[<command>]")
    print("Display tree object. Contains input function and process status.")
    print("Process status:")
    print("    False: Unprocessed tree.")
    print("    True:  Processed tree.")
    print("command:")
    print("    show:    Display tree representing the inverse of the outcome of the function.")
    print("    attr:    All attributes of the tree.")
    print("    pstatus: Process status of the tree.")
    print("    func:    Attributes of input function necessary for the tree.")
    print("    inv:     Inversion pairs of the tree. Number of pairs is the displacement of the input function.")
    print("Displacement is the total number of spots moved by all cars from their preferred to current spot.\n")