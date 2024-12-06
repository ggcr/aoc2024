import sys

sys.setrecursionlimit(7500)

def parseFile(file_path: str) -> (int, int, dict):
    with open(file_path, 'r') as fd:
        data = fd.readlines()
        COLS = len(data[0].strip())
        ROWS = len(data)
        ret = {}
        coords0 = (0,0)
        for i in range(ROWS):
            for j in range(COLS):
                if data[i][j] == "^":
                    ret[(i, j)] = "."
                    coords0 = (i, j)
                else:
                    ret[(i, j)] = data[i][j]
                        
    def guardianPath(coords, direction, visited):
        if coords not in ret: # out of bounds
            return visited
        i, j = coords
        visited.add(coords)
        if direction == 'up':
            nextDir = 'right'
            nextCoords = (i-1, j)
        elif direction == 'down':
            nextDir = 'left'
            nextCoords = (i+1, j)
        elif direction == 'left':
            nextDir = 'up'
            nextCoords = (i, j-1)
        else:
            nextDir = 'down'
            nextCoords = (i, j+1)
        if nextCoords in ret and ret[nextCoords] != ".":
            return guardianPath(coords, nextDir, visited)
        else:
            return guardianPath(nextCoords, direction, visited)

    vis = guardianPath(coords0, 'up', set())
    print(len(vis))


parseFile('./input.txt')
