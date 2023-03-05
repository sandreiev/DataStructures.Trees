from tree_node import TreeNode

def _processNode(node: TreeNode, tree, result):
    result.append(node.label)

    descendants = tree.get(node)

    if (descendants is None):
            return result

    for descendant in descendants:
        _processNode(descendant, tree, result)

def performListing(tree) -> list[str]:
    result =  []

    _processNode(next(iter(tree)), tree, result)
    
    return result
    