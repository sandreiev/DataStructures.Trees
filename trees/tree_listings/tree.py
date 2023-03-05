from tree_node import TreeNode

class Tree:
    def __init__(
            self, 
            source:dict[TreeNode, list[TreeNode]],
            is_expression = False) -> None:
        self.tree = source
        self.root = next(iter(self.tree))
        self.is_expression = is_expression

    def __str__(self) -> str:
        result = ''

        for key, value in self.tree.items():
            valueStr = None if value is None else [str(x) for x in value]
            result += f"{key}:{valueStr}\n"

        return result

    def _process_node_preorder(self, node: TreeNode, result):
        result.append(node.label)

        descendants = self.get_node_descendants(node)

        if (descendants is None):
            return result

        for descendant in descendants:
            self._process_node_postorder(descendant, result)
            
    def _process_node_inorder(self, node: TreeNode, result):
        descendants = self.get_node_descendants(node)

        if (descendants is None):
            return result.append(node.label)

        for i in range(len(descendants)):
            descendant = descendants[i]
            self._process_node_inorder(descendant, result)

            if i == 0:
                result.append(node.label)

    def _process_expression_node_inorder(self, node: TreeNode, result):
        descendants = self.get_node_descendants(node)

        if (descendants is None):
            return result.append(node.label)

        for i in range(len(descendants)):
            if i == 0 and node is not self.root:
                result.append('(')

            descendant = descendants[i]
            self._process_expression_node_inorder(descendant, result)

            if i == 0:
                result.append(node.label)

            if i == len(descendants) - 1 and node is not self.root:
                result.append(')')

    def _process_node_postorder(self, node: TreeNode, result):
        descendants = self.get_node_descendants(node)

        if (descendants is not None):
            for descendant in descendants:
                self._process_node_preorder(descendant, result)

        return result.append(node.label)

    def get_node_descendants(self, node_name: str) -> list[str]:
        return self.tree.get(node_name)
    
    def preorder_listing(self) -> list[str]:
        result =  []

        self._process_node_preorder(self.root, result)
        
        return result
    
    def inorder_listing(self) -> list[str]:
        result =  []

        if self.is_expression:
            self._process_expression_node_inorder(self.root, result)
        else:
            self._process_node_inorder(self.root, result)
        
        return result
    
    def postorder_listing(self) -> list[str]:
        result =  []

        self._process_node_postorder(self.root, result)
        
        return result
