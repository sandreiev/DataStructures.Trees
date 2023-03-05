from tree_node import TreeNode
from tree import Tree

def create_simple_tree() -> Tree:
    one = TreeNode('1')
    two = TreeNode('2')
    three = TreeNode('3')
    four = TreeNode('4')
    five = TreeNode('5')
    six = TreeNode('6')
    seven = TreeNode('7')
    eight = TreeNode('8')
    nine = TreeNode('9')
    ten = TreeNode('10')

    return Tree({
        one: [two,three,four], 
        two: None, three: [five,six], four: [seven], 
        five: [eight,nine], six: [ten], seven: None, 
        eight: None, nine: None, ten: None
    })

def create_expression_tree() -> Tree:
    root = TreeNode(1,'*')
    firstSum = TreeNode(2,'+')
    secondSum = TreeNode(3,'+')
    a1 = TreeNode(4, 'a')
    b = TreeNode(5, 'b')
    a2 = TreeNode(6, 'a')
    c = TreeNode(7, 'c')

    source = {
        root: [firstSum, secondSum],
        firstSum: [a1, b],
        secondSum: [a2, c]
    }

    #(a+b) * (a+c)
    return Tree(source, True)