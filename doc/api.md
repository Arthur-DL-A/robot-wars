API reference
=============

Creating a robot
----------------

To be valid, a robot must be part of the Robot class and must implement
the `Robot.act(self, game)` method. You may use any number of other
methods and attributes. Any data you store in the class (as attributes)
is stored between turns. In this way, you can record information from
previous turns.


Taking action
-------------

The method must return one or more valid actions to perform, in a list.
Depending on your action points, you may be able to perform more than
one action on your turn. If you want to perform multiple actions, they
must be in separate elements.

An action is comprised of a list containing one or more strings.
Depending on the action, you may have to specify a direction, e.g. 'move
up'. Note that this means you will be returning a *list in a list*.

Following is an example robot which tries to move left then guard every
turn:

```python
class Robot:
    def act(self, game):
        return [["move", "left"], ["guard"]]
```

The robot will try to perform as many of the actions you return as
possible. If it does not have enough action points to perform an action,
it will stop and end its turn.

Note that even if you only want to perform one action, you still have to
return a list:

```python
class Robot:
    def act(self, game):
        return [["shoot", "up"]]
```


The `game` variable
-------------------

Every turn, data is passed to each robot about the board and the current
game in the `game` dictionary. Details on its contents are described
below. A summary of the current keys in the dictionary follows:

  * health
  * action_points
  * location
    * x
    * y
  * visible_tiles
    * tile
      * x
      * y


Note that you can access any one of these variables as keys in a
dictionary or as attributes of an object: e.g. `game['health']`,
`game.health`, `game[location].x` etc.


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
