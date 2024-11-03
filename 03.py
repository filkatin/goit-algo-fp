import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Додаємо для неорієнтованого графа

    def dijkstra(self, start):
        # Ініціалізуємо словник відстаней до всіх вершин як безкінечність
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0  # Відстань до стартової вершини - нуль

        # Черга з пріоритетом для вибору вершини з найменшою відстанню
        priority_queue = [(0, start)]
        heapq.heapify(priority_queue)

        while priority_queue:
            # Вибираємо вершину з мінімальною відстанню
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Пропускаємо оброблені вершини
            if current_distance > distances[current_vertex]:
                continue

            # Оновлюємо відстані до сусідніх вершин
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # Якщо знайдено коротший шлях до сусіда
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Тестування:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'E', 3)

start_vertex = 'A'
shortest_paths = graph.dijkstra(start_vertex)

print(f"Найкоротші відстані від вершини {start_vertex}:")
for vertex, distance in shortest_paths.items():
    print(f"Відстань до {vertex}: {distance}")
