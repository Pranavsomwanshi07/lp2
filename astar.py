graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 5},
    'C': {'F': 2},
    'D': {},
    'E': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

h = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 1,
    'G': 0
}

open = ['A']

while open:

    node = open.pop(0)

    print(node)

    if node == 'G':
        break

    temp = []

    for i in graph[node]:
        temp.append((graph[node][i] + h[i], i))

    temp.sort()

    for c, n in temp:
        open.append(n)
