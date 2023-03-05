class TreeNode:
    def __init__(self, name, label = None):
        self.name = name
        self.label = label if label is not None else name

    def __str__(self) -> str:
        return f"{self.name}({self.label})"
