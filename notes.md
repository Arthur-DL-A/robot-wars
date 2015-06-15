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


Function definition
-------------------

### Output

We expect output in the form of a formatted string. The command is
evaluated in character pairs,

```
class Robot:
    def react(tiles, board_size, current_position):
        mnsw
```

Tiles = dict
