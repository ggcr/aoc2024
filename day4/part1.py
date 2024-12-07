def getNextCoords(coords, dir):
    i, j = coords
    if dir == 0: # top
        nextCoords = (i-1, j)
    elif dir == 1: # top-right
        nextCoords = (i-1, j+1)
    elif dir == 2: # top-left
        nextCoords = (i-1, j-1)
    elif dir == 3: # right
        nextCoords = (i, j+1)
    elif dir == 4: # down
        nextCoords = (i+1, j)
    elif dir == 5: # down-right
        nextCoords = (i+1, j+1)
    elif dir == 6: # down-left
        nextCoords = (i+1, j-1)
    elif dir == 7: # left
        nextCoords = (i, j-1)
    return nextCoords

def findXMAS(grid, coords, dir):
    for ch in "XMAS":
        if coords in grid and grid[coords] == ch:
            coords = getNextCoords(coords, dir)
            continue
        else:
            return False
    return True

def parse_input(file_path: str) -> list():
    with open(file_path, 'r') as fd:
        lines = fd.readlines()
        data = {}
        i = 0
        j = 0
        for line in lines:
            j = 0
            for ch in line.strip():
                data[(i, j)] = ch
                j += 1
            i += 1
    return data, i, j

if __name__ == '__main__':
    data, ROWS, COLS = parse_input('./input.txt')
    total_xmas = 0
    for i in range(ROWS):
        for j in range(COLS):
            if data[(i, j)] == 'X':
                print(f"Starting position:{(i, j)}")
                for k in range(8):
                    if findXMAS(data, (i, j), k) == True:
                        total_xmas += 1
    print(total_xmas)
