from collections import deque
from heapq import heapify,heappop,heappush
from functools import cache

@cache
def bfs(A, B, PRIZE):
    buttons = [A, B]
    q = []
    heappush(q, (0, (PRIZE[0], PRIZE[1])))

    while q:
        cost, (x,y) = heappop(q)
        
        if x == 0 and y == 0:
            return cost
               
        for i, button in enumerate(buttons):
            
            if i == 0:
                newcost = cost + 3
            else:
                newcost = cost + 1
            nx = x - button[0]
            ny = y - button[1]
            
            if nx < 0 or ny < 0:
                continue
            
            if (newcost, (nx,ny)) not in q:
                heappush(q, (newcost, (nx, ny)))

    return 0


def main(machines):
    cost = 0
    for v in machines.values():
        A, B, PRIZE = v
        cost += bfs(A, B, PRIZE)
    return cost 

    

if __name__ == "__main__":
    # path = r"C:\AOC\2024\day_13\test_data.txt" 
    path = r"C:\AOC\2024\day_13\data.txt" 

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
            
    tokens = main(claw_machines)
    print(f"Fewest tokens: {tokens}")