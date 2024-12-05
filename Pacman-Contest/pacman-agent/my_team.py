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
from contest.distance_calculator import Distancer


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

    def check_scared_ghosts(self, game_state):
        """
        Check if any enemy ghost is scared and return a list of scared ghosts positions with their scared timer.
        """
        opponents = self.get_opponents(game_state)
        my_pos = game_state.get_agent_state(self.index).get_position()
        scared_ghosts = []

        for opponent_index in opponents:
            enemy_state = game_state.get_agent_state(opponent_index)
            if not enemy_state.is_pacman:  # Ensure it's a ghost
                if enemy_state.scared_timer > 0:  # Check if scared
                    scared_ghosts.append((opponent_index, enemy_state.get_position(), enemy_state.scared_timer))
        
        # Filter out ghosts that are not visible (position is None)
        visible_ghosts = [(index, pos, timer) for index, pos, timer in scared_ghosts if pos is not None]

        if not visible_ghosts:
            return None  # No visible ghosts to consider

        # Find the closest ghost based on maze distance
        closest_ghost = min(
            visible_ghosts,
            key=lambda ghost: self.get_maze_distance(my_pos, ghost[1])  # Distance to the ghost's position
            )
        return closest_ghost

    def enemy_distance(self,game_state):
        distancer = Distancer(game_state.data.layout)
        my_position = game_state.get_agent_state(self.index).get_position()
        opponents = self.get_opponents(game_state)
        
        distance = []
        for index in opponents:
            enemy_position = game_state.get_agent_position(index)
            if enemy_position == None:
                distance.append(100)
            else:
                distance.append(distancer.get_distance(enemy_position, my_position ))
        # print("Distance",distance)
        return(min(distance))   
    
    def enemy_position(self,game_state):
        enemy_position = []
        opponents = self.get_opponents(game_state)
        
        for index in opponents:
            enemy_position.append(game_state.get_agent_position(index))

        # print(enemy_position)
        return(enemy_position)   
        
    def choose_action(self, game_state):
            """
            Choose Offensive action using A* to navigate to the nearest food.
            """
            my_pos = game_state.get_agent_state(self.index).get_position()
            pacman_state = game_state.get_agent_state(self.index).is_pacman
            e_dist = self.enemy_distance(game_state)
            food_list = self.get_food(game_state).as_list()
            closest_ghost = self.check_scared_ghosts(game_state) # Check if ghost are scared
            goal = min(food_list, key=lambda food: self.get_maze_distance(my_pos, food)) #Nearest Food

            if pacman_state: # If we are Pacman MODE
                heuristic = 10/self.enemy_distance(game_state)
                if not food_list: # If we are done eating we go back to base.
                     goal = game_state.get_initial_agent_position(self.index)          
                
                elif closest_ghost:
                    goal = closest_ghost[1]

                
                elif e_dist < 4 : # If we are being chased or we are done eating we go back to the base
                    capsules = self.get_capsules(game_state)
                    print(capsules)
                    if len(capsules)>0:
                        # goal = min(capsules, key=lambda cap: self.get_maze_distance(my_pos, cap)) #Neares Capsule
                        goal = capsules
            
                else:
                    # print("Offensive mode on")
                    goal = min(food_list, key=lambda food: self.get_maze_distance(my_pos, food)) #Nearest Food
            
            else: #Ghost mode
                goal = min(food_list, key=lambda food: self.get_maze_distance(my_pos, food)) # Nearest Food
                heuristic = self.enemy_distance(game_state)


            # print("GOAL:",goal )
            path = self.a_star_search(game_state, my_pos, goal, heuristic)

            # Return the first step of the path, if it exists
            if path and len(path) > 0:
                # print("First step of path", path)
                return path[0]
            else:
                #If something weird is happening jus go home
                goal = game_state.get_initial_agent_position(self.index)
                path = self.a_star_search(game_state, my_pos, goal, heuristic)
                
                return path[0]



    def a_star_search(self,initial_game_state, start, goal, heuristic):
        """Search the node that has the lowest combined cost and heuristic first."""

        expanded_nodes = set()  # Expanded nodes initialized as an empty set
        frontier = util.PriorityQueue()  # Frontier as a PriorityQueue
        frontier.push((initial_game_state,start, []), 0)  # Frontier initialized with the initial state
        cost_so_far = {start: 0}  # Dictionary to track the minimum cost to reach each state

        while not frontier.is_empty():            
            current_game_state, current_pos, path = frontier.pop() # Pop the node with the lowest path cost
            # Goal test after popping the node
            if current_pos == goal:  
                return path  # Return the solution path if goal is found

            if current_pos in expanded_nodes:
                continue  # Skip already expanded nodes
            else: 
                expanded_nodes.add(current_pos) # Mark node as expanded

            # Expand neighbors, looking at actions
            for action in current_game_state.get_legal_actions(self.index):
                # Ignore STOP action
                if action == Directions.STOP:
                    continue
                 # Get successor state and position
                successor = current_game_state.generate_successor(self.index, action) #Returns the successor state (a GameState object) after the specified agent takes the action.
                next_pos = successor.get_agent_state(self.index).get_position() #Returns the position of agent after taken the current action
                next_pos = nearest_point(next_pos)

                # Compute costs
                new_cost = cost_so_far[current_pos] + 1  # Cost to move is constant
                # If next_pos has not been expanded, or if a cheaper path to it is found
                if next_pos not in expanded_nodes or new_cost < cost_so_far[next_pos]:
                    cost_so_far[next_pos] = new_cost
                    new_path = path + [action]

                    # Priority is based on f(n) = g(n) + h(n)
                    h = self.get_maze_distance(next_pos, goal)  # Heuristic (Manhattan distance)
                    # d = self.enemy_distance(successor)
                    # if d == 0 : d =1
                    # f = new_cost + h + 100/d
                    f = new_cost + h + heuristic
                    # print("New Path: ", new_path) 
                    frontier.push((successor,next_pos, new_path), f)
                    

    
   
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


