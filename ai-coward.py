#!/usr/bin/env python3
#
# An AI for Robot Wars.

import sys

class Robot:
    def act(self, game):
        # TODO
        print(game["health"], file=sys.stderr)
        print(game.health, file=sys.stderr)

        # testing for bad command error catching
        return [["guuard"]]
