# Optimized Graph Coloring

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

colors = ["Red", "Green", "Blue"]
result = {}

for node in graph: 

    used = []

    for neighbor in graph[node]:

        if neighbor in result:
            used.append(result[neighbor])

    for color in colors:

        if color not in used:
            result[node] = color
            break


print(result)  
