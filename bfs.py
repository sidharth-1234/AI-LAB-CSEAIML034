def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(f"exploring node: {current_node}")
            visited.append(current_node)

            for neighbor in graph.get(current_node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return visited


print("--- building graph ---")
students_graph = {}

num_edges = int(input("how many edges (connections) does the graph have? "))

print("enter the edges separated by space (e.g., A B):")

for i in range(num_edges):
    u, v = input(f"edge {i + 1}: ").split()
    if u not in students_graph:
        students_graph[u] = []
    if v not in students_graph:
        students_graph[v] = []

    students_graph[u].append(v)
    students_graph[v].append(u)

start = input("enter the starting node: ")
print(f"\n your graph dictionary: {students_graph}")
print("starting BFS traversal from node:")
print(bfs(students_graph, start))