'''
--- Day 8: Haunted Wasteland ---
You're still riding a camel across Desert Island when you spot a sandstorm quickly approaching. When you turn to warn the Elf, she disappears before your eyes! To be fair, she had just finished warning you about ghosts a few minutes ago.

One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about how to navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains a list of left/right instructions, and the rest of the documents seem to describe some kind of network of labeled nodes.

It seems like you're meant to use the left/right instructions to navigate the network. Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!

After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now, and you have to follow the left/right instructions until you reach ZZZ.

This format defines each node of the network individually. For example:

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.

Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes 6 steps to reach ZZZ:

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

Your puzzle answer was 13301.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had the camel follow the instructions, but you've barely left your starting position. It's going to take significantly more steps to escape!

What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of spacetime? Only one way to find out.

After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

For example:

LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

Step 0: You are at 11A and 22A.
Step 1: You choose all of the left paths, leading you to 11B and 22B.
Step 2: You choose all of the right paths, leading you to 11Z and 22C.
Step 3: You choose all of the left paths, leading you to 11B and 22Z.
Step 4: You choose all of the right paths, leading you to 11Z and 22B.
Step 5: You choose all of the left paths, leading you to 11B and 22C.
Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
So, in this example, you end up entirely on nodes that end in Z after 6 steps.

Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?
'''

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