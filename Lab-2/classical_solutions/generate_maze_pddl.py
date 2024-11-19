def generate_pddl_from_maze(maze, start, goal, problem_name):
    rows = len(maze)
    cols = len(maze[0])

    # Generate x and y positions
    x_coord = [f"x{i+1}" for i in range(cols)]
    y_coord = [f"y{i+1}" for i in range(rows)]

    # Increment and decrement relationships
    inc_x = " ".join(
        [f"(inc {x_coord[i]} {x_coord[i+1]})" for i in range(len(x_coord) - 1)])
    inc_y = " ".join(
        [f"(inc {y_coord[i]} {y_coord[i+1]})" for i in range(len(y_coord) - 1)])
    dec_x = " ".join(
        [f"(dec {x_coord[i+1]} {x_coord[i]})" for i in range(len(x_coord) - 1)])
    dec_y = " ".join(
        [f"(dec {y_coord[i+1]} {y_coord[i]})" for i in range(len(y_coord) - 1)])

    # Identify walls
    walls = []
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "X":
                walls.append(f"(obstacle {x_coord[x]} {y_coord[y]})")

    walls_str = " ".join(walls)

    # Define agent start and goal positions
    start_x, start_y = start
    goal_x, goal_y = goal
    start_position = f"(at ag {x_coord[start_x]} {y_coord[start_y]})"
    goal_position = f"(at ag {x_coord[goal_x]} {y_coord[goal_y]})"

    # Create PDDL structure
    pddl = f"""
(define (problem maze-{problem_name})
  (:domain maze)

  (:objects {" ".join(x_coord)} {" ".join(y_coord)} - coordinate ag - agent)

  (:init
    ; Adjacency definition
    {inc_x}
    {inc_y}
    {dec_x}
    {dec_y}

    ; Obstacles
    {walls_str}

    ; Initial position
    {start_position}
  )

  (:goal
    ; Goal position
    {goal_position}
  )
)
"""
    return pddl.strip()


# Input maze as a list of strings
maze_input = [
    ".....X....X....X....",
    "XXXX.XXXX.X.XXXXXXX.",
    ".....X....X.....X.X.",
    ".XXXXX.XXXXXX.X.X.X.",
    ".X.....X......X.X.X.",
    "...XXX.X.XXXXXX.X...",
    "XXXX...X.X......X.XX",
    ".....X.X.X.XXXXXX...",
    ".XXXXX.X.X......XXX.",
    ".X.....X.XXXXXX.X...",
    ".XXXXXXX.X..X...X.X.",
    ".........X.XX.XXX.X.",
    "XXXXXXXXXX....X...X.",
    ".........X.XXXX.XXX.",
    ".XXXXXXXXX.X..X...X.",
    "...........X.XXXX.XX",
    ".XXXX.XXXXXX.X......",
    "....X........X.XXXX.",
    "XXX.XXXXXXXXXX....X.",
    "...............XX.X."
]

# Define start and goal positions as (x, y)
start_position = (19, 19)  # Bottom-right corner
goal_position = (0, 0)  # Top-left corner
problem_name = "F"

# Generate PDDL
pddl_output = generate_pddl_from_maze(
    maze_input, start_position, goal_position, problem_name)

# Save to file
with open("F.pddl", "w") as file:
    file.write(pddl_output)

print(f"PDDL problem file generated: {problem_name}.pddl")
