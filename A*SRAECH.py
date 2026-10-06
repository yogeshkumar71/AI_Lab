import copy
from queue import PriorityQueue

class Node:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def get_blank_pos(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

def get_misplaced_tiles(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

def get_manhattan_distance(state, goal):
    distance = 0
    goal_pos = {}
    for i in range(3):
        for j in range(3):
            goal_pos[goal[i][j]] = (i, j)
   
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                g_i, g_j = goal_pos[val]
                distance += abs(i - g_i) + abs(j - g_j)
    return distance

def get_successors(node):
    successors = []
    r, c = node.get_blank_pos()
    moves = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]
   
    for dr, dc, move_name in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = copy.deepcopy(node.state)
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            successors.append(Node(new_state, node, move_name, node.depth + 1))
    return successors

def a_star(start_state, goal_state, heuristic_type):
    start_node = Node(start_state)
    if heuristic_type == 1:
        start_node.cost = get_misplaced_tiles(start_state, goal_state)
    else:
        start_node.cost = get_manhattan_distance(start_state, goal_state)
       
    open_list = PriorityQueue()
    open_list.put(start_node)
   
    closed_set = set()
   
    while not open_list.empty():
        current_node = open_list.get()
       
        state_tuple = tuple(tuple(row) for row in current_node.state)
        if state_tuple in closed_set:
            continue
           
        closed_set.add(state_tuple)
       
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]
           
        for successor in get_successors(current_node):
            suc_tuple = tuple(tuple(row) for row in successor.state)
            if suc_tuple in closed_set:
                continue
               
            if heuristic_type == 1:
                h = get_misplaced_tiles(successor.state, goal_state)
            else:
                h = get_manhattan_distance(successor.state, goal_state)
               
            successor.cost = successor.depth + h
            open_list.put(successor)
           
    return None

def print_puzzle(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()

if __name__ == "__main__":
    start = [,
 ,
        [7, 5, 8]
    ]
   
    goal = [,
 ,
        [7, 8, 0]
    ]
   
    print("--- Case 1: Misplaced Tiles Heuristic ---")
    path1 = a_star(start, goal, heuristic_type=1)
    if path1:
        for node in path1:
            if node.move:
                print(f"Move: {node.move} (Depth/g: {node.depth}, Cost/f: {node.cost})")
            else:
                print(f"Start State (Cost/f: {node.cost})")
            print_puzzle(node.state)
           
    print("--- Case 2: Manhattan Distance Heuristic ---")
    path2 = a_star(start, goal, heuristic_type=2)
    if path2:
        for node in path2:
            if node.move:
                print(f"Move: {node.move} (Depth/g: {node.depth}, Cost/f: {node.cost})")
            else:
                print(f"Start State (Cost/f: {node.cost})")
            print_puzzle(node.state)
