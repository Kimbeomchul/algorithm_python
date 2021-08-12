class Node:
    def __init__(self, value , left=None , right = None):
        self.value = value
        self.left = left
        self.right = right


def min_data(tree):
    queue = [(tree, tree.value)]
    min_data = float('inf')

    while queue:
        item , root = queue.pop()

        if item.left:
            queue.append((item.left , item.left.value + root))
        if item.right:
            queue.append((item.right , item.right.value + root))
        if not item.right and not item.left:
            min_data = min(min_data, root)

    return min_data



node = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1), None))) # 15
node2 = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1))) # 16
node3 = Node(10, Node(5, None, Node(2)), Node(5)) # 15
node4 = Node(10) # 10
print(min_data(node))
