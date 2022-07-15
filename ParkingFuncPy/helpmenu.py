def help_():
    
    print(">>Enter help:<command> for more info.")
    print("List of commands:")
    print("    input")
    print("    func")
    print("    prevfunc")
    print("    tree")
    print("    clr:  Clear the terminal.")
    print("    quit: Quit the terminal.")
    
def input_():

    print("input:<function>")
    print("Input a list of numbers to load into the 'func' object.")
    print("Numbers must be separated by a whitespace.")
    print("Integers are the only valid input. Improper usage of whitespace may give undesirable results.")
    
def func():

    print("func:[<attr>]")
    print("Display the 'func' object and its attributes.")
    print("Attributes:")
    print("    attr:                    All attributes of the function.")
    print("    isPF:                    True if function is a parking function and False if not.")
    print("    length:                  Length of function.")
    print("    input:                   Input loaded into 'func'.")
    print("    outcome:                 Result of input.")
    print("    outcomeInv:              Inverse of outcome.")
    print("    nonDecArr:               Non-decreasing order of input.")
    print("    spec:                    Number of cars that prefer a position.")
    print("    specDetail [<position>]: Detailed spec.")
    print("    orderPerm:               Order permutation of function.")
    print("    orderPermInv:            Inverse of order permutation.")
    print("    error:                   Error associated with the function during input processing.")
    
def prevfunc():

    print("prevfunc")
    print("Display previously used function.")
    print("This function is inactive and cannot be used.")
    print("input:prevfunc")
    print("'prevfunc' can be loaded into 'func' through 'input'.")
    
def tree():

    print("tree:<function> [<process>]")
    print("Display tree representing the function.")
    print("Displays unprocessed tree by default.")
    print("process:")
    print("    up: Unprocessed tree.")
    print("    p:  Processed tree.")