import sys

sys.setrecursionlimit(100000)

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
                        
    def guardianPath(ret, coords, direction, visited, loops):
        if coords not in ret: # out of bounds
            return False
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
        # dirty solution, use the state of direction+coords in a set instead...
        if loops == 1000: # we are on a loop
            return True
        if nextCoords in ret and ret[nextCoords] != ".":
            return guardianPath(ret, coords, nextDir, visited, loops+1)
        else:
            return guardianPath(ret, nextCoords, direction, visited, loops)

    final_L = 0
    for i in range(ROWS):
        for j in range(COLS):
            if ret[(i, j)] == '.' and (i, j) != coords0:
                ret[(i, j)] = '#'
                if guardianPath(ret, coords0, 'up', set(), 0) == True:
                    final_L += 1
                ret[(i, j)] = '.'
    print(final_L)


parseFile('./input.txt')
