#  733. Flood Fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = [(sr, sc)]
        visited = {(sr, sc)}
        color = image[sr][sc]
        while q:
            x, y = q.pop()
            image[x][y] = newColor
            for dirx, diry in directions:
                tx, ty = x + dirx, y + diry
                if (0 <= tx < m and 0 <= ty < n and image[tx][ty] == color and 
                    (tx, ty) not in visited):
                    q.append((tx, ty))
                    visited.add((tx, ty))
        return image
        
        
        
        
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image
    
    
    
    
        if not image or not image[0]:
            return []
        if image[sr][sc] == color:
            return image
        row = len(image)
        col = len(image[0])
        queue = deque()
        queue.append((sr, sc))
        old = image[sr][sc]
        image[sr][sc] = color
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xx, yy = x + dx, y + dy
                if xx < 0 or xx == row or yy < 0 or yy == col:
                    continue
                if image[xx][yy] != old:
                    continue
                image[xx][yy] = color
                queue.append((xx, yy))
        return image
        
        
        
        
        
        rowNum = len(image)
        colNum = len(image[0])
        visited = set()
        matchColor = image[sr][sc]       
        q = collections.deque()
        q.append((sr, sc))
        while q:
            currR, currC = q.popleft()
            visited.add((currR, currC))
            image[currR][currC] = color
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            for r, c in directions:
                nextR = currR + r
                nextC = currC + c 
                if (nextR >= 0 and nextR < rowNum and nextC >= 0 and nextC < colNum and (nextR, nextC) not in visited and image[nextR][nextC] == matchColor):
                    q.append((nextR, nextC))  
        return image
    
    
    
        
        diff = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        stack = [[sr, sc]]
        original_color = image[sr][sc]
        if color == original_color: return image
        while len(stack) > 0:
            r, c = stack.pop() 
            if image[r][c] == original_color:
                image[r][c] = color
            for i, j in diff:
                r1 = r + i
                c1 = c + j
                if (r1 >= 0 and r1 < len(image) and 
                    c1 >=0 and c1 < len(image[r1]) and 
                    image[r1][c1] == original_color):
                    stack.append([r1, c1])
        return image
