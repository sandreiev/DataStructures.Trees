from tree_node import TreeNode

def _processNode(node: TreeNode, tree, result):
    descendants = tree.get(node)

    if (descendants is None):
        return result.append(node.label)

    for i in range(len(descendants)):
        descendant = descendants[i]
        _processNode(descendant, tree, result)

        if (i == 0):
            result.append(node.label)

def performListing(tree) -> list[str]:
    result =  []

    _processNode(next(iter(tree)), tree, result)
    
    return result