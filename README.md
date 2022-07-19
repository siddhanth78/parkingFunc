# Parking Functions

## Sample terminal output

    >>help
    >>Type help:<command> for more info.

    command:
        input
        func
        build
        tree
        clr:  Clear the terminal.
        quit: Quit the terminal.

    >>help:input
    
    input:<function>  
    Input a list of numbers to load into the 'func' object.  
    Numbers must be separated by a whitespace.  
    Integers are the only valid input. Improper usage of whitespace may give undesirable results.  

    >>help:func
    
    func:[<attribute>]  
    Display the 'func' object and its attributes.  
    attribute:  
        attr:                    All attributes of the function.  
        isPF:                    True if function is a parking function and False if not.
        length:                  Number of cars in the function.
        input:                   Input loaded into 'func'.
        outcome:                 Result of input.
        outcomeInv:              Inverse of outcome.
        nonDecArr:               Non-decreasing order of input.
        spec:                    Number of cars that prefer a position.
        specDetail [<position>]: Detailed spec.
        orderPerm:               Order permutation of function.
        orderPermInv:            Inverse of order permutation.
        error:                   Error associated with the function during input processing.

    >>help:build

    build:func [<process>]
    Build tree using 'func' object to load into 'tree' object.
    Tree represents the inverse of the outcome of 'func'.
    process:
        up: Unprocessed tree.
        p:  Processed tree.
    process 'up' by default.

    >>help:tree

    tree:[<command>]
    Display tree object. Contains input function and process status.
    Process status:
        False: Unprocessed tree.
        True:  Processed tree.
    command:
        show:    Display tree representing the inverse of the outcome of the function.
        attr:    All attributes of the tree.
        pstatus: Process status of the tree.
        func:    Attributes of input function necessary for the tree.
        inv:     Inversion pairs of the tree. Number of pairs is the displacement of the input function.
    Displacement is the total number of spots moved by all cars from their preferred to current spot.

    >>input:5 1 2 4 4 6 2 3
    >>func[5, 1, 2, 4, 4, 6, 2, 3]
    >>func:isPF
    >>True
    >>func:outcomeInv
    >>[2, 3, 7, 4, 1, 5, 6, 8]
    >>build:func p
    >>tree([5, 1, 2, 4, 4, 6, 2, 3], True)
    >>tree:show
    0
    ╚══ 6
        ╠══ 3
        ║   ╚══ 2
        ║       ╚══ 7
        ╚══ 4
            ╚══ 8
                ╠══ 1
                ╚══ 5

    >>tree:inv

    Displacement of input function: 9
    Inversion pairs:                [[6, 4], [6, 1], [4, 1], [8, 1], [6, 5], [8, 5], [6, 3], [6, 2], [3, 2]]

    >>func:attr

    Attributes:
        isPF:         True
        length:       8
        input:        [5, 1, 2, 4, 4, 6, 2, 3]
        outcome:      [5, 1, 2, 4, 6, 7, 3, 8]
        outcomeInv:   [2, 3, 7, 4, 1, 5, 6, 8]
        nonDecArr:    [1, 2, 2, 3, 4, 4, 5, 6]
        spec:         [1, 2, 1, 2, 1, 1, 0, 0]
        specDetail:   {1: 1, 2: 2, 3: 1, 4: 2, 5: 1, 6: 1, 7: 0, 8: 0}
        orderPerm:    [7, 1, 2, 5, 6, 8, 3, 4]
        orderPermInv: [2, 3, 7, 8, 4, 5, 1, 6]
        error:        None
