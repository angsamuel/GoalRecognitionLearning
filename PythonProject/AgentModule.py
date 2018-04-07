import numpy as np
import pylab as plt
import networkx as nx
import random

class Agent:
    def __init__(self, name, isSneaky, gameScenario):
      self.name = name
      self.sneaky = isSneaky
      self.gs = gameScenario
      self.state = self.gs.startState
      self.visited_states = []

    def generateQTables(self, tableSize, newGamma, targets):
      self.q_table_dict = dict()
      self.path_dict = dict()
      self.gamma = newGamma
      for target in targets:
        q_table = np.matrix(np.ones(shape=(self.gs.nodesNum, self.gs.nodesNum)))
        q_table *= 0
        for edge in self.gs.edges:
          if edge[1] == target:
            q_table[edge] = 0
          else:
            q_table[edge] = 0
          if edge[0] == target:
            q_table[edge[::-1]] = 0
          else:
            q_table[edge[::-1]] = 0
        self.q_table_dict.update({target: q_table})


    def move(self, target):
      q_table = self.q_table_dict[target]
      next_step_index = np.where(q_table[self.state,] == np.max(q_table[self.state,]))[1]
      if next_step_index.shape[0] > 1:
        next_step_index = int(np.random.choice(next_step_index, size = 1))
      else:
        next_step_index = int(next_step_index)
      self.state = next_step_index

    def update(self, current_state, action, target):
      max_index = np.where(self.q_table_dict[target][action,] == np.max(self.q_table_dict[target][action,]))[1]
      if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size = 1))
      else:
        max_index = int(max_index)
      max_value = self.q_table_dict[target][action, max_index] #max value of next possible move
      
      self.q_table_dict[target][current_state, action] = self.R[current_state, action] + (self.gamma * max_value)
      self.q_table_dict[target][current_state, action] -= (self.G[target][current_state, action])
      
      if self.q_table_dict[target][current_state, action] < 0:
        self.q_table_dict[target][current_state, action] = 0

      if (np.max(self.q_table_dict[target]) > 0):
        #return(np.sum(self.q_table_dict[target]/(self.gs.targetUtility * 100) ) ) #/(np.max(self.q_table_dict[target])))   )
        return(np.sum(self.q_table_dict[target]) / (self.gs.targetUtility * len(self.gs.edges)))
      else:
        return (0)

    def get_score(self, target):
      if (np.max(self.q_table_dict[target]) > 0):
        return(np.sum(self.q_table_dict[target])/(self.gs.targetUtility * len(self.gs.edges)) )  #/(np.max(self.q_table_dict[target])))   )
      else:
        return (0)

    def get_possible_actions(self, state):
      current_state_row = self.R[state,]
      possible_actions = np.where(current_state_row >= 0)[1]

      return possible_actions

    #pass possible actions
    def preview_next_action(self, available_act):
      next_action = int(np.random.choice(available_act,1))
      return next_action

    def refresh_R_table(self, target, utility):
      self.R = np.matrix(np.ones(shape=(self.gs.nodesNum, self.gs.nodesNum)))
      self.R *= -1
      if utility < 0:
        utility = 0
      for edge in self.gs.edges:
        if edge[1] == target:
          self.R[edge] = utility
        else:
          self.R[edge] = 0
        if edge[0] == target:
          self.R[edge[::-1]] = utility
        else:
          self.R[edge[::-1]] = 0
        #print(t, self.R_allowed[t])

    def get_best_path(self, target):
      return self.path_dict[target]

    def reset_guess_table(self):
      self.G =  dict()
      for t in self.gs.targets:
        self.G.update({t: np.matrix(np.ones(shape=(self.gs.nodesNum, self.gs.nodesNum)))})

    def apply_guess_penalty(self, current_state, action, target):
      #self.G[target][current_state, action] = self.gs.guessReward
      self.q_table_dict[target][current_state, action] -= 1
      #if self.q_table_dict[target][current_state, action] < 0:
      #  self.q_table_dict[target][current_state, action] = 0


    def gimme_move(self, q_table, prev_state, current_state):
      moves = []
      move_max_value = -1000000
      for m in range(self.gs.nodesNum):
        if m != prev_state and m!= current_state and self.R[current_state, m] >= 0:
          moves.append(m)
          if move_max_value < q_table[current_state,m]:
            move_max_value = q_table[current_state,m]
      

      chosen_moves = []
      for m in moves:
        if q_table[current_state,m] >= move_max_value:
          chosen_moves.append(m)

      if(len(chosen_moves) < 1):
        print(prev_state, current_state)

      random_index = np.random.randint(0, len(chosen_moves))
      return chosen_moves[random_index]


    def train_agent(self, episodes):
      self.generateQTables(self.gs.nodesNum, .8, self.gs.targets)
      self.reset_guess_table()
      for target in self.gs.targets:
        self.refresh_R_table(target,self.gs.targetUtility)

        possible_action = self.get_possible_actions(self.gs.startState)
        action = self.preview_next_action(possible_action)

        self.update(self.gs.startState, action, target)
        scores = []
        #place agent in a random location, make a move, record results
        for i in range(episodes):
          current_state = np.random.randint(0, int(self.q_table_dict[target].shape[0]))
          possible_action = self.get_possible_actions(current_state)
         # print(current_state, possible_action)
          action = self.preview_next_action(possible_action)
          score = self.update(current_state,action, target)
          scores.append(score)

        # Testing
        current_state = self.gs.startState
        prev_state = current_state
        steps = [current_state]
        q_table = self.q_table_dict[target]
        while current_state != target:

            next_step_index = self.gimme_move(q_table, prev_state, current_state)
            steps.append(next_step_index)
            prev_state = current_state
            current_state = next_step_index
        print "\n"
        print("Agent Summary For Target: " + str(target) )
        print("Most efficient path:")
        print(steps)
        self.path_dict.update({target: steps})
        plt.plot(scores)
        plt.show()
      return self



    def train_agent_against_observer(self, episodes, observer):
      #self.generateQTables(self.gs.nodesNum, .8, self.gs.targets)
      self.scores_dict = dict()
      self.reset_guess_table()
      for t in self.gs.targets:
        self.scores_dict.update({t: []})

      for i in range(0, episodes):
        observer.reset_belief()


        target = self.gs.targets[np.random.randint(len(self.gs.targets))]
        self.refresh_R_table(target, self.gs.targetUtility)

        current_state = self.gs.startState
        prev_state = current_state
        steps = [current_state]
        q_table = self.q_table_dict[target]
        while current_state != target:
          next_step_index = self.gimme_move(q_table, prev_state, current_state)

          #self.update(current_state,next_step_index,target)
          steps.append(next_step_index)
          
          
          
          #observer work
          observer.update_belief(current_state)
          observer_guess = observer.belief_guess()

          score = self.update(current_state,next_step_index, target)
          if observer_guess == target and current_state != self.gs.startState:
              self.apply_guess_penalty(prev_state, current_state, target)

          self.scores_dict[target].append(score)

          observer.observe_action(current_state, target)
          prev_state = current_state
          current_state = next_step_index

      #
      #for target in self.gs.targets:
      #  plt.plot(self.scores_dict[target])
      #  plt.show()

      #testing
      for target in self.gs.targets:
        # Testing
        observer.reset_belief()
        agent_points = self.gs.targetUtility
        current_state = self.gs.startState
        prev_state = current_state

        steps = [current_state]
        q_table = self.q_table_dict[target]

        while current_state != target:
            #print(current_state)
            #print(target)
            next_step_index = self.gimme_move(q_table, prev_state, current_state)
            steps.append(next_step_index)

            #observer work
            observer.update_belief(current_state)
            observer_guess = observer.belief_guess()

            score = self.update(current_state,next_step_index, target)
            if observer_guess == target and current_state != self.gs.startState:
              self.apply_guess_penalty(prev_state, current_state, target)
              agent_points -= self.gs.guessReward

            observer.observe_action(current_state, target)
            prev_state = current_state
            current_state = next_step_index
        print "\n"
        print("Agent Summary (vs Belief Update) For Target: " + str(target))
        print("Most efficient path:")
        print(steps)
        print("agent score", agent_points)
        print("observer score", self.gs.targetUtility - agent_points)
        self.path_dict.update({target: steps})
        plt.plot(self.scores_dict[target])
        plt.show()

      #calculate final observer score
      samples = 1000
      final_scores = []

      for i in range(0, samples):
        observer.reset_belief()


        target = self.gs.targets[np.random.randint(len(self.gs.targets))]
        self.refresh_R_table(target, self.gs.targetUtility)

        current_state = self.gs.startState
        prev_state = current_state
        steps = [current_state]
        q_table = self.q_table_dict[target]
        agent_points = self.gs.targetUtility
        while current_state != target:
          #print(current_state)
          #print(target)
          next_step_index = self.gimme_move(q_table, prev_state, current_state)

          #self.update(current_state,next_step_index,target)
          steps.append(next_step_index)
          
          #observer work
          observer.update_belief(current_state)
          observer_guess = observer.belief_guess()

          score = self.update(current_state,next_step_index, target)
          if observer_guess == target and current_state != self.gs.startState:
              self.apply_guess_penalty(prev_state, current_state, target)
              agent_points -= self.gs.guessReward

          self.scores_dict[target].append(score)

          observer.observe_action(current_state, target)
          prev_state = current_state
          current_state = next_step_index
        final_scores.append(agent_points)
      print "\n"
      print("Belief Update Average Score for Observer: " , self.gs.targetUtility - (sum(final_scores) / float(len(final_scores))))   
      plt.plot(final_scores)
      plt.show()

    def train_agent_LP(self, episodes, lp_dict):
        #self.generateQTables(self.gs.nodesNum, .8, self.gs.targets)
        #self.reset_guess_table()
        final_lp_scores = []
        for target in self.gs.targets:
          self.refresh_R_table(target,self.gs.targetUtility)

          possible_action = self.get_possible_actions(self.gs.startState)
          action = self.preview_next_action(possible_action)

          self.update(self.gs.startState, action, target)
          scores = []
          #place agent in a random location, make a move, record results
          for i in range(episodes):
            current_state = np.random.randint(0, int(self.q_table_dict[target].shape[0]))
            possible_action = self.get_possible_actions(current_state)
            action = self.preview_next_action(possible_action)

            #lp guessing
            observer_guess = 0
            best_guess_value = 0
            for t in self.gs.targets:
              if lp_dict[(action, t)] > best_guess_value:
                best_guess_value = lp_dict[(current_state, t)]
                observer_guess = t

            score = self.update(current_state,action, target)
            if observer_guess == target and current_state != self.gs.startState:
                self.apply_guess_penalty(current_state, action, target)
                #agent_points -= self.gs.guessReward

            scores.append(score)

          # Testing
          
          current_state = self.gs.startState
          prev_state = current_state
          prev_state = current_state
          steps = [current_state]
          q_table = self.q_table_dict[target]
          agent_score_lp = self.gs.targetUtility
          while current_state != target:

              next_step_index = self.gimme_move(q_table, prev_state, current_state)
              steps.append(next_step_index)

              observer_guess = 0
              best_guess_value = 0

              for t in self.gs.targets:
                if lp_dict[(current_state, t)] > best_guess_value:
                  best_guess_value = lp_dict[(current_state, t)]
                  observer_guess = t

              if observer_guess == target:
                agent_score_lp -= self.gs.guessReward

              prev_state = current_state
              current_state = next_step_index
          print "\n"
          print("Agent Summary Against Stationary Observer: " + str(target))
          print("Most efficient path:")
          print(steps)
          print("observer score ", self.gs.targetUtility - agent_score_lp)
          final_lp_scores.append(self.gs.targetUtility - agent_score_lp + 0.0)
          self.path_dict.update({target: steps})
          plt.plot(scores)
          plt.show()
        print(final_lp_scores)
        print("Observer Stationary Strategy Outcome: " + str(sum(final_lp_scores)/len(final_lp_scores)))
        return self

