from treelib import Tree, Node

def getTree(pfunc, processed = False):

    pf = pfunc.copy()
    
    #Get unprocessed auxiliary tree
    axtree = auxiliaryTree(pf)

    #Map outcomeInv and input
    map_outcome = {}
    map_input = {}

    for i in range(1, len(pf['outcome'])+1):
        map_outcome[i] = pf['outcome'][i-1]
    
    for i in range(1, len(pf['input'])+1):
        map_input[i] = pf['input'][i-1]

    #Get vertices of the tree excluding the root
    list_of_vertices = [i for i in axtree.expand_tree(0, mode = 1)]

    list_of_vertices.remove(0)

    #list to store stages of the processed tree
    stages = []

    #create copy of original tree
    ax_copy = Tree(axtree.subtree(axtree.root), deep=True)

    #create copy of tree to use for the stages
    tree_stage = ax_copy.subtree(0)

    #process the vertices
    for i in list_of_vertices:
        if ax_copy.get_node(i).is_leaf():
            continue
        tree_stage = processVertex(i, tree_stage, ax_copy, map_outcome, map_input)
        stages.append(tree_stage)
    
    if processed == False:
        return axtree, processed
    elif processed == True:
        return stages[0], processed

def processVertex(vertex, stage, ogtree, map_outcome, map_input):
    
    #Get node id and tag
    n_id = ogtree.get_node(vertex).identifier
    tag = stage.get_node(n_id).tag
    
    #Create subtree with root vertex
    subtree = stage.subtree(n_id)
    
    
    #Get all vertices of subtree excluding the root
    vertices = [i for i in subtree.expand_tree(n_id, mode = 1)]
    root = vertices.pop(0)
    
    #(1 + kth outcome - kth preference of ogtree)
    pos = 1 + map_outcome[n_id] - map_input[n_id]
    
    #Get corresponding n_id
    vertices.sort()
    
    #Get corresponding tag
    if len(vertices)<pos:
        pos = len(vertices)
    node_at_pos = vertices[pos-1]
    
    stage_node = stage.get_node(node_at_pos).tag
    
    #swap tags
    stage.get_node(n_id).tag = stage_node
    stage.get_node(node_at_pos).tag = tag
    
    return stage
    
def inversionPairs(tree):
    #Get path to all leaves
    li_path = tree.paths_to_leaves()

    inversions = []

    for i in li_path:
        n = 0
        if len(i) == 2:
            inversions.append([tree.get_node(i[1]).tag,None])
            continue
        for j in i:
            jtag = tree.get_node(j).tag
            for k in range(n, len(i)):
                ktag = tree.get_node(i[k]).tag
                #Compare tags
                if jtag > ktag:
                    #Add tag pairs to list of inversions
                    if [jtag,ktag] not in inversions:
                        inversions.append([jtag,ktag])
            n+=1
    return inversions, len(inversions)


def auxiliaryTree(pf):
    pf_copy = pf.copy()
    
    outcomeInv = pf_copy['outcomeInv']
    
    li_copy = outcomeInv.copy()
    
    tree = Tree()
    
    treeDict = {}
    
    #Create dictionary of trees with root node of corresponding outcomeInv
    for i in li_copy:
        newTree = Tree()
        newTree.create_node(i, i)
        treeDict[i] = newTree
    
    #Create tree with root node 0
    newTree = Tree()
    newTree.create_node(0, 0)
    treeDict[0] = newTree
    
    
    #Compare each element of list
    n=0
    for i in li_copy:
        flag = 0
        for j in range(n,len(li_copy)):
            if i == li_copy[j] and i == max(li_copy):
                treeDict[0].paste(0, treeDict[i])
                n+=1
                break
            elif i == li_copy[j] and li_copy.index(i) == len(li_copy)-1:
                flag = 0
            elif i == li_copy[j]:
                flag = 0
                continue
            elif i<li_copy[j]:
                #Paste tree with corresponding "parent tree"
                treeDict[li_copy[j]].paste(li_copy[j], treeDict[i])
                n+=1
                flag = 1
            elif i>li_copy[j] and j == len(li_copy)-1:
                flag = 0
            elif i>li_copy[j]:
                flag = 0
                continue
                
            if flag == 1:
                break
            elif flag == 0:
                #Attach entire tree to main tree with root 0
                treeDict[0].paste(0, treeDict[i])
                n+=1
                
    return treeDict[0]