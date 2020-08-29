# PyQt Tetris

<img align="right" src=data/Tetris_Main_Demo.gif width="480" height="337"/>

<p align="justify">
PyQt Tetris is a single player tetris game implemented via PyQt5. Modeled after the now-defunct
Facebook Tetris, it allows the user to play a two-minute round of traditional tetris, where the
aim is to 'send' as many lines as possible in that time period. 
</p>

<p align="justify">
Tetris is a tile-matching video game created in 1984, where the goal is for the user to control 
pieces called tetrominoes that automatically descend, and maneuver them to complete rows. The user is able to move the
tetrominoes left and right, and rotate them. The only thing they are not allowed to do is to move
the tetromino upwards. Once a row is completely filled by tetromino blocks, the row disappears, and
all rows above that row shift down. 
</p>

There are many game modes that exist within Tetris. Some of the traditional game modes are shown below. For a list of 
implemented game modes and further explanation, see [here](#game-modes): 
* Marathon: Compete for highest score as pieces descend faster and faster as more lines are cleared
* Sprint 40: Compete for the shortest amount of time needed to clear 40 lines
* Battle 2P: Compete in order to knockout an opponent by clearing lines to send lines to the opponent
* Time Trial: Compete for the most lines sent given a specific amount of time

___

### Controls
* 'Enter' or 'Return': Start the game 
* 'p': Pause the game/resume the game
* 'q': Quit the game
* 'r': Restart the game after game over
* Left arrow key: Move tetromino left by one space. If held, move by multiple, depending on hold duration
* Right arrow key: Move tetromino right by one space. If held, move by multiple, depending on hold duration
* Down arrow key: Move tetromino down by one space. If held, move by multiple, depending on hold duration
* Up arrow key: Rotate tetromino clockwise by 90°. If held, rotate multiple times, depending on hold duration
* Space bar: Drop the piece down to the bottom of the board (where the current ghost piece is)
* Shift: Move the current tetromino to the hold space. Can only do once per new tetromino

___

### Game Configuration
Game configurations that are currently implemented. Choices in __bold__ are the default.


* Randomizer: The strategy for which new pieces are added to the queue.
  * __Classic__: Completely random pieces
* Previews: How many pieces you can see coming up next
  * __4__: The next four pieces in the queue can be seen at all times
* Lock Delay: How much time a piece can wait on the ground before locking into place. There are three 
types of lock delay. L1 lock delay is the maximum amount of time after a piece is soft-dropped to the ground
before it locks. L2 lock delay is the maximum amount of time after a piece is soft-dropped to the ground and
kept in motion via left/right arrow keys before it locks. L3 lock delay is the maximum amount of time a piece
can be kept in motion when it first enters the grid before it is force-hard dropped and locked into place.
Note that L1 lock delay is reset if the piece is moved or rotated after soft-dropped to the ground, L2
lock delay is reset if the piece is rotated after soft-dropped to the ground, and L3 lock delay can never
be reset.
  * L1: __500 milliseconds__
  * L2: __5000 milliseconds__
  * L3: __20000 milliseconds__
* Clear Delay: How much time is required for a line to clear. During this time, no action can be performed.
  * Delay: __0 milliseconds__
* Gravity Level: The speed at which the live tetromino automatically descends
  * Gravity: __1 block/seconds__
* DAS: Delayed auto shift - how long you have to hold down the left or right arrow key before the block moves in that 
direction. 
  * DAS: __133 milliseconds__
* ARR: Auto repeat rate - how fast the tetromino moves left or right when the left or right arrow keys are held.
  * ARR: __20 milliseconds__


___

### Game Modes
Currently, the implemented game modes include:
* Time Trial
  * The goal of this is to see how many lines can be sent by the user within 120 seconds, or two minutes. The game will
  start timing immediately, and will freeze all keyboard control after the two minutes have elapsed.
  
___
  
### Future Work
* Leaderboards
* Sprint game mode
* Marathon game mode
* Custom keyboard control
* Customize game configuration