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
* 'r': Restart the game after game over.
* Left arrow key: Move the tetromino left by one space. If held, move by multiple, depending on duration of hold
* Right arrow key: Move the tetromino right by one space. If held, move by multiple, depending on duration of hold.
* Down arrow key: Move the tetromino down by one space. If held, move by multiple, depending on duration of hold.
* Up arrow key: Rotate the tetromino clockwise by 90 degrees. If held, rotated multiple times, depending on duration.
* Space bar: Drop the piece down to the bottom of the board (where the current ghost piece is)
* Shift: Move the current tetromino to the hold space. Can only do once per new tetromino

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