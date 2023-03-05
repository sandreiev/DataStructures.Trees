from tree_node import TreeNode

def _processNode(node: TreeNode, tree, result):
    descendants = tree.get(node)

    if (descendants is not None):
        for descendant in descendants:
            _processNode(descendant, tree, result)

    return result.append(node.label)

def performListing(tree) -> list[str]:
    result =  []

    _processNode(next(iter(tree)), tree, result)
    
    return result