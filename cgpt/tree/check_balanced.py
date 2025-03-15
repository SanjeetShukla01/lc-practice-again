# Python program to check if a tree is height-balanced or not
# Using Top Down Recursion

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to calculate the height of a tree
def height(node):
    # Base case: Height of empty tree is zero
    if node is None:
        return 0

    # Height = 1 + max of left height and right heights
    return 1 + max(height(node.left), height(node.right))


# Function to check if the binary tree with given root is height-balanced
def isBalanced(root):
    # If tree is empty then return true
    if root is None:
        return True

    # Get the height of left and right subtrees
    lHeight = height(root.left)
    rHeight = height(root.right)

    # If absolute height difference is greater than 1
    # Then return false
    if abs(lHeight - rHeight) > 1:
        return False

    # Recursively check the left and right subtrees
    return isBalanced(root.left) and isBalanced(root.right)


if __name__ == "__main__":
    # Representation of input BST:
    #            1
    #           / \
    #          2   3
    #         /  \
    #        4   5
    #       /
    #      8
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)

    print("True" if isBalanced(root) else "False")
