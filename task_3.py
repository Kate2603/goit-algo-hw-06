import networkx as nx
import matplotlib.pyplot as plt

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

# Реалізація алгоритму Дейкстри для знаходження найкоротшого шляху між усіма вершинами
def dijkstra_all_pairs(graph):
    paths = dict(nx.all_pairs_dijkstra_path(graph))
    lengths = dict(nx.all_pairs_dijkstra_path_length(graph))
    return paths, lengths

# Отримання найкоротших шляхів та їх довжин
paths, lengths = dijkstra_all_pairs(G)

# Виведення результатів
print("Найкоротші шляхи між усіма вершинами:")
for source in paths:
    for target in paths[source]:
        print(f"Шлях від {source} до {target}: {paths[source][target]}, довжина шляху: {lengths[source][target]}")
