import uuid
import networkx as nx
import matplotlib.pyplot as plt

class HeapNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.color = "lightgreen"
        self.id = str(uuid.uuid4())

class MaxHeap:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = HeapNode(key)
        if not self.root:
            self.root = new_node
        else:
            self._insert_node(self.root, new_node)

    def _insert_node(self, current, new_node):
        # Реалізація вставки нового вузла в максимальну купу
        if new_node.val > current.val:
            # Обмін значеннями
            new_node.val, current.val = current.val, new_node.val
        
        # Використовуємо рівні для вставки
        if not current.left:
            current.left = new_node
        elif not current.right:
            current.right = new_node
        else:
            # Якщо обидва нащадки зайняті, вставляємо в ліве або праве піддерево в залежності від кількості вузлів
            if self._count_nodes(current.left) <= self._count_nodes(current.right):
                self._insert_node(current.left, new_node)
            else:
                self._insert_node(current.right, new_node)

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def add_edges(self, graph, node, pos, x=0, y=0, layer=1):
        if node is not None:
            graph.add_node(node.id, color=node.color, label=node.val)
            if node.left:
                graph.add_edge(node.id, node.left.id)
                l = x - 1 / 2 ** layer
                pos[node.left.id] = (l, y - 1)
                self.add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
            if node.right:
                graph.add_edge(node.id, node.right.id)
                r = x + 1 / 2 ** layer
                pos[node.right.id] = (r, y - 1)
                self.add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
        return graph

    def draw_heap(self):
        tree = nx.DiGraph()
        pos = {self.root.id: (0, 0)}
        tree = self.add_edges(tree, self.root, pos)

        colors = [node[1]['color'] for node in tree.nodes(data=True)]
        labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

        plt.figure(figsize=(8, 5))
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.show()

# Тест
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(3)
max_heap.insert(15)
max_heap.insert(18)
max_heap.insert(30)
max_heap.insert(25)
max_heap.insert(17)

# Відображення купи
max_heap.draw_heap()
