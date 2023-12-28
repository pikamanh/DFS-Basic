import sys

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, node):
        self.stack.append(node)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        
    def current_stack(self):
        if len(self.stack) > 0:
            return True

class Maze:
    def __init__(self):
        with open(sys.argv[1]) as f:
            self.src = f.read()

        self.src = self.src.splitlines()

        self.height = len(self.src)
        self.width = max(len(line) for line in self.src)

        for i, line in enumerate(self.src):
            for j, element in enumerate(line):
                if element =="A":
                    self.start = (i, j)
                elif element =="B":
                    self.end = (i, j)
        
    def action(self, row, col):
        actions = {
            "up": (row - 1, col),
            "down": (row + 1, col),
            "left": (row, col - 1),
            "right": (row, col + 1)
        }

        return actions

    def solve(self):
        stack = Stack()
        explored = set()
        path = []
        self.numPath = 0

        start_node = Node(self.start, None, None)
        stack.add(start_node)

        while stack.current_stack():
            curr_node = stack.pop()

            if curr_node.state == self.end:
                while curr_node:
                    path.append(curr_node.state)
                    curr_node = curr_node.parent
                path.reverse()
                return path
            
            explored.add(curr_node.state)
            self.numPath += 1
            
            for action, (row, col) in self.action(*curr_node.state).items():
                if 0 <= row < self.height and 0 <= col < self.width and "#" not in self.src[row][col] and (row, col) not in explored:
                    next_node = Node((row, col), curr_node, action)
                    stack.add(next_node)
                    

        return Node
    
    def stored(self):
        maze = []
        for i, row in enumerate(self.src):
            rows = ""
            for j, col in enumerate(row):
                if col == "A":
                    rows+= ("A")
                elif col == "B":
                    rows+= ("B")
                elif col == "#":
                    rows+= ("█")
                elif col == " " and (i, j) in self.solve():
                    rows+= ("*")
                else:
                    rows+= " "
            maze.append(rows)

        return maze
    
    def print(self):
        for i in self.stored():
            print(i)

m = Maze()

print(m.print())
print(m.numPath)