import numpy as np

from collections import deque
from heapq import heapify,heappop,heappush
from functools import cache
from numpy.linalg import solve



def main(machines):
    cost = 0
    for v in machines.values():
        path_cost = np.array([3, 1])
        A, B, PRIZE = v
        b = np.array( [PRIZE[0] + 10000000000000, PRIZE[1] + 10000000000000] )
        a = np.array( [ [A[0], B[0]], 
                        [A[1], B[1]] 
                      ])
        ans = np.round(solve(a,b), decimals=3)

        if ans[0] % 1 == ans[1] % 1 == 0:
            cost += ans @ path_cost

    return int(cost)

    

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