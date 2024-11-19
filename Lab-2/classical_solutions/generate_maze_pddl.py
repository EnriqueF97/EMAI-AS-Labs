def generate_pddl_from_maze(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])
    
    # Generate x and y positions
    x_positions = [f"x{i+1}" for i in range(cols)]
    y_positions = [f"y{i+1}" for i in range(rows)]

    # Increment and decrement relationships
    inc_x = " ".join([f"(inc {x_positions[i]} {x_positions[i+1]})" for i in range(len(x_positions) - 1)])
    inc_y = " ".join([f"(inc {y_positions[i]} {y_positions[i+1]})" for i in range(len(y_positions) - 1)])
    dec_x = " ".join([f"(dec {x_positions[i+1]} {x_positions[i]})" for i in range(len(x_positions) - 1)])
    dec_y = " ".join([f"(dec {y_positions[i+1]} {y_positions[i]})" for i in range(len(y_positions) - 1)])

    # Identify walls
    walls = []
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "X":
                walls.append(f"(wall {x_positions[x]} {y_positions[y]})")

    walls_str = " ".join(walls)

    # Define agent start and goal positions
    start_x, start_y = start
    goal_x, goal_y = goal
    start_position = f"(at {x_positions[start_x]} {y_positions[start_y]})"
    goal_position = f"(at {x_positions[goal_x]} {y_positions[goal_y]})"

    # Create PDDL structure
    pddl = f"""
(define (problem maze-problem)
  (:domain maze)
  
  (:objects {" ".join(x_positions)} {" ".join(y_positions)} - position)
  
  (:init
    ; Define increment (inc) and decrement (dec) relationships
    {inc_x}
    {inc_y}
    {dec_x}
    {dec_y}

    ; Walls
    {walls_str}

    ; Initial position
    {start_position}
  )

  (:goal
    {goal_position}
  )
)
"""
    return pddl.strip()


# Input maze as a list of strings
maze_input = [
    ".......",
    ".......",
    ".......",
    ".......",
    ".......",
    ".......",
    "......."
  ]

# Define start and goal positions as (x, y)
start_position = (6, 6)  # Top-left corner
goal_position = (0, 0)  # Bottom-right corner

# Generate PDDL
pddl_output = generate_pddl_from_maze(maze_input, start_position, goal_position)

# Save to file
with open("B.pddl", "w") as file:
    file.write(pddl_output)

print("PDDL problem file generated: maze_problem.pddl")
