from collections import deque
from heapq import heapify,heappop,heappush
from functools import cache
import sys

sys.setrecursionlimit(100000000)

def dfs_min_cost(A, B, x, y):
    buttons = [A, B]

    @cache    
    def dfs(x, y, cost):
        print(x,y)        
        if x == 0 and y == 0:
            return cost
        
        if x < 0 or y < 0:
            return float("inf")
        
        min_cost = float("inf")
        for i, button in enumerate(buttons):
            if i == 0:
                newcost = cost + 3
            else:
                newcost = cost + 1
            nx = x - button[0]
            ny = y - button[1]
            
            min_cost =  min( min_cost, ( dfs(nx, ny, newcost) )) 
            
        return min_cost

    return dfs(x, y, 0)



def main(machines, pt2 = False):
    cost = 0
    for v in machines.values():
        A, B, PRIZE = v
        if not pt2:
            x,y = PRIZE
        else:
            x,y = PRIZE[0] + 10000000000000, PRIZE[1] + 10000000000000
        dfs_cost = dfs_min_cost(A, B, x, y)
        print(dfs_cost)
        if dfs_cost != float("inf"):
            cost += dfs_cost
    return cost 

    

if __name__ == "__main__":
    path = r"C:\AOC\2024\day_13\test_data.txt" 
    # path = r"C:\AOC\2024\day_13\data.txt" 

    with open(path, "r") as f:
        machines = f.read().split("\n\n")
        claw_machines = {}
        for i, machine in enumerate(machines):
            temp = []
            for j in machine.split("\n"):
                j1,j2 = j.split(", ")
                _, jx = j1.split('X')
                _, jy = j2.split('Y')
                if jx[0] == "=" and jy[0] == "=":
                    jx = jx[1:]
                    jy = jy[1:]
                temp.append((int(jx),int(jy)))
            claw_machines[i] = temp
            
    tokens = main(claw_machines, pt2 = True)
    print(f"Fewest tokens: {tokens}")