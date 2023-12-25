from heapq import heappush, heappop

if __name__ == '__main__':

    path = r'C:\AOC\2023\Day_17\test_data.txt'
    # path = r'C:\AOC\2023\Day_17\data.txt'

    with open(path, 'r') as file:
        grid = [[int(ch) for ch in i] for i in file.read().splitlines()]
        
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, r, c, dr, dc, n = heappop(pq)
        # print(hl,r,c,dr,dc,n)
        
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            print(hl)
            break

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))
        
        if n < 3:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    # print(nr,nc)
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))


