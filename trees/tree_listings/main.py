import tree_samples

tree = tree_samples.create_simple_tree()

print(tree)

result = tree.preorder_listing()
print('preorder: ', ' '.join(result))

result = tree.inorder_listing()
print('inorder:  ', ' '.join(result))

result = tree.postorder_listing()
print('postorder:', ' '.join(result))
