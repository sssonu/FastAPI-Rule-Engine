class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

def node_to_dict(node):
    if node is None:
        return None
    return {
        'type': node.type,
        'value': node.value,
        'left': node_to_dict(node.left),
        'right': node_to_dict(node.right)
    }

def dict_to_node(d):
    if d is None:
        return None
    return Node(
        d['type'],
        d['value'],
        dict_to_node(d['left']),
        dict_to_node(d['right'])
    )
