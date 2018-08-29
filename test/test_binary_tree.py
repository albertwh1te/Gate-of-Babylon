from algorithms.acm.binary_tree import (
    preorder_traversal,
    postorder_traversal,
    inorder_traversal,
    BinaryNode
)


def test_traversal():
    """
    the test case from wikipedia
    https://en.wikipedia.org/wiki/Tree_traversal
    """
    F = BinaryNode("F")
    A = BinaryNode("A")
    B = BinaryNode("B")
    C = BinaryNode("C")
    D = BinaryNode("D")
    E = BinaryNode("E")
    G = BinaryNode("G")
    H = BinaryNode("H")
    I = BinaryNode("I")
    F.left = B
    F.right = G
    B.left = A
    B.right = D
    D.left = C
    D.right = E
    G.right = I
    I.left = H
    assert preorder_traversal(
        F) == ["F", "B", "A", "D", "C", "E", "G", "I", "H"]
    assert inorder_traversal(
        F) == ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    assert postorder_traversal(
        F) == ["A", "C", "E", "D", "B", "H", "I", "G", "F"]
