class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs solution - traverse all 4 directions
        # whenever we reach a 1
        rows, cols= len(grid), len(grid[0])
        directions= [(1,0), (-1,0), (0,1), (0, -1)]

        def bfs(r,c): 
            q= deque()
            grid[r][c] = '0' # mark starting cell as 0 after visiting
            q.append((r,c))

            while q: 
                row, col= q.popleft()
                for dr, dc in directions: 
                    nr, nc= dr + row, dc + col 
                    # Skip if out of bounds, water, or already visited
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == '0'):
                        continue
                    
                    q.append((nr, nc))

                    # mark newly discovered neighbor as visited 
                    grid[nr][nc]= '0'

        islands= 0
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == '1': 
                    bfs(r,c)
                    islands += 1
        
        return islands