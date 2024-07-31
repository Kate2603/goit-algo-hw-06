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

# DFS і BFS функції
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Пошук шляхів між двома вершинами
start, goal = 'A', 'E'
dfs_result = list(dfs_paths(G, start, goal))
bfs_result = list(bfs_paths(G, start, goal))

print("DFS шляхи від {} до {}: {}".format(start, goal, dfs_result))
print("BFS шляхи від {} до {}: {}".format(start, goal, bfs_result))

# Порівняння результатів
print("\nПорівняння результатів DFS та BFS:")
print(f"Кількість шляхів знайдених DFS: {len(dfs_result)}")
print(f"Кількість шляхів знайдених BFS: {len(bfs_result)}")

# Пояснення різниці
print("\nПояснення:")
print("DFS (пошук у глибину) знаходить шляхи, заглиблюючись у граф настільки глибоко, наскільки можливо, перш ніж повернутися назад.")
print("BFS (пошук у ширину) знаходить шляхи, розширюючи всі можливі шляхи на кожному рівні одночасно, що гарантує знаходження найкоротших шляхів першими.")


# Висновки:
# DFS може знайти довші шляхи, оскільки він заглиблюється в граф, перш ніж повернутися назад.
# BFS завжди знайде найкоротший шлях, оскільки він перевіряє всі сусідні вершини на кожному рівні перед тим, як заглиблюватися далі.