class IterativeDeepening:

    def __init__(self):
        self.stack = []
        self.maxDepth = 0
        self.depth = 0
        self.goalFound = False
        self.path = []

    def iterativeDeepening(self, maze, start, goal, max_limit):
        self.maxDepth = 0

        while self.maxDepth <= max_limit and not self.goalFound:
            visited = set()
            self.stack = []
            self.path = []
            self.depth = 0

            self.depthLimitedSearch(maze, start, goal, visited)

            if self.goalFound:
                print(f"Path found at depth {self.depth} using IDDFS")
                path_str = "[" + ", ".join([f"({x},{y})" for x, y in self.path]) + "]"
                print(f"Traversal Order: {path_str}")
                return

            self.maxDepth += 1

        print(f"Path not found at max depth {max_limit} using IDDFS")

    def depthLimitedSearch(self, maze, current, goal, visited):
        self.stack.append(current)
        visited.add(current)
        self.path.append(current)

        if current == goal:
            self.goalFound = True
            return

        if self.depth < self.maxDepth:
            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for move in moves:
                new_x = current[0] + move[0]
                new_y = current[1] + move[1]

                if self.isValid(new_x, new_y, maze, visited):
                    self.depth += 1
                    self.depthLimitedSearch(maze, (new_x, new_y), goal, visited)

                    if self.goalFound:
                        return

                    self.depth -= 1  


        self.stack.pop()
        self.path.pop()
        visited.remove(current)

    def isValid(self, x, y, maze, visited):
        if x < 0 or y < 0:
            return False
        if x >= len(maze) or y >= len(maze[0]):
            return False
        if maze[x][y] == 1:
            return False
        if (x, y) in visited:
            return False

        return True


if __name__ == "__main__":
    try:
        rows, cols = map(int, input().strip().split())

        maze = []
        for i in range(rows):
            row = list(map(int, input().strip().split()))
            maze.append(row)

        start_input = input("Start: ").strip()
        if start_input.startswith("Start:"): 
            start_input = start_input.replace("Start:", "").strip()
        sx, sy = map(int, start_input.split())

        target_input = input("Target: ").strip()
        if target_input.startswith("Target:"): 
            target_input = target_input.replace("Target:", "").strip()
        tx, ty = map(int, target_input.split())

        max_depth = rows * cols

        start = (sx, sy)
        goal = (tx, ty)

        solver = IterativeDeepening()
        solver.iterativeDeepening(maze, start, goal, max_depth)

    except Exception as e:
        print("Wrong input format")