from collections import defaultdict, deque
import re

system_dict = defaultdict()

def qc(pt):
    global system_dict
    stack = []
    stack.append('in')
    x,m,a,s = pt
    
    while stack:
        node = stack.pop()
    
        if node == 'A':
            return True
        elif node == 'R':
            return False

        qc_cond = system_dict[node]
            
        for conditions in qc_cond[:-1]:
            if eval(conditions[0]):
                stack.append(conditions[1])
                # print('condition met')
                break
            else:
                pass
                # print('condition not met')
        else:
            stack.append(qc_cond[-1][0])
            # print("no other rules met, default condition applied")

    return False

def find_n():
    global system_dict
    intervals = deque()
    nodes = deque()
    A = []
    XMAS = [[1, 4000],[1, 4000],[1, 4000],[1, 4000]]
    nodes.append('in')
    intervals.append(XMAS)
    re_pattern = f'(?<=[<>])|(?=[<>])'
   
    # I think this should be BFS traversal of graph to check each node
    # pass nested list into while loop, while nodes queue is true
    # traverse tree at each level and evaluate respective nested list for that 
    # workflow and push new nodes to nodes queue and new lists to intervals queue
    # when A node reached, append final list to A list 
    # we will use this list to calculate n number of choices
    tracking = []

    while nodes:
        node = nodes.popleft()

        curr_list = intervals.popleft()
        tracking.append((curr_list, node))
        
        xmin, xmax = curr_list[0]
        mmin, mmax = curr_list[1]
        amin, amax = curr_list[2]
        smin, smax = curr_list[3]
        
        oxmin, oxmax = curr_list[0]
        ommin, ommax = curr_list[1]
        oamin, oamax = curr_list[2]
        osmin, osmax = curr_list[3]




        if node == 'A':
            A.append(curr_list)
            # print('part accepted, appending to A')
            continue
        elif node == 'R':
            # print('part rejected')
            continue

        qc_cond = system_dict[node]
        
        for conditions in qc_cond[:-1]:
            ch, cond, value = re.split (re_pattern, conditions[0] )
            value = int(value)

            xmin, xmax = oxmin, oxmax
            mmin, mmax = ommin, ommax
            amin, amax = oamin, oamax
            smin, smax = osmin, osmax

            if ch == 'x':
                if cond == '<' and curr_list[0][1] > value:
                    xmax = value - 1
                    oxmin = value
                    oxmax = curr_list[0][1]
                elif cond == '>' and curr_list[0][0] < value:
                    xmin = value + 1
                    oxmax = value
                    oxmin = curr_list[0][0]

            elif ch == 'm':
                if cond == '<' and curr_list[1][1] > value:
                    mmax = value - 1
                    ommin = value
                    ommax = curr_list[1][1]
                elif cond == '>' and curr_list[1][0] < value:
                    mmin = value + 1
                    ommax = value
                    ommin = curr_list[1][0]

            elif ch == 'a':
                if cond == '<' and curr_list[2][1] > value:
                    amax = value - 1
                    oamin = value
                    oamax = curr_list[2][1]
                elif cond == '>' and curr_list[2][0] < value:
                    amin = value + 1
                    oamax = value
                    oamin = curr_list[2][0]

            elif ch == 's':
                if cond == '<' and curr_list[3][1] > value:
                    smax = value - 1
                    osmin = value
                    osmax = curr_list[3][1]
                elif cond == '>' and curr_list[3][0] < value:
                    smin = value + 1
                    osmax = value
                    osmin = curr_list[3][0]
            
            new_list = [[xmin, xmax], [mmin, mmax], [amin,amax], [smin,smax]]
            intervals.append(new_list)
            nodes.append(conditions[1])

        else:
            new_list = [[oxmin, oxmax], [ommin, ommax], [oamin,oamax], [osmin,osmax]]
            
            intervals.append(new_list)
            nodes.append(qc_cond[-1][0])
            # print("no other rules met, default condition applied")

    return A, tracking

def calculate_combinations(ranges_list):
    total_combinations = 0

    for ranges in ranges_list:
        combinations_for_this_list = 1
        for r in ranges:
            min_val, max_val = r
            combinations_for_this_list *= (max_val - min_val + 1)
        total_combinations += combinations_for_this_list

    return total_combinations



def main(pt, part_two=False):
    # problem is a graph problem.  We represent the graph as a dictionary.  key is the node (workflow identifier), value is a tuple
    # that contains information on what the conditions are to move from current node to next node 
    # if none of the conditionals are met, then the last index value is the default next node
    # We start at the [in] node and end at either [R] or [A], there are multiple nodes in between
    # use DFS to traverse graph and resolve each part, sum total value of part (xmas) and add to total

    if not part_two:
        total = 0 
        for part in pt:
            if qc(part):
                total += sum(part)
    else:
        A_list, tracking = find_n()
        # for i in tracking:
        #     print(i)
        # for i in A_list:
        #     print(i)
        # print(A_list)
        total = calculate_combinations(A_list)


    
    return total


if __name__ == '__main__':

    path = r'C:\AOC\2023\Day_19\test_data.txt'
    # path = r'C:\AOC\2023\Day_19\data.txt'
    
    # 167_409_079_868_000
    with open(path, 'r') as file:
        input = file.read().split('\n\n')

        workflows, parts = input
        parts = [[int(j.split('=')[1]) for j in i.strip('{}').split(',')] for i in parts.split()]
        
        workflows = workflows.split('\n')

        for workflow in workflows:
            key, conditions = workflow.split('{')
            various = [i.split(':') for i in conditions.strip('}').split(',')]
            system_dict[key] = various   

    print(system_dict)
    total = main(parts, part_two=True)
    print(total)

