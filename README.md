# goit-algo-hw-06

-----------------------------------

# Завдання 1

Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).

info
📖 Реальну мережу можна вибрати на свій розсуд, якщо немає можливості придумати свою мережу, наближену до реальності.

Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин).

# pip install networkx

-----------------------------------
# Завдання 2

Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.

Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.

# Висновки:
Шляхи, отримані алгоритмом DFS, можна пояснити тим, що він досліджує всі можливі шляхи від стартової вершини, не зважаючи на їхню довжину. Це означає, що він може знайти шляхи, які не є найкоротшими, але проходять через більше вершин.

Шляхи, отримані алгоритмом BFS, можна пояснити тим, що він розширює всі можливі шляхи на кожному рівні одночасно, що гарантує знаходження найкоротших шляхів першими. Це означає, що він завжди знаходить найкоротший шлях між двома вершинами, якщо такий шлях існує.

-----------------------------------

# Завдання 3

Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.