Robot Wars
==========

Intro
-----

Robot Wars is a heated 1v1 AI arena combat game written in Python.
Create robots with unique behaviours to defeat your opponents. Move,
guard, attack and shoot your way to victory!

Robot Wars has two main parts: an API to program robot AI using, and a
simulation module which pits two robots against eachother in a tiled
arena. Each turn, robots receive information about themselves and the
arena, and can take action in a number of different ways, subject to
their Action Points for that turn. The aim of the game is to destroy the
opposing robot.


Making a robot
--------------

To make a robot, you'll want to consult the Robot class reference, found
in `doc/api.md`. All other documentation can be found in the `doc`
folder.

To create a robot, simply make a new Python file and define the Robot
class and an implementation for the `Robot.act(self, game)` method.
For example:

```python
class Robot:
    def act(self, game):
        return ["guard"]
```

Such a robot would guard for the entire game. Tactical!


Competition format & scoring
----------------------------

This section is specifically for CS club members!

After giving you a couple of weeks to develop your robots, we will be
running a competition to determine the best robot -- a survival of the
fittest. Each robot will be pitted against each other robot. The winner
of a match will earn a point. After all matches have taken place, the
overall winner will be the robot with the highest score, i.e. most wins.
