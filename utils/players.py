import numpy as np


class BasePlayer(object):
    def __init__(self):
        self.past_actions = []
        self.num_games = 0

    def get_action_history(self):
        return self.past_actions

    def initial_action(self):
        """function defining the policy on how to act on the initial move,
        when the opponents do not have the history of each other"""
        pass

    def reset(self):
        self.past_actions = []
        self.num_games = 0

    def get_action(self, opponents_history: list):
        """General function to return an action (cooperate or defect)
        given a list of the opponents actions, if the list of opponents actions is empty then
        use <initial_action()> for the action to choose in the start of the game

        :param list opponents_history: List of actions the opponent took while playing the game.
        :returns str action: string action "cooperate" or "defect".
        :rtype: bool
        """

        # initial move in the game
        if len(opponents_history) == 0:
            action = self.initial_action()

        else:
            # policy
            pass

        self.past_actions.append(action)
        self.num_games += 1

        return action


class Tit4Tat(BasePlayer):
    def initial_action(self):
        return "cooperate"

    def get_action(self, opponents_history: list):

        if len(opponents_history) == 0:
            action = self.initial_action()

        else:
            action = opponents_history[-1]

        self.past_actions.append(action)
        self.num_games += 1
        return action


class Tit42Tats(BasePlayer):
    def initial_action(self):
        return "cooperate"

    def get_action(self, opponents_history: list):

        if len(opponents_history) <= 1:
            action = self.initial_action()

        else:
            action = opponents_history[-2]

        self.past_actions.append(action)
        self.num_games += 1
        return action


class Cooperator(BasePlayer):
    def initial_action(self):
        return "cooperate"

    def get_action(self, opponents_history: list):

        if len(opponents_history) == 0:
            action = self.initial_action()

        else:
            action = "cooperate"

        self.past_actions.append(action)
        self.num_games += 1
        return action


class Defector(BasePlayer):
    def initial_action(self):
        return "defect"

    def get_action(self, opponents_history: list):

        if len(opponents_history) == 0:
            action = self.initial_action()

        else:
            action = "defect"

        self.past_actions.append(action)
        self.num_games += 1
        return action


class Resentful(BasePlayer):
    def initial_action(self):
        return "cooperate"

    def get_action(self, opponents_history: list):

        if len(opponents_history) == 0:
            action = self.initial_action()

        else:
            if "defect" in opponents_history:
                action = "defect"
            else:
                action = "cooperate"

        self.past_actions.append(action)
        self.num_games += 1
        return action


class Tester(BasePlayer):
    def initial_action(self):
        return "defect"

    def get_action(self, opponents_history: list):

        if len(opponents_history) == 0:
            action = self.initial_action()

        else:
            opp_action = opponents_history[0]
            if opp_action == "defect":
                action = "cooperate"
            else:
                action = "defect"

        self.past_actions.append(action)
        self.num_games += 1
        return action


class Majority(BasePlayer):
    def initial_action(self):
        return "cooperate"

    def get_action(self, opponents_history: list):

        if len(opponents_history) == 0:
            action = self.initial_action()

        else:
            opponents_history = np.array(opponents_history)
            num_cooperations = (opponents_history == "cooperate").sum()
            num_defects = (opponents_history == "defect").sum()
            if num_cooperations >= num_defects:
                action = "cooperate"
            else:
                action = "defect"

        self.past_actions.append(action)
        self.num_games += 1
        return action


class Random(BasePlayer):
    def initial_action(self):
        return np.random.choice(["cooperate", "defect"])

    def get_action(self, opponents_history: list):

        if len(opponents_history) == 0:
            action = self.initial_action()

        else:
            action = np.random.choice(["cooperate", "defect"])

        self.past_actions.append(action)
        self.num_games += 1
        return action
