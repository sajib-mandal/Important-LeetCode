class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 1
        visit = set()
        rows, cols = len(grid), len(grid[0])
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            area = 1
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        (nr, nc) not in visit and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        area += 1
            return area
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    visit.add((r, c))
                    maxArea = max(maxArea, bfs(r, c))
        return maxArea
        
        
        
        # 2
        rows, cols = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or
                grid[r][c] == 0 or (r, c) in visit):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        return area
        
        
        
        # 3
        visited = set()
        max_size = 0
        row,col = len(grid), len(grid[0])
        directions= [(-1,0), (0,1), (1,0), (0,-1)]
        def dfs(x, y):
            area = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < row and 0 <= ny < col and 
                    (nx,ny) not in visited and grid[nx][ny] == 1):
                    visited.add((nx, ny))
                    area += dfs(nx, ny)
            return area
        
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1 and (x,y) not in visited:
                    visited.add((x, y))
                    max_size = max(dfs(x, y), max_size)
        return max_size
        
        
        
        
        # 4
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            area = 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while queue:
                r, c = queue.popleft()  
                for (dr, dc) in directions:
                    next_r, next_c = r + dr, c + dc
                    
                    if (-1 < next_r < ROWS and -1 < next_c < COLS and 
                        (next_r, next_c) not in visited and grid[next_r][next_c] == 1):
                        queue.append((next_r, next_c))
                        visited.add((next_r, next_c))
                        area+=1
            return area
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c)  not in visited:
                    visited.add((r, c))
                    area = bfs(r, c)
                    max_area = max(area, max_area)
        return max_area
        
