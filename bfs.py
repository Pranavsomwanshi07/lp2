graph = {
    1:[2,3],
    2:[4,5],
    3:[1],
    4:[2],
    5:[2]
}

queue = [1]
visited = [1] 

while queue:

    node = queue.pop(0)

    print(node)

    for i in graph[node]:

        if i not in visited:

            visited.append(i)

            queue.append(i)
