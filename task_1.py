import networkx as nx
import matplotlib.pyplot as plt

# Створимо граф
G = nx.Graph()

# Додамо вершини (станції)
stations = ['A', 'B', 'C', 'D', 'E']
G.add_nodes_from(stations)

# Додамо ребра (залізничні шляхи між станціями)
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')]
G.add_edges_from(edges)

# Візуалізуємо граф
pos = nx.spring_layout(G)  # Позиціонуємо вершини для візуалізації
nx.draw(G, pos, with_labels=True, node_color='yellow', edge_color='lightblue', node_size=500, width=2)
plt.show()

# Аналіз основних характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"Вершина {node}: {degree}")

# Додатковий аналіз (опціонально)
# Знаходження середньої ступені
average_degree = sum(degrees.values()) / num_nodes
print(f"Середня ступінь: {average_degree:.2f}")

# Знаходження діаметру графа
if nx.is_connected(G):
    diameter = nx.diameter(G)
    print(f"Діаметр графа: {diameter}")
else:
    print("Граф не зв'язний, діаметр не визначено")
