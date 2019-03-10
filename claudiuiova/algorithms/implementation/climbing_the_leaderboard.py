#!/bin/python3

import math
import os
import random
import re
import sys
import time
import datetime


def timer(func):
    def time_measuring(*args):
        start = time.time()
        function_content = func(*args)
        end = time.time() - start
        if end < 60:
            print("Took: {} sec".format(end))
        elif int(end) in range(60, 3600):
            print("Took: {} min and {} sec".format(int(end // 60), end % 60))
        else:
            print("Took: {} h {} min {} sec".format(int(end // 3600), int(end % 3600), end % 60))

        return function_content

    return time_measuring


@timer
def climbingLeaderboard(scores, alice):
    return_array = []
    for game_score in alice:
        if game_score < scores[-1]:
            return_array.append(len(set(scores)) + 1)
        elif game_score >= scores[0]:
            return_array.append(1)
        elif game_score in scores:
            return_array.append(len(set(scores[:scores.index(game_score)])) + 1)
        else:
            closest_value = min(scores, key=lambda x: abs(x-game_score))
            return_array.append(len(set(scores[:scores.index(closest_value)])) + 1)

    return return_array


if __name__ == '__main__':
    scores_count = 200000
    with open("climb_the_leaderboard.txt") as txt:
        content = txt.readlines()

    # scores = list(map(int, content[0].rstrip().split()))
    scores = list(map(int, "100 100 50 40 40 20 10".rstrip().split()))

    alice_count = 100000

    # alice = list(map(int, content[1].rstrip().split()))
    alice = list(map(int, "5 25 50 120".rstrip().split()))

    result = climbingLeaderboard(scores, alice)
    print(result)

