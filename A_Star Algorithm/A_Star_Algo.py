def create_graph(input_data):
    graph = {}
    heuristics = {}
    sentences = input_data.split("\n")
    for sentence in sentences:
        words = sentence.split(" ")
        if words[0] not in heuristics.keys():
            heuristics[words[0]] = int(words[1])
        for i in range(len(words)):
            if i == 0:
                graph[words[0]] = {}
            if i > 1 and i % 2 == 0:
                graph[words[0]][words[i]] = int(words[i+1])
    return graph, heuristics

def find_start_and_goal(heuristics, start):
    if start == '':
        start = list(heuristics.keys())[0]
    else:
        start = start
    for key, value in heuristics.items():
        if value == 0:
            goal = key
    return start, goal
        
def A_Star(graph, heuristics, start, goal):
    inf = float('inf')
    visited = []
    to_visit = [(heuristics[start], start, 0)]
    costs = {}
    for key in heuristics.keys():
        costs[key] = inf
    costs[start] = 0
    while to_visit:
        to_visit.sort()
        current_heuristic, city, distance = to_visit.pop(0)
        if len(visited) < 1:
            visited.append(city)
        else:
            if city in graph[visited[-1]].keys():
                visited.append(city)
        if city == goal:
            return visited, distance
        for key, value in graph[city].items():
            if key not in visited:
                new_actual_cost = distance + value
                if new_actual_cost < costs[key]:
                    costs[key] = new_actual_cost
                    total_cost = new_actual_cost + heuristics[key]
                    to_visit.append((total_cost, key, new_actual_cost))
    return "No Path Found", 0
        
file_path = 'F:/Random Codes/A_Star Algorithm/Input_file.txt'
with open(file_path, 'r') as file:
    input_data = file.read()

graph, heuristics = create_graph(input_data)

start = input("Enter Starting City: ")
start, goal = find_start_and_goal(heuristics, start)

path, distance = (A_Star(graph, heuristics, start, goal))
if path != "No Path Found":
    print("Path: ", end = "")
    for city in range(len(path)):
        if city < len(path) - 1:
            print(f'{path[city]} -> ', end = '')
    print(path[-1])
    print(f'Total Distance: {distance}')
else:
    print('NO PATH FOUND')