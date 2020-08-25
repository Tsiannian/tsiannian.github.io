from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        islands = set()
        searched = set()
        width = len(grid)
        height = len(grid[0])
        area = 0
        for x in range(0, width):
            for y in range(0, height):
                if (x, y) in searched:
                    continue
                # try to get island
                searched.add((x, y))
                if grid[x][y] == 0:
                    continue
                # island begin, get left and right
                island = self.getIsland(grid, x, y)
                for pos in island:
                    searched.add(pos)
                area = max(area, len(island))
        return area

    def getIsland(self, grid:List[List[int]], x, y):
        width = len(grid)
        height = len(grid[0])
        wait = set()
        wait.add((x, y))
        searched = set()
        island = set()
        while wait:
            temp = set()
            for pos in wait:
                x, y = pos[0], pos[1]
                searched.add((x, y))
                if grid[x][y] == 0:
                    continue
                island.add((x, y))
                if x > 0:
                    if (x-1, y) not in searched:
                        if grid[x-1][y] == 1:
                            temp.add((x-1, y))
                            island.add((x-1, y))
                if x + 1 < width:
                    if (x+1, y) not in searched:
                        if grid[x+1][y] == 1:
                            temp.add((x+1, y))
                            island.add((x-1, y))
                if y > 0:
                    if (x, y-1) not in searched:
                        if grid[x][y-1] == 1:
                            temp.add((x, y-1))
                            island.add((x, y-1))
                if y + 1 < height:
                    if (x, y+1) not in searched:
                        if grid[x+1][y] == 1:
                            temp.add((x, y+1))
                            island.add((x, y+1))
            wait.clear()                
            wait.update(temp)
        return island


if __name__ == "__main__":
    s = Solution()
    print(s.largestIsland([[1,0],[0,1]]))