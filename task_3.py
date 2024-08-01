import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створимо граф
G = nx.Graph()

# Додамо вершини (станції)
stations = ['A', 'B', 'C', 'D', 'E']
G.add_nodes_from(stations)

# Додамо ребра (залізничні шляхи між станціями) з вагами
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2)
]
G.add_weighted_edges_from(edges)

# Візуалізуємо граф з вагами ребер
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='yellow', edge_color='lightblue', node_size=500, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]
    shortest_path_tree = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, data in graph[current_node].items():
            weight = data['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_path_tree[neighbor] = current_node

    return distances, shortest_path_tree

# Знаходження найкоротших шляхів від кожної вершини до всіх інших
all_pairs_shortest_paths = {}
all_pairs_distances = {}

for node in G.nodes:
    distances, paths = dijkstra(G, node)
    all_pairs_shortest_paths[node] = paths
    all_pairs_distances[node] = distances

# Виведення результатів
print("Найкоротші шляхи між усіма вершинами:")
for source in all_pairs_shortest_paths:
    for target in G.nodes:
        if source != target:
            path = []
            current_node = target
            while current_node != source:
                path.append(current_node)
                current_node = all_pairs_shortest_paths[source][current_node]
            path.append(source)
            path.reverse()
            print(f"Шлях від {source} до {target}: {' -> '.join(path)}, довжина шляху: {all_pairs_distances[source][target]}")

