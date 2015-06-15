Brainstorming
-------------

We want to write a simple 1v1 AI arena combat game. We'll run a
competition of sorts where we pit AIs against each other and score or
rank them.


* Combat AIs
* Grid-based (moving +1 units, unit(2,3))
* Square or rectangular finite board

* Input:
  * Circle of tiles around their current tile
  * Board size
  * Current coordinate on the board

* Robot:
  * Health
  * Action Points:
    * e.g. Moving = 1,
           Pushing = 1,
           Shooting = 2
  * Actions:
    * Move
    * Punch
    * Shoot


API
---

*Note: I took a lot from
[Robot Game](https://robotgame.net/gettingstarted), including the idea
of using a `game` variable, the 'guard' action, and a few variable
names.
Thought it would be a good base for now.*

*Note: This should be moved to the README once it's finished.*

To be valid, an AI must be part of the Robot class and must have a
`make_turn()` function.

To create an AI, simply make a new Python file and define the Robot
class and an implementation for the `act()` function. For example:

    class Robot:
        def act(self, game):
            return "guard"

This robot would guard for the entire game. Tactical!

The `game` variable is a dictionary which holds all of the information
you receive for that turn. Its contents are:

  * `health`:
  * `action_points`:
  * `location`:
  * TODO, etc.

You can access any one of these variables using the syntax
`game['health']`, `game['action_points']` etc.


Function definition
-------------------

### Output

We expect output in the form of a formatted string. The command is
evaluated in character pairs, [...]

Would it be easier to maybe separate commands by spaces? Slightly less
confusing too, since we can use more English commands like Robot Game.
