# my_team.py
# ---------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import random
import contest.util as util

from contest.capture_agents import CaptureAgent
from contest.game import Directions
from contest.util import nearest_point


#################
# Team creation #
#################

def create_team(first_index, second_index, is_red,
                first='OffensiveAStarAgent', second='DefensiveReflexAgent', num_training=0):
    """
    This function should return a list of two agents that will form the
    team, initialized using firstIndex and secondIndex as their agent
    index numbers.  isRed is True if the red team is being created, and
    will be False if the blue team is being created.

    As a potentially helpful development aid, this function can take
    additional string-valued keyword arguments ("first" and "second" are
    such arguments in the case of this function), which will come from
    the --red_opts and --blue_opts command-line arguments to capture.py.
    For the nightly contest, however, your team will be created without
    any extra arguments, so you should make sure that the default
    behavior is what you want for the nightly contest.
    """
    return [eval(first)(first_index), eval(second)(second_index)]



#############
# My Agents #
#############

class OffensiveAStarAgent(CaptureAgent):
    """
        Uses A Star to look for the food.
    """

    def __init__(self, index, time_for_computing=.1):
        super().__init__(index, time_for_computing)
        self.start = None

    def register_initial_state(self, game_state):
        self.start = game_state.get_agent_position(self.index)
        CaptureAgent.register_initial_state(self, game_state)

    def a_star_search(self,initial_game_state, start, goal):
        """Search the node that has the lowest combined cost and heuristic first."""

        expanded_nodes = set()  # Expanded nodes initialized as an empty set
        frontier = util.PriorityQueue()  # Frontier as a PriorityQueue
        frontier.push((initial_game_state,start, []), 0)  # Frontier initialized with the initial state
        cost_so_far = {start: 0}  # Dictionary to track the minimum cost to reach each state

        while not frontier.is_empty():            
            # print("Enter While")
            current_game_state, current_pos, path = frontier.pop() # Pop the node with the lowest path cost
            # print("Current Path", path)
            # Goal test after popping the node
            if current_pos == goal:  
                # print("SOLVED RETURN:", path)
                # return []
                return path  # Return the solution path if goal is found

            if current_pos in expanded_nodes:
                continue  # Skip already expanded nodes
            else: 
                expanded_nodes.add(current_pos) # Mark node as expanded

            # Expand neighbors, looking at actions
            for action in current_game_state.get_legal_actions(self.index):
                # print("Current Action: ", action)
                # Ignore STOP action
                if action == Directions.STOP:
                    continue
                 # Get successor state and position
                successor = current_game_state.generate_successor(self.index, action) #Returns the successor state (a GameState object) after the specified agent takes the action.
                next_pos = successor.get_agent_state(self.index).get_position() #Returns the position of agent after taken the current action
                next_pos = nearest_point(next_pos)
                # print("Next position", next_pos)
                # print("Nearest", nearest_point(next_pos))
                # print(next_pos != nearest_point(next_pos))
                # print("cost_so_far:", cost_so_far)
                
                
                # Skip invalid positions or half-grid positions
                # if next_pos not in cost_so_far or next_pos != nearest_point(next_pos):
                    # continue

                # Compute costs
                new_cost = cost_so_far[current_pos] + 1  # Cost to move is constant
                # print("New Cost: ", new_cost)
                # print("cost_so_far[next_pos]:", cost_so_far[next_pos])
                # If next_pos has not been expanded, or if a cheaper path to it is found
                if next_pos not in expanded_nodes or new_cost < cost_so_far[next_pos]:

                    # print("Enter the void")
                    cost_so_far[next_pos] = new_cost
                    new_path = path + [action]

                    # Priority is based on f(n) = g(n) + h(n)
                    h = self.get_maze_distance(next_pos, goal)  # Heuristic (Manhattan distance)
                    f = new_cost + h   
                    # print("New Path: ", new_path) 
                    frontier.push((successor,next_pos, new_path), f)

    
    def choose_action(self, game_state):
        """
        Choose an action using A* to navigate to the nearest food.
        """
        my_pos = game_state.get_agent_state(self.index).get_position()
        food_list = self.get_food(game_state).as_list()
        # If there is no food left, stop
        if not food_list:
            return Directions.STOP
        
        goal = min(food_list, key=lambda food: self.get_maze_distance(my_pos, food))
        path = self.a_star_search(game_state, my_pos, goal)
 
        # Return the first step of the path, if it exists
        if path and len(path) > 0:
            # print("First step of path", path)
            return path[0]
        else:
            return Directions.STOP

##########
# Agents #
##########

class ReflexCaptureAgent(CaptureAgent):
    """
    A base class for reflex agents that choose score-maximizing actions
    """

    def __init__(self, index, time_for_computing=.1):
        super().__init__(index, time_for_computing)
        self.start = None

    def register_initial_state(self, game_state):
        self.start = game_state.get_agent_position(self.index)
        CaptureAgent.register_initial_state(self, game_state)

    def choose_action(self, game_state):
        """
        Picks among the actions with the highest Q(s,a).
        """
        actions = game_state.get_legal_actions(self.index)

        # You can profile your evaluation time by uncommenting these lines
        # start = time.time()
        values = [self.evaluate(game_state, a) for a in actions]
        # print 'eval time for agent %d: %.4f' % (self.index, time.time() - start)

        max_value = max(values)
        best_actions = [a for a, v in zip(actions, values) if v == max_value]

        food_left = len(self.get_food(game_state).as_list())

        if food_left <= 2:
            best_dist = 9999
            best_action = None
            for action in actions:
                successor = self.get_successor(game_state, action)
                pos2 = successor.get_agent_position(self.index)
                dist = self.get_maze_distance(self.start, pos2)
                if dist < best_dist:
                    best_action = action
                    best_dist = dist
            return best_action

        return random.choice(best_actions)

    def get_successor(self, game_state, action):
        """
        Finds the next successor which is a grid position (location tuple).
        """
        successor = game_state.generate_successor(self.index, action)
        pos = successor.get_agent_state(self.index).get_position()
        if pos != nearest_point(pos):
            # Only half a grid position was covered
            return successor.generate_successor(self.index, action)
        else:
            return successor

    def evaluate(self, game_state, action):
        """
        Computes a linear combination of features and feature weights
        """
        features = self.get_features(game_state, action)
        weights = self.get_weights(game_state, action)
        return features * weights

    def get_features(self, game_state, action):
        """
        Returns a counter of features for the state
        """
        features = util.Counter()
        successor = self.get_successor(game_state, action)
        features['successor_score'] = self.get_score(successor)
        return features

    def get_weights(self, game_state, action):
        """
        Normally, weights do not depend on the game state.  They can be either
        a counter or a dictionary.
        """
        return {'successor_score': 1.0}


class OffensiveReflexAgent(ReflexCaptureAgent):
    """
  A reflex agent that seeks food. This is an agent
  we give you to get an idea of what an offensive agent might look like,
  but it is by no means the best or only way to build an offensive agent.
  """

    def get_features(self, game_state, action):
        features = util.Counter()
        successor = self.get_successor(game_state, action)
        food_list = self.get_food(successor).as_list()
        features['successor_score'] = -len(food_list)  # self.getScore(successor)

        # Compute distance to the nearest food

        if len(food_list) > 0:  # This should always be True,  but better safe than sorry
            my_pos = successor.get_agent_state(self.index).get_position()
            min_distance = min([self.get_maze_distance(my_pos, food) for food in food_list])
            features['distance_to_food'] = min_distance
        return features

    def get_weights(self, game_state, action):
        return {'successor_score': 100, 'distance_to_food': -1}


class DefensiveReflexAgent(ReflexCaptureAgent):
    """
    A reflex agent that keeps its side Pacman-free. Again,
    this is to give you an idea of what a defensive agent
    could be like.  It is not the best or only way to make
    such an agent.
    """

    def get_features(self, game_state, action):
        features = util.Counter()
        successor = self.get_successor(game_state, action)

        my_state = successor.get_agent_state(self.index)
        my_pos = my_state.get_position()

        # Computes whether we're on defense (1) or offense (0)
        features['on_defense'] = 1
        if my_state.is_pacman: features['on_defense'] = 0

        # Computes distance to invaders we can see
        enemies = [successor.get_agent_state(i) for i in self.get_opponents(successor)]
        invaders = [a for a in enemies if a.is_pacman and a.get_position() is not None]
        features['num_invaders'] = len(invaders)
        if len(invaders) > 0:
            dists = [self.get_maze_distance(my_pos, a.get_position()) for a in invaders]
            features['invader_distance'] = min(dists)

        if action == Directions.STOP: features['stop'] = 1
        rev = Directions.REVERSE[game_state.get_agent_state(self.index).configuration.direction]
        if action == rev: features['reverse'] = 1

        return features

    def get_weights(self, game_state, action):
        return {'num_invaders': -1000, 'on_defense': 100, 'invader_distance': -10, 'stop': -100, 'reverse': -2}


