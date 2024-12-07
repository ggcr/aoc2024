
def findXMAS(grid, coords):
    set_tl = set() # topleft diagonal
    set_br = set() # bottomright diagonal

    i, j = coords

    set_tl.add(grid[(i, j)]) # A
    set_tl.add(grid[(i-1, j-1)])
    set_tl.add(grid[(i+1, j+1)])

    set_br.add(grid[(i, j)]) # A
    set_br.add(grid[(i+1, j-1)])
    set_br.add(grid[(i-1, j+1)])

    for ch in "MAS":
        if ch not in set_tl or ch not in set_br:
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
    for i in range(1, ROWS-1):
        for j in range(1, COLS-1):
            if data[(i, j)] == 'A':
                if findXMAS(data, (i, j)) == True:
                    total_xmas += 1
    print(total_xmas)
