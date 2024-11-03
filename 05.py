import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    nx.set_node_attributes(tree, colors, 'color')

    node_colors = [tree.nodes[node]['color'] for node in tree.nodes]

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()


def generate_colors(num_nodes):
    # Створює кольори у форматі 16-системи RGB, виключаючи дуже світлі відтінки
    colors = []
    for i in range(num_nodes):
        # Зміна інтенсивності, щоб не доходити до білого (максимум 200 замість 255)
        intensity = int(200 * (i + 1) / num_nodes)
        color = f"#{intensity:02x}{intensity:02x}ff"
        colors.append(color)
    return colors


def bfs(root):
    queue = [root]
    order = []
    while queue:
        node = queue.pop(0)
        if node:
            order.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return order


def dfs(root):
    stack = [root]
    order = []
    while stack:
        node = stack.pop()
        if node:
            order.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return order


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# BFS обхід
bfs_order = bfs(root)
bfs_colors = {node.id: color for node, color in zip(bfs_order, generate_colors(len(bfs_order)))}
draw_tree(root, bfs_colors)

# DFS обхід
dfs_order = dfs(root)
dfs_colors = {node.id: color for node, color in zip(dfs_order, generate_colors(len(dfs_order)))}
draw_tree(root, dfs_colors)
