import sys

sys.path.append("..")

import numpy as np

from utils.players import (
    Cooperator,
    Defector,
    Majority,
    Random,
    Resentful,
    Tester,
    Tit4Tat,
    Tit42Tats,
)
from utils.playground import PlayGround


def main(verbose: bool = False):

    strategies = [
        "Tit4Tat",
        "Tit42Tats",
        "Cooperator",
        "Defector",
        "Resentful",
        "Tester",
        "Majority",
        "Random",
    ]
    players1 = [
        Tit4Tat(),
        Tit42Tats(),
        Cooperator(),
        Defector(),
        Resentful(),
        Tester(),
        Majority(),
        Random(),
    ]
    players2 = [
        Tit4Tat(),
        Tit42Tats(),
        Cooperator(),
        Defector(),
        Resentful(),
        Tester(),
        Majority(),
        Random(),
    ]

    results = []

    for i, player1 in enumerate(players1):
        buffer_results = []
        player1.reset()

        if verbose:
            print("#" * 30)
        for j, player2 in enumerate(players2):
            player2.reset()

            environment = PlayGround(
                player1=player1,
                player1_name=strategies[i],
                player2=player2,
                player2_name=strategies[i],
            )
            environment.run(verbose=verbose)

            buffer_results.append(
                (environment.score_player1, environment.score_player2)
            )

        results.append(buffer_results)

    # Print some statistics on the Scores of each of the players playing against each other and the final scoreboard

    year_counters = [0 for _ in range(len(strategies))]

    print("\n\n")
    print("SCORING MATRIX:\n")
    print(
        "        | Tit4Tat  |  Tit42Tats  |  Cooperator  |  Defector  |  Resentful  |  Tester  |  Majority |  Random",
        end="",
    )
    for i, row in enumerate(results):
        print()
        print("--" * 50)
        print(strategies[i], end=" | ")
        for column in row:
            print(column, end=" | ")
            year_counters[i] += column[0]

    print("\n\n")
    print("LEADER BOARD: \n")
    print("Position    Strategy    Total score")
    print("--" * 20)
    idxs = np.argsort(np.array(year_counters))

    ctr = 0
    for i in idxs:
        ctr += 1
        print(f"#{ctr}/{len(strategies)}        {strategies[i]}   {year_counters[i]}")


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description="My parser")
    parser.add_argument(
        "--verbose", default=False, action=argparse.BooleanOptionalAction
    )
    args = parser.parse_args()

    main(verbose=args.verbose)
