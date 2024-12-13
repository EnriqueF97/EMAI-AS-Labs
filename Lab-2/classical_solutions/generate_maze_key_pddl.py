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

    # Identify walls, keys, and doors
    walls = []
    keys = []
    key_at = []
    door_at = []
    door_locked = []
    key_unlocks = []
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "X":  # Wall
                walls.append(f"(obstacle {x_coord[x]} {y_coord[y]})")
            elif cell.islower():  # Keys (lowercase letters)
                key_symbol = f"k{cell}"
                if key_symbol not in keys:
                    keys.append(key_symbol)
                key_at.append(
                    f"(key-at {key_symbol} {x_coord[x]} {y_coord[y]})")
            elif cell.isupper():  # Doors (uppercase letters)
                door_x = x_coord[x]
                door_y = y_coord[y]
                door_at.append(f"(door-at {door_x} {door_y})")
                door_locked.append(f"(door-locked {door_x} {door_y})")
                # Automatically create key-door relationship
                key_char = cell.lower()
                key_symbol = f"k{key_char}"
                if key_symbol not in keys:
                    keys.append(key_symbol)
                    # Note: Key may not be present in the maze
                key_unlocks.append(
                    f"(key-unlocks {key_symbol} {door_x} {door_y})")

    # Prepare strings for the PDDL sections
    walls_str = " ".join(walls)
    key_at_str = " ".join(key_at) if key_at else "; Keys"
    door_at_str = " ".join(door_at) if door_at else "; Doors"
    door_locked_str = " ".join(
        door_locked) if door_locked else "; Doors are unlocked"
    key_unlocks_str = " ".join(
        key_unlocks) if key_unlocks else "; Key-Door Relationships"

    # Define agent start and goal positions
    start_x, start_y = start
    goal_x, goal_y = goal
    start_position = f"(at ag {x_coord[start_x]} {y_coord[start_y]})"
    goal_position = f"(at ag {x_coord[goal_x]} {y_coord[goal_y]})"

    # Create PDDL structure
    pddl = f"""
(define (problem maze-{problem_name})
  (:domain maze-key)

  (:objects {" ".join(x_coord)} {" ".join(y_coord)} - coordinate ag - agent {" ".join(keys)} - key)

  (:init
    ; Adjacency definition
    {inc_x}
    {inc_y}
    {dec_x}
    {dec_y}

    ; Walls
    {walls_str}

    ; Keys
    {key_at_str}

    ; Doors
    {door_at_str}
    {door_locked_str}

    ; Key-Door Relationships
    {key_unlocks_str}

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
    "...W..XwXr",
    "XXXX..X.X.",
    "vXuX.pXUXV",
    ".X.X..XoXq",
    "OXPXQRXSXT",
    "sXtXijXlXk",
    "IXJXKLXMXN",
    "fXnXc.XeXd",
    "CXDXEFXGXH",
    "mAgB..abh."
]

# Define start and goal positions as (x, y)
start_position = (9, 9)  # Bottom-right corner
goal_position = (0, 0)  # Top-left corner
problem_name = "J"

# Generate PDDL
pddl_output = generate_pddl_from_maze(
    maze_input, start_position, goal_position, problem_name)

# Save to file
with open(f"{problem_name}.pddl", "w") as file:
    file.write(pddl_output)

print(f"PDDL problem file generated: {problem_name}.pddl")
