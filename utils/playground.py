class PlayGround(object):
    def __init__(
        self,
        player1: object,
        player2: object,
        player1_name: str,
        player2_name: str,
        num_games: int = 100,
    ):

        self.max_games = num_games
        self.num_games = 0

        self.player1, self.player2 = player1, player2
        self.player1_name, self.player2_name = player1_name, player2_name
        self.score_player1, self.score_player2 = 0, 0

    def play(self, verbose: bool = True):

        if self.num_games < self.max_games:
            self.num_games += 1

            # get the histories
            player1_history = self.player1.get_action_history()
            player2_history = self.player2.get_action_history()

            # act based on histories from the opponents
            action_p1 = self.player1.get_action(opponents_history=player2_history)
            action_p2 = self.player2.get_action(opponents_history=player1_history)

            # check the payoffs
            score_p1, score_p2 = self.rules(action_p1=action_p1, action_p2=action_p2)

            if verbose:
                print(
                    f"Player 1 ({self.player1_name}): [{action_p1}], Player 2 ({self.player2_name}): [{action_p2}]"
                )
                print(
                    f"\t -> Player 1 ({self.player1_name}) gets {score_p1} years in prison"
                )
                print(
                    f"\t -> Player 2 ({self.player2_name}) gets {score_p2} years in prison"
                )

            self.score_player1 += score_p1
            self.score_player2 += score_p2
            return False

        return True

    def run(self, verbose: bool = True):
        done = False
        while not done:
            done = self.play(verbose=verbose)

    def rules(self, action_p1: str, action_p2: str):
        if (action_p1 == "cooperate") and (action_p2 == "cooperate"):
            return (1, 1)

        elif (action_p1 == "defect") and (action_p2 == "cooperate"):
            return (0, 20)

        elif (action_p1 == "cooperate") and (action_p2 == "defect"):
            return (20, 0)

        elif (action_p1 == "defect") and (action_p2 == "defect"):
            return (5, 5)
