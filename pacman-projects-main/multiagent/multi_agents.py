# multi_agents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattan_distance
from game import Directions, Actions
from pacman import GhostRules
import random, util
from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """
    def get_action(self, game_state):
        """
        You do not need to change this method, but you're welcome to.

        get_action chooses among the best options according to the evaluation function.

        Just like in the previous project, get_action takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legal_moves = game_state.get_legal_actions()

        # Choose one of the best actions
        scores = [self.evaluation_function(game_state, action) for action in legal_moves]
        best_score = max(scores)
        best_indices = [index for index in range(len(scores)) if scores[index] == best_score]
        chosen_index = random.choice(best_indices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legal_moves[chosen_index]

    def evaluation_function(self, current_game_state, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (new_food) and Pacman position after moving (new_pos).
        new_scared_times holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successor_game_state = current_game_state.generate_pacman_successor(action)
        new_pos = successor_game_state.get_pacman_position()
        new_food = successor_game_state.get_food()
        new_ghost_states = successor_game_state.get_ghost_states()
        new_ghost_positions = successor_game_state.get_ghost_positions()
        new_scared_times = [ghostState.scared_timer for ghostState in new_ghost_states]
        "*** YOUR CODE HERE ***"

        # FOOD DISTANCE EVALUATION
        # Convert the food grid to a list of food positions
        food_list = new_food.as_list()    
        if food_list: # Check if there is any food in the list
            distances = []
            for food in food_list:
                distance = manhattan_distance(new_pos, food)
                distances.append(distance)
            min_food_distance = min(distances)  # Find the minimum distance in the list of distances
        else:
            min_food_distance = 1 # If there is no food, set the distance to 1
                
    
        # Create a list to store distance to ghosts
        ghost_distances = []

        for ghost in new_ghost_states:
            ghost_position = ghost.get_position()            
            distance = manhattan_distance(new_pos, ghost_position)
            ghost_distances.append(distance)

        
        #Separate between active and scared
        
            scared_ghosts = []
            active_ghosts = []

        # Loop through each ghost's scared time and distance
        for i, time in enumerate(new_scared_times):
            # Check if the ghost is scared (scared time > 0)
            if time > 0:
                scared_ghosts.append(ghost_distances[i])

            if time == 0:
                active_ghosts.append(ghost_distances[i])

        
        #Penalty for active ghosts
        active_ghosts_penalty = 0
        if active_ghosts:
            min_active_ghost_distance = min(active_ghosts)
            active_ghosts_penalty = -100/(min_active_ghost_distance + 1)
        # Reward Pacman for chasing scared ghosts
        scared_ghost_reward = 0
        if scared_ghosts:
            min_scared_ghost_distance = min(scared_ghosts)
            scared_ghost_reward = 200 / (min_scared_ghost_distance + 1)  # Reward for approaching scared ghosts

        score =  successor_game_state.get_score() \
                 + (10 / min_food_distance) \
                    - len(food_list) * 100  \
                    + active_ghosts_penalty \
                    + scared_ghost_reward
        
        return score

def score_evaluation_function(current_game_state):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return current_game_state.get_score()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, eval_fn='score_evaluation_function', depth='2'):
        super().__init__()
        self.index = 0
        self.evaluation_function = util.lookup(eval_fn, globals())
        self.depth = int(depth) 

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def get_action(self, game_state):
        """
        Returns the minimax action from the current game_state using self.depth
        and self.evaluation_function.

        Here are some method calls that might be useful when implementing minimax.

        game_state.get_legal_actions(agent_index):
        Returns a list of legal actions for an agent
        agent_index=0 means Pacman, ghosts are >= 1

        game_state.generate_successor(agent_index, action):
        Returns the successor game state after an agent takes an action

        game_state.get_num_agents():
        Returns the total number of agents in the game

        game_state.is_win():
        Returns whether or not the game state is a winning state

        game_state.is_lose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        
        best_score = float('-inf')  # Initialize best score to negative infinity
        best_action = None  # Initialize best action as None

        legal_actions = game_state.get_legal_actions(0) # Get list of legal actions for Pacman (agent index 0)
        
        for action in legal_actions: # Iterate over all legal actions to find the best one
            successor_state = game_state.generate_successor(0, action) # Generate the successor state after Pacman takes the action
            
            current_score = self.minimax(successor_state, 0, 1) # Call the minimax function for the next agent (first ghost) at depth 0

            if current_score > best_score: # Update best score and action if a better score is found
                best_score = current_score
                best_action = action

        # Return the action with the highest minimax value
        return best_action
    
    """ This is the minimax function what will be used for the max and min turns """
    def minimax(self, game_state, depth, agent_index):
        # When we reach maximum depth or we won or lose via the game state, end game by returning the eval function of the current game state
        if depth == self.depth or game_state.is_win() or game_state.is_lose():
            return self.evaluation_function(game_state)

        if agent_index == 0: # Pacman agent turn (maximizing player)
            return self.max_value(game_state, depth, agent_index)
        
        else: # Ghost agent turn (minimizing players)
            return self.min_value(game_state, depth, agent_index)
    
    """ This is the max player (Pacman) minimax function, returns the max value of a given game state that goes to a specified depth """
    def max_value(self, game_state, depth, agent_index):
        
        max_value = float('-inf')  # Initialize value to negative infinity
        pacman_legal_actions = game_state.get_legal_actions(agent_index) # Get all  legal actions for Pacman

        if not pacman_legal_actions:

            return self.evaluation_function(game_state) # If there are no legal actions, we return the evaluation of the current sate

        for action in pacman_legal_actions:
            successor_state = game_state.generate_successor(agent_index, action) # Generate successor state
            
            next_agent_id = agent_index + 1 # Next agent index (ghosts)
            score = self.minimax(successor_state, depth, next_agent_id % game_state.get_num_agents()) # recursively execute minimax for the next agent
            max_value = max(max_value, score) # Udpate the value with the maximum score

        return max_value
    
    """ This is the min player (Ghosts) turn function, returns the max value of a given game state that goes to a specified depth """
    def min_value(self, game_state, depth, agent_index):
        min_value = float('inf')  # Initialize value to positive infinity
        legal_actions = game_state.get_legal_actions(agent_index) # Get legal actions for the ghost agent

        if not legal_actions:
            return self.evaluation_function(game_state)# return the evaluation of the current state

        for action in legal_actions:
            successor_state = game_state.generate_successor(agent_index, action) #Generate successor state

            next_agent = agent_index + 1 #change agnet id 
            num_agents = game_state.get_num_agents()

            if next_agent % num_agents == 0: # when modulus is 0, means all agents have been visited, thus going to a deeper level and starting again with agent 0
                score = self.minimax(successor_state, depth+1, 0) # Increase depth, it's Pacmans turn again
            else:
                score = self.minimax(successor_state, depth, next_agent%num_agents) # Continue to next ghost
            min_value = min(min_value, score) # Update the value with the minimum score

        return min_value

        
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your alphabeta agent with alpha-beta pruning (question 3)
    """

    def get_action(self, game_state):
        """
        Returns the alphabeta action using self.depth and self.evaluation_function
        """
        "*** YOUR CODE HERE ***"
        #Initializations
        alpha = float('-inf')
        beta = float('inf')
        best_value = float('-inf')  
        best_action = None  

        legal_actions = game_state.get_legal_actions(0) # Get the list of legal actions for Pacman (agent index 0)
        
        for action in legal_actions: # Iterate over allthe legal actions to find the best one
            successor_state = game_state.generate_successor(0,action) # generate the successor state after Pacman takes the action
            
            #This is the first call of alphabeta, so we are at a max turn, calling a min turn
            value = self.alphabeta(successor_state, 0, 1,alpha, beta )

            if value > best_value: #Update best score and action if a better score is found
                best_value = value
                best_action = action #We save the best action of alpha beta

            alpha = max(alpha, best_value) #Update alpha

        #Return the action with the highest alphabeta value
        return best_action
    
    """ This is the alphabeta function what will be used for the max and min turns """
    def alphabeta(self, game_state, depth, agent_index, alpha, beta):
        # Check if we have reached the maximum depth or we won or lose via the game state
        if depth == self.depth or game_state.is_win() or game_state.is_lose():
            return self.evaluation_function(game_state)

        if agent_index == 0: # Pacman agent turn (maximizing player)
            return self.max_value(game_state, depth, agent_index,alpha,beta)
        else: # Ghost agent turn (minimizing players)
            return self.min_value(game_state, depth, agent_index,alpha,beta)
    
    """ This is the max player (Pacman) alphabeta function, returns the max value of a given game state that goes to a specified depth """
    def max_value(self, game_state, depth, agent_index, alpha, beta):
        max_value = float('-inf')  #Initialize value to negative infinity

        pacman_legal_actions = game_state.get_legal_actions(agent_index) # Get legal actions for Pacman

        if not pacman_legal_actions:
            return self.evaluation_function(game_state) # iff no legal actions, return the evaluation of the current state

        for action in pacman_legal_actions:
            successor_state = game_state.generate_successor(agent_index, action) #generate successor state
            
            next_agent = agent_index + 1 # Next agent index (ghosts)
            
            value = self.alphabeta(successor_state, depth, next_agent,alpha,beta) #Recursively call alphabeta for the next agent, returns a value for that branc
            
            max_value = max(value, max_value) #update max

            if max_value > beta: #Prunning
                return max_value # We return before the for cicle is over, then we are not exploring all the legal acctions of PacMan
            alpha = max(alpha,max_value) #update Alpha
            
        return max_value
    
    """ This is the min player (Ghosts) turn function, returns the max value of a given game state that goes to a specified depth """
    def min_value(self, game_state, depth, agent_index,alpha,beta):
        min_value = float('inf')  # Initialize value to positive infinity

        legal_actions = game_state.get_legal_actions(agent_index) # Get legal actions for the ghost agent

        if not legal_actions:
            # Return the evaluation of the current state
            return self.evaluation_function(game_state)

        for action in legal_actions:
            successor_state = game_state.generate_successor(agent_index, action) # Generate successor state
            next_agent = agent_index + 1 
            num_agents = game_state.get_num_agents()

            if next_agent % num_agents == 0: #It loop arround the ghosts, its pacman turn again
                value = self.alphabeta(successor_state, depth + 1, 0,alpha,beta) # Increase depth, it's Pacmans turn again
            else:
                value = self.alphabeta(successor_state, depth, next_agent,alpha,beta) # Continue to next ghost

            min_value = min(value, min_value)
            if min_value < alpha: #Pruning
                return min_value  #We return before the for cicle is over, then we are not exploring all the legal acctions of the ghost
            beta = min(beta,min_value) #update beta
                
        return min_value # return the value 




class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def get_action(self, game_state):
        """
        Returns the expectimax action using self.depth and self.evaluation_function

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raise_not_defined()

def better_evaluation_function(current_game_state):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raise_not_defined()
    


# Abbreviation
better = better_evaluation_function
