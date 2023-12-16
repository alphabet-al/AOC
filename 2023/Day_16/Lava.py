"""
--- Day 16: The Floor Will Be Lava ---
With the beam of light completely focused somewhere, the reindeer leads you deeper still into the Lava Production Facility. At some point, you realize 
that the steel facility walls have been replaced with cave, and the doorways are just cave, and the floor is cave, and you're pretty sure this is actually 
just a giant cave.

Finally, as you approach what must be the heart of the mountain, you see a bright light in a cavern up ahead. There, you discover that the beam of light 
you so carefully focused is emerging from the cavern wall closest to the facility and pouring all of its energy into a contraption on the opposite side.

Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid containing empty space (.), mirrors (/ and \), and splitters 
(| and -).

The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid converts some of the beam's light into heat to 
melt the rock in the cavern.

You note the layout of the contraption (your puzzle input). For example:

.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
The beam enters in the top-left corner from the left and heading to the right. Then, its behavior depends on what it encounters as it moves:

If the beam encounters empty space (.), it continues in the same direction.
If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the mirror. For instance, a rightward-moving beam 
that encounters a / mirror would continue upward in the mirror's column, while a rightward-moving beam that encounters a \ mirror would continue downward 
from the mirror's column.
If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter were empty space. For instance, a 
rightward-moving beam that encounters a - splitter would continue in the same direction.
If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the two directions the splitter's pointy 
ends are pointing. For instance, a rightward-moving beam that encounters a | splitter would split into two beams: one that continues upward from the 
splitter's column and one that continues downward from the splitter's column.
Beams do not interact with other beams; a tile can have many beams passing through it at the same time. A tile is energized if that tile has at least 
one beam pass through it, reflect in it, or split in it.

In the above example, here is how the beam of light bounces around the contraption:

>|<<<\....
|v-.\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\
.v../2\\..
<->-/vv|..
.|<<<2-|.\
.v//.|.v..
Beams are only shown on empty tiles; arrows indicate the direction of the beams. If a tile contains beams moving in multiple directions, the number of 
distinct directions is shown instead. Here is the same diagram but instead only showing whether a tile is energized (#) or not (.):

######....
.#...#....
.#...#####
.#...##...
.#...##...
.#...##...
.#..####..
########..
.#######..
.#...#.#..
Ultimately, in this example, 46 tiles become energized.

The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing the current situation. With the beam 
starting in the top-left heading right, how many tiles end up being energized?

Your puzzle answer was 7608.

--- Part Two ---
As you try to work out what might be wrong, the reindeer tugs on your shirt and leads you to a nearby control panel. There, a collection of buttons 
lets you align the contraption so that the beam enters from any edge tile and heading away from that edge. (You can choose either of two directions 
for the beam if it starts on a corner; for instance, if the beam starts in the bottom-right corner, it can start heading either left or upward.)

So, the beam could start on any tile in the top row (heading downward), any tile in the bottom row (heading upward), any tile in the leftmost column 
(heading right), or any tile in the rightmost column (heading left). To produce lava, you need to find the configuration that energizes as many tiles 
as possible.

In the above example, this can be achieved by starting the beam in the fourth tile from the left in the top row:

.|<2<\....
|v-v\^....
.v.v.|->>>
.v.v.v^.|.
.v.v.v^...
.v.v.v^..\
.v.v/2\\..
<-2-/vv|..
.|<<<2-|.\
.v//.|.v..
Using this configuration, 51 tiles are energized:

.#####....
.#.#.#....
.#.#.#####
.#.#.##...
.#.#.##...
.#.#.##...
.#.#####..
########..
.#######..
.#...#.#..
Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized in that configuration?

Your puzzle answer was 8221.
"""

def check_boundary(grid, pos):
    r,c = int(pos.imag), int(pos.real)

    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


def get_moves(pos, dx_dy, grid):
    r,c = int(pos.imag), int(pos.real)
    tile = grid[r][c]
    moves = []
    # print(r,c, tile, dx_dy)

    if tile == '|':
        if (dx_dy == 1 or dx_dy == -1):
            # print('vertical splitting')
            moves.append(1j)
            moves.append(-1j)
        elif (dx_dy == 1j or dx_dy == -1j):
            return [dx_dy]
    
    elif tile == '-':
        if (dx_dy == 1 or dx_dy == -1):
            return [dx_dy]
        elif (dx_dy == 1j or dx_dy == -1j):
            # print('horizontal split')
            moves.append(1)
            moves.append(-1)
    
    # '\\' : right => down / up => left / down => right / left => up (current direction => new direction)
    elif tile == '\\':
        if dx_dy == 1:  # right to down
            return [1j]
        elif dx_dy == -1:   # left to up
            return [-1j]
        elif dx_dy == -1j:   # up to left
            return [-1]
        elif dx_dy == 1j:   # down to right
            return [1]
    
    # '/' : right => up / up => right / down => left / left => down
    elif tile == '/':
        if dx_dy == 1:  # right to up
            return [-1j]
        elif dx_dy == -1:   # left to down
            return [1j]
        elif dx_dy == -1j:   # up to right
            return [1]
        elif dx_dy == 1j:   # down to left
            return [-1]
    
    elif tile == '.':
        return [dx_dy]
    
    return moves


def dfs_iterative(grid, start_pos, start_dx_dy):
    visited_set = set()
    stack = [(start_pos, start_dx_dy)]
    path_set = set()

    while stack:
        pos, dx_dy = stack.pop()

        if not check_boundary(grid, pos) or (pos, dx_dy) in path_set:
            continue

        visited_set.add(pos)
        path_set.add((pos, dx_dy))
        moves = get_moves(pos, dx_dy, grid)
        for move in moves:
            new_pos = pos + move
            stack.append((new_pos, move))

    return visited_set


def main(data, part_two = False):
    perimeter_dict = {'top_row':  list ( complex(i, 0) for i in range( len( data[0] ) ) ),
                        'bottom_row' : list ( complex( i, len( data ) - 1) for i in range( len( data[0] ) )),
                        'left_col' : list (complex(0, i) for i in range(len(data))),
                        'right_col' : list (complex(len(data[0]) - 1, i) for i in range(len(data)))
                        }
    
    dx_dy_dict = {'top_row' : 1j,
                    'bottom_row' : -1j,
                    'left_col' : 1,
                    'right_col' : -1
                    }

    if not part_two:
        start_pos = 0 + 0j
        dx_dy = 1
        visited_set = dfs_iterative(data, start_pos, dx_dy)
        return len(visited_set)
    else:  
        max_val = 0      
        for k,v in perimeter_dict.items():
            for start_pos in v:
                dx_dy = dx_dy_dict[k]
                visited_set = dfs_iterative(data, start_pos, dx_dy)
                energized_count = len(visited_set)
                if energized_count > max_val:
                    max_val = energized_count
        return max_val
    


if __name__ == '__main__':

    # path = r'C:\AOC\2023\Day_16\test_data.txt'
    path = r'C:\AOC\2023\Day_16\data.txt'

    with open(path, 'r') as file:
        input = [[ch for ch in i] for i in file.read().splitlines()]
    
    total = main(input, part_two = True)
    print(total)

