def compute_antinodes(grid, locs):
    for ch, coords in locs.items():
        for i in range(len(coords)):
            for j in range(i+1, len(coords)):
                start = coords[i]
                end = coords[j]
                subCoords = lambda x, y: (x[0] - y[0], x[1] - y[1])
                addCoords = lambda x, y: (x[0] + y[0], x[1] + y[1])
                anti0 = addCoords(start, subCoords(start, end))
                anti1 = addCoords(end, subCoords(end, start))
                if anti0 in grid:
                    grid[anti0] = '#'
                if anti1 in grid:
                    grid[anti1] = '#'
    return grid

def parse_input(file_path: str) -> list():
    with open(file_path, 'r') as fd:
        lines = fd.readlines()
        data = {}
        locs = {}
        i = 0
        j = 0
        for line in lines:
            j = 0
            for ch in line.strip():
                data[(i, j)] = ch
                if ch != '.' and ch != '#':
                    locs[ch] = locs.get(ch, []) + [(i, j)]
                j += 1
            i += 1
    return data, locs, i, j


if __name__ == '__main__':
    grid, locs, ROWS, COLS = parse_input('./input.txt')
    # compute all antinodes (and over-write)
    written_grid = compute_antinodes(grid, locs)
    # count how many #
    total = 0
    for k, v in written_grid.items():
        if v == '#':
           total += 1
    print(total)
