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

The API reference and other documentation can be found in the `doc`
folder.

TODO: how scoring works


Notes - TODO into README
========================

API
---

*Note: I took a lot from [Robot
Game](https://robotgame.net/gettingstarted), including the idea of using
a `game` variable, the 'guard' action, and a few variable names. Thought
it would be a good base for now.*

*Note: This should be moved to the README once it's finished.*

To be valid, an AI must be part of the Robot class and must have a
`make_turn()` function.

To create an AI, simply make a new Python file and define the Robot
class and an implementation for the `act()` function. For example:

    class Robot: def act(self, game): return "guard"

This robot would guard for the entire game. Tactical!

The `game` variable is a dictionary which holds all of the information
you receive for that turn. Its contents are described in the below
sections.

You can access any one of these variables as keys in a dictionary or as
attributes, e.g. `game['health']`, `game.health`, `game[location].x`
etc.


### `visible_tiles`

Type: `dict[dict]`

The radius circle of tiles around your robot which you are given
information about.

Each tile is stored absolutely, *not* relative to your robot's current
position (TODO: agree/disagree? what're your thoughts?). e.g. TODO

*(TODO: I like the absolute idea because it might make it easier to
record tiles each turn, and build up a vision of the board. Also
slightly easier implementation, since we just have to provide a slice of
the game board rather than making it all relative and awkward.)*


### `health`

Type: `int`

Your robot's current health.

TODO: max?


### `action_points`

Type: `int`

Your robot's current Action Points, used to perform actions such as
moving or attacking during your turn.


### `location`

Type: `dict`

The co-ordinate of the tile your robot is on. This is measured (?) from
the top left. You may assume that the game board is 8x8 (TODO), i.e. (0,
0) is the top-left corner and (7, 7) the bottom-right.



Function definition
-------------------

### Output

We expect output in the form of a formatted string. The command is
evaluated in character pairs, [...]

Would it be easier to maybe separate commands by spaces? Slightly less
confusing too, since we can use more English commands like Robot Game.
