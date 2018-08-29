"""Everything about binary tree
include but not limited to:
binary tree implementataion,
preorder, postorder ,inorder traversal
"""


class BinaryNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        """
        serializer for binary tree
        """
        return f"_{self.left}_{self.value}_{self.right}"


def preorder_traversal(root):
    """
    in order traversal
    input: root node of a binary tree
    output: array of values 
    """
    results = []
    stack = [root]
    while stack:
        node = stack.pop()
        results.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return results


def inorder_traversal(root):
    """
    in order traversal
    input: root node of a binary tree
    output: array of values 
    """
    results = []
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            results.append(node.value)
            node = node.right

    return results


def postorder_traversal(root):
    """
    in order traversal
    input: root node of a binary tree
    output: array of values 
    """
    results = []
    stack = [root]
    while stack:
        node = stack.pop()
        results.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return results[::-1]


def main():
    root = BinaryNode('root')
    n1 = BinaryNode(1)
    n2 = BinaryNode(2)
    n3 = BinaryNode(3)
    n4 = BinaryNode(4)
    root.left = n1
    root.right = n2
    n1.left = n3
    n1.right = n4
    print(root)
    print('preorder:', preorder_traversal(root))
    print('inorder:', inorder_traversal(root))
    print('postorder:', postorder_traversal(root))


if __name__ == '__main__':
    main()
