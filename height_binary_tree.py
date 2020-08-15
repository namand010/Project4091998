class Node:
    ###Node Formation
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height_traverse(root):
    if root is None:
        return 0

    q = []
    q.append(root)
    height = 0

    while True:
        nodecount = len(q)
        if nodecount == 0:
            return height

        height += 1   #####means node levels and height of tree is incfrement as node

        while nodecount > 0:
            node = q.pop()
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            nodecount -= 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Height of tree is ", height_traverse(root))
