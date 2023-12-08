from collections import deque

def parse(ve):
    adj = {}

    for i in ve[2:]:
        k, v = i.split(' = ')
        values = tuple(v.strip('()').split(', '))
        adj[k] = values
            
    return adj

def find_zzz(dir, lst):
    count = 0
    visited = []
    current = deque()
    current.append('AAA')

    while 'ZZZ' not in visited:
        index = count % len(dir)
        edges = lst[current[0]]
        
        if dir[index] == 'L':
            visited.append(current.pop())
            current.append(edges[0])
        
        else:
            visited.append(current.pop())
            current.append(edges[1])
        
        if 'ZZZ' in visited:
            break
        
        count += 1

    print(count)

def find_all_z(dir, lst):
    count = 0
    # list that stores the nodes that we have just visited, we should have the same number of nodes
    # at the end of the for loop as we did when we begane the loop, it should break out of while loop
    # when all the nodes in the visited list end in 'z'.  if they aren't all z, then we clear the list before then next loop
    visited = []
    current = deque()   # queue that stores currently visited nodes, contains key values of adjacency list

    # initialize the current queue with all keys that end in 'z'
    for k in lst.keys():
        if k[-1] == 'A':
            current.append(k) 
    # get number of start points, count of z's at the end must match this value
    start_A_count = len(current)
        
    while True:
        index = count % len(dir) # count is indexed by 1 at the end of each while loop....this lets us find the correct move
        current_copy = current.copy()   # need to make a copy because we need to traverse it and mutate it

        z_count = 0
        for current_node in current_copy:    # loop through each node in the current queue    
            edges = lst[current_node]
                                    
            if dir[index] == 'L':
                visited.append(current.popleft())
                current.append(edges[0])
            
            else:
                visited.append(current.popleft())
                current.append(edges[1])
            
            if current_node[-1] == 'Z':
                z_count += 1
        # print(visited)
        
        if z_count == start_A_count:
            break
        # else:
        #     visited.clear()

        count += 1
    # print(visited)
    print(count)
            
def main(data):
    directions = data[0]
    adj_list = parse(data)
    
    """ part 1 """
    # find_zzz(directions, adj_list)

    """ part 2 """
    find_all_z(directions, adj_list)


if __name__ == '__main__':
    # path =  r'C:\AOC\2023\Day_08\test_data3.txt'
    path =  r'C:\AOC\2023\Day_08\data.txt'

    with open(path, 'r') as file:
        input = file.read().splitlines()

    main(input)