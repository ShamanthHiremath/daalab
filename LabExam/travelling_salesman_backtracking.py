from collections import defaultdict

def tsp(graph, visited, curr_pos, V, count, cost, path):
    if count == V and curr_pos in graph and graph[curr_pos][path[0]] != float('inf'):
        return cost + graph[curr_pos][path[0]], path + [path[0]]
    
    # if count == V :
        # return cost, path
    
    ans = float('inf')
    best_path = []
    
    for neighbor in graph[curr_pos]:
        if not visited[neighbor]:
            visited[neighbor] = True
            new_cost, new_path = tsp(graph, visited, neighbor, V, count + 1, cost + graph[curr_pos][neighbor], path + [neighbor])
            if new_cost < ans:
                ans = new_cost
                best_path = new_path
            visited[neighbor] = False
    
    return ans, best_path

V = int(input("\nEnter no of vertices: "))
visited = [False] * V

graph = defaultdict(dict)

E = int(input("Enter the no of edges: "))
print("Enter edges and their weight separated by space(u v weight)")
for i in range(E):
    u, v, weight = map(int, input(f"Edge {i+1}: ").split())
    graph[u][v] = weight
    graph[v][u] = weight

src = int(input("Enter the source node: "))
visited[src] = True

path = [src]

min_cost, tour_path = tsp(graph, visited, src, V, 1, 0, path)
print("Minimum Cost of Tour:", min_cost)
print("Path Taken:", " -> ".join(map(str, tour_path)))



def tsp(graph, visited, curr_pos, V, count, cost, path):
    if count == V and graph[curr_pos][path[0]]:
        return cost + graph[curr_pos][path[0]], path + [path[0]]
    ans = float('inf')
    best_path = []
    for i in range(V):
        if not visited[i]:
            visited[i] = True
            new_cost, new_path = tsp(graph, visited, i, V, count + 1, cost + graph[curr_pos][i], path + [i])
            if new_cost < ans:
                ans = new_cost
                best_path = new_path
            visited[i] = False
    return ans, best_path

V = int(input("\nEnter no of vertices: "))
visited = [False for i in range(V)]

Graph = [[float('inf') for i in range(V)] for j in range(V)] 
for i in range(V):
    Graph[i][i] = 0

E = int(input("Enter the no of edges: "))
print("Enter edges and their weight separated by space(u v weight)")
for i in range(E):
    u, v, weight = map(int, input(f"Edge {i+1}: ").split())
    Graph[u][v] = weight
    Graph[v][u] = weight

src = int(input("Enter the source node: "))
visited[src] = True

path = [src]

min_cost, tour_path = tsp(Graph, visited, src, V, 1, 0, path)
print("Minimum Cost of Tour:", min_cost)
print("Path Taken:", " -> ".join(map(str, tour_path)))
