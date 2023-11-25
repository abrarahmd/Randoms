import random

def generate_maze(rows, cols):
    startEndnum = []
    for i in range(rows*cols):
        startEndnum.append(i)
    generate = ["#", " "]
    rowPointer = 1
    maze = ""
    for i in range(rows):
        for j in range(cols):
            if 1 < rowPointer < rows:
                maze += random.choice(generate)
            elif rowPointer == 1 or rowPointer == rows:
                maze += "#"
            else:
                pass 
        rowPointer += 1
        if i != rows - 1:
            maze += "\n"
    while True:
        start_index = random.choice(startEndnum)
        if maze[start_index] != "\n":
            maze = maze[:start_index] + "S" + maze[start_index + 1:]
            break
    while True:
        end_index = random.choice(startEndnum)
        if maze[end_index] != "S" and maze[end_index] != "\n":
            maze = maze[:end_index] + "E" + maze[end_index + 1:]
            break
    return maze

def solve_maze(maze):
    splitting = maze.split("\n")
    matrix = []
    for i in splitting:
        listing = []
        for j in i:
            listing.append(j)
        matrix.append(listing)
    solution = False
    rows, cols = len(matrix), len(matrix[0])
    start_pos = None
    end_pos = None
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'S':
                start_pos = (i, j)
            elif matrix[i][j] == 'E':
                end_pos = (i, j)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    queue = [(start_pos, [])]
    while queue:
        current_pos, path = queue.pop(0)
        if current_pos == end_pos:
            matrix = updateMatrix(matrix, path)
            maze = ""
            for i in matrix:
                for j in i:
                    maze += j
                maze += "\n"
            maze = maze[:-1]
            solution = True
            break
        if current_pos not in visited:
            visited.add(current_pos)
            for dr, dc in directions:
                new_row, new_col = current_pos[0] + dr, current_pos[1] + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] != '#':
                    queue.append(((new_row, new_col), path + [(new_row, new_col)]))
    return [maze, solution]

def updateMatrix(matrix, path):
    for i in path:
        a = i[0]
        b = i[1]
        if matrix[a][b] != "E":
            matrix[a][b] = "O"
    return matrix

cols = int(input("How many columns? "))
rows = int(input("How many rows? "))
maze = generate_maze(rows, cols)
print(f"{cols}*{rows} Maze")
print(maze)
yn = input("Would you like to see the solution (y/n)? ")
if yn == "y":
    newMaze = solve_maze(maze)
    if newMaze[1] != False:
        print(newMaze[0])
        print("Thank you for playing, now get back to your school work!")
    else:
        print("No Solution")
        print("Thank you for playing, now get back to your school work!")
elif yn == "n":
    print("Thank you for playing, now get back to your school work!")
else:
    print("Wrong Input!")