# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# # Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in search_agents.py).
"""
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in obj-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem.
        """
        util.raise_not_defined()

    def is_goal_state(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raise_not_defined()

    def get_successors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raise_not_defined()

    def get_cost_of_actions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raise_not_defined()


def tiny_maze_search(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# def addSuccessors(problem, addCost=True):

class SearchNode:
    def __init__(self, parent, node_info):
        """
            parent: parent SearchNode.

            node_info: tuple with three elements => (coord, action, cost)

            coord: (x,y) coordinates of the node position

            action: Direction of movement required to reach node from
            parent node. Possible values are defined by class Directions from
            game.py

            cost: cost of reaching this node from the starting node.
        """

        self.__state = node_info[0]
        self.action = node_info[1]
        self.cost = node_info[2] if parent is None else node_info[2] + parent.cost
        self.parent = parent

    # The coordinates of a node cannot be modified, se we just define a getter.
    # This allows the class to be hashable.
    @property
    def state(self):
        return self.__state

    def get_path(self):
        path = []
        current_node = self
        while current_node.parent is not None:
            path.append(current_node.action)
            current_node = current_node.parent
        path.reverse()
        return path
    
    # Consider 2 nodes to be equal if their coordinates are equal (regardless of everything else)
    # def __eq__(self, __o: obj) -> bool:
    #     if (type(__o) is SearchNode):
    #         return self.__state == __o.__state
    #     return False

    # # def __hash__(self) -> int:
    # #     return hash(self.__state)

def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.get_start_state()) (9, 1)
    print("Is the start a goal?", problem.is_goal_state(problem.get_start_state())) False
    print("Start's successors:", problem.get_successors(problem.get_start_state())) [((10, 1), 'East', 1), ((8, 1), 'West', 1)]
    """
    "*** YOUR CODE HERE ***"
    
    # Stack for DFS: list that stores tuples of (state, path)
    # path = list of state elements
    # state = coordinates of a state

    stack = util.Stack() # LIFO from util
    visited = set() # We don't care about the order here

    start_state = (problem.get_start_state())
    stack.push((start_state, [], 1))  # Path is initially empty

    while stack:
        # Get the values from state tuple
        state, path, cost = stack.pop()

        if problem.is_goal_state(state):
            print("Goal state found:", state)
            print("Path found:", new_path)
            print("Stack length:", len(stack.list))
            return path  # Found the goal; return the path of actions

        if state not in visited:
            visited.add(state)

            for successor, action, cost in problem.get_successors(state):
                if successor not in visited:
                    new_path = path + [action]
                    stack.push((successor, new_path, cost))

    return [] 



def breadth_first_search(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #stack = []
    queue = util.Queue()
    visited = set() # We don't care about the order here

    start_state = (problem.get_start_state())
    queue.push((start_state, [], 1))  # Path is initially empty

    while queue:
        # Get the values from state tuple
        state, path, cost = queue.pop()

        if problem.is_goal_state(state):
            print("Goal state found:", state)
            print("Path found:", new_path)
            print("Queue length:", len(queue.list))
            return path  # Found the goal; return the path of actions

        if state not in visited:
            visited.add(state)

            for successor, action, cost in problem.get_successors(state):
                if successor not in visited:
                    # Append the new action to the existing path
                    new_path = path + [action]
                    queue.push((successor, new_path, cost))

    return [] 

    util.raise_not_defined()

def uniform_cost_search(problem):
    # Initialize the priority queue and visited set
    frontier = util.PriorityQueue()
    visited = set()

    # Start state
    start_state = problem.get_start_state()
    frontier.push((start_state, []), 0)  # (state, path), priority

    # A dictionary to keep track of the best cost to reach a state
    state_costs = {start_state: 0}

    while not frontier.is_empty():
        (state, path) = frontier.pop()

        if problem.is_goal_state(state):
            print("Path:", path)
            # print("State_costs:", state_costs[0])
            return path  # Return the sequence of actions

        if state in visited:
            continue

        visited.add(state)

        for successor, action, step_cost in problem.get_successors(state): #  [((10, 1), 'East', 1), ((8, 1), 'West', 1)]
            new_path = path + [action] # ['South', 'South', 'West'] + 'East'
            new_cost = state_costs[state] + step_cost

            # If the successor has not been visited or a better cost is found
            if (successor not in state_costs) or (new_cost < state_costs[successor]):
                state_costs[successor] = new_cost
                frontier.update((successor, new_path), new_cost)
        
        
    return []
 
    util.raise_not_defined()

def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def a_star_search(problem, heuristic=null_heuristic):
    # Initialize the priority queue (frontier) and other data structures
    frontier = util.PriorityQueue()
    explored = set()

    start_state = problem.get_start_state()
    start_node = (start_state, [], 0)  # (state, path, g(n))

    # Calculate the initial f(n) = g(n) + h(n)
    start_h = heuristic(start_state, problem)
    start_f = start_h + start_node[2] # Since g(n) = 0 at the start state, only 
    frontier.push(start_node, start_f)

    # Dictionary to keep track of the lowest g(n) cost to reach each state
    state_costs = {start_state: 0}

    # Main loop
    while not frontier.is_empty():
        # Pop the node with the lowest f(n) value
        current_state, current_path, current_g = frontier.pop()

        # Goal state check
        if problem.is_goal_state(current_state):
            return current_path  # Return the sequence of actions to reach the goal

        # Skip already explored states
        if current_state in explored:
            continue

        # Mark the state as explored
        explored.add(current_state)

        # Expand the current node
        for successor, action, step_cost in problem.get_successors(current_state):
            # Calculate g(n) for the successor
            new_g = current_g + step_cost
            new_path = current_path + [action]

            # Calculate h(n) and f(n)
            h = heuristic(successor, problem)
            f = new_g + h

            # If the successor has not been seen or offers a better path
            if (successor not in state_costs) or (new_g < state_costs[successor]):
                state_costs[successor] = new_g
                frontier.push((successor, new_path, new_g), f)

    # If the frontier is empty and the goal was not found
    return []
    util.raise_not_defined()

# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
