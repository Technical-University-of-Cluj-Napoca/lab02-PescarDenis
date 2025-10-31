import sys
from collections import deque 
def read_maze(filename: str) -> list[str]:
    """Reads a maze from a file and returns it as a list of lists (i.e. a matrix).

    Args:
        filename (str): The name of the file containing the maze.
    Returns:
        list: A 2D list (matrix) representing the maze.
    """
    new_data = []
    with open(filename,'r') as file : 
        data = file.read()     
    new_data = data.split("\n")
    return new_data




def find_start_and_target(maze: list[str]) -> list[tuple[int, int]]:
    """Finds the coordinates of start ('S') and target ('T') in the maze, i.e. the row and the column
    where they appear.

    Args:
        maze (list[list[str]): A 2D list (matrix) representing the maze.
    Returns:
        tuple[int, int]: A tuple containing the coordinates of the start and target positions.
        Each position is represented as a tuple (row, column).
    """
    start = None
    target = None
    start_end = []
    for r,row in enumerate(maze) :
            for c,value in enumerate(row) :
                if value == 'S' :
                        start = (r,c)
                        start_end.append(start)
                elif value == 'T' :
                        target = (r,c)
                        start_end.append(target)
    return start_end


def get_neighbors(maze: list[str], position: tuple[int, int]) -> list[tuple[int, int]]:
    """Given a position in the maze, returns a list of valid neighboring positions: (up, down, left, right)
    where the player can be moved to. A neighbor is considered valid if (1) it is within the bounds of the maze
    and (2) not a wall ('#').

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        position (tuple[int, int]): The current position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of valid neighboring positions.
    """
    # construct the direction array: list[tuple[int, int]] (up, down, left, right)
    # test the position in each direction
    dir = [(-1,0),(1,0),(0,-1),(0,1)]
    new_dir = []

    rows = len(maze)
    col = len(maze[0])

    x = position[0]
    y = position[1]
    for d in dir :
         dx = x + d[0]
         dy = y + d[1]
         if(dx >= 0 and dy >=0 and dx < rows and dy < col) : 
                if maze[dx][dy] != "#":
                    new_dir.append((dx,dy))
 
    return new_dir



def bfs(maze: list[str], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    """Performs a breadth-first search (BFS) to find the shortest path from start to target in the maze.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        start (tuple[int, int]): The starting position in the maze as (row, column).
        target (tuple[int, int]): The target position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of positions representing the shortest path from start to target,
        including both start and target. If no path exists, returns an empty list.
    """
    # from collections you can import deque for using a queue.
    q = deque([(start,[start])]) #current node, current path

    vis = {start} 
    while q : 
         curr_node,path = q.popleft()

         if curr_node == target : 
          return path
         for neighbour in get_neighbors(maze,curr_node) : 
              if neighbour not in vis : 
                   vis.add(neighbour)
                   new_path = path + [neighbour]
                   q.append((neighbour,new_path))
    
    return None



def dfs(maze: list[str], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    """Performs a depth-first search (DFS) to find the shortest path from start to target in the maze.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        start (tuple[int, int]): The starting position in the maze as (row, column).
        target (tuple[int, int]): The target position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of positions representing the shortest path from start to target,
        including both start and target. If no path exists, returns an empty list.
    """
    # you can use a list as a stack in Python.

    stack = [(start,[start])] #current node, current path

    vis = {start} 
    while start : 
         curr_node,path = stack.pop()

         if curr_node == target : 
          return path
         for neighbour in get_neighbors(maze,curr_node) : 
              if neighbour not in vis : 
                   vis.add(neighbour)
                   new_path = path + [neighbour]
                   stack.append((neighbour,new_path))
    
    return None



def print_maze_with_path(maze: list[str], path: list[tuple[int, int]]) -> None:
    """Prints the maze to the console, marking the path with colored characters.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        path (list[tuple[int, int]]): A list of positions representing the path to be marked.
    Returns:
        None
    """
    # ANSI escape codes for colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    maze_copy = [list(row) for row in maze]

    for r, c in path:
        if maze_copy[r][c] not in ('S', 'T'):
            maze_copy[r][c] = f"{RED}x{RESET}"

    # Color the start and target positions
    for r, row in enumerate(maze_copy):
        for c, val in enumerate(row):
            if val == 'S':
                maze_copy[r][c] = f"{GREEN}S{RESET}"
            elif val == 'T':
                maze_copy[r][c] = f"{YELLOW}T{RESET}"

    # Print the maze
    for row in maze_copy:
        print(''.join(row))




if __name__ == "__main__":
    # Example usage: py maze_search.py dfs/bfs maze.txt
    if len(sys.argv) !=3 :
        print("Usage : py maze_search.py dfs/bfs maze.txt ")
        sys.exit(1)

    maze = read_maze(sys.argv[2])
    start_end = find_start_and_target(maze)
    if(sys.argv[1] == "bfs") :
       path = bfs(maze,start_end[0],start_end[1])
    elif(sys.argv[1] == "dfs") : 
        path = dfs(maze,start_end[0],start_end[1])
    
    if(path == None) :
         print("There is no path")
    else :
        print_maze_with_path(maze,path)
