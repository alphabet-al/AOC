from ortools.sat.python import cp_model

def main():
    # Initialize the CP model
    model = cp_model.CpModel()

    # Define the lines (initial points and velocities)
    lines = [
        ((19, 13), (-2, 1)),
        ((18, 19), (-1, -1)),
        ((20, 25), (-2, -2)),
        ((12, 31), (-1, -2)),
        ((20, 19), (1, -5))
    ]

    # Spatial bounds
    min_x, max_x = 7, 27
    min_y, max_y = 7, 27

    # Time range
    max_time = 10  # Adjust based on your requirements

    # Variables for positions at each time step
    positions = {}
    for t in range(max_time):
        for i, ((x0, y0), (vx, vy)) in enumerate(lines):
            x_t = model.NewIntVar(min_x, max_x, f'x_{i}_{t}')
            y_t = model.NewIntVar(min_y, max_y, f'y_{i}_{t}')
            positions[(i, t)] = (x_t, y_t)

            # Movement constraints
            if t == 0:
                model.Add(x_t == x0)
                model.Add(y_t == y0)
            else:
                model.Add(x_t == positions[(i, t-1)][0] + vx)
                model.Add(y_t == positions[(i, t-1)][1] + vy)

    # Constraints for intersections
    for t in range(max_time):
        for i in range(len(lines)):
            for j in range(i + 1, len(lines)):
                xi, yi = positions[(i, t)]
                xj, yj = positions[(j, t)]

                # Check if lines i and j intersect at time t
                intersect = model.NewBoolVar(f'intersect_{i}_{j}_{t}')
                model.Add(xi == xj).OnlyEnforceIf(intersect)
                model.Add(yi == yj).OnlyEnforceIf(intersect)

    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        for t in range(max_time):
            for i in range(len(lines)):
                for j in range(i + 1, len(lines)):
                    if solver.Value(intersect):
                        xi, yi = solver.Value(xi), solver.Value(yi)
                        print(f"Lines {i} and {j} intersect at ({xi}, {yi}) at time {t}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
