# game_of_life-aksel-CDOF4
Creating an open source game of life project that will work in a terminal.

The code is divided in three parts: 
- imports
- functions
- main

For now, the only library that is imported is the "random" library to initialize the grid with both dead and living cells.

The function "get neighbors" will list all the neighbors of a cell (by checking around its position while staying inside the bounds of the grid).
The function "update cell" will update the status of the present cell (dead or alive) after checking how many neighbors said cell has.
The function "next gen" will initialize the next state grid.
The "print grid" function prints the grid with filled squares when the cells are alive and hollow squares when the cells are dead.

In the main, a random grid is initalized and the user can decide to reach the next state by pressing Enter.

How to run the game: 

Clone the repo:
    ``` git clone git@github.com:Rubiksel/game_of_life-aksel-CDOF4.git ```

- Windows: open a command prompt window and navigate to the "core.py" file directory. Type in your command prompt "python3 core.py".
- MacOS/Linux: open a terminal window and navigate to the "core.py" file directory. Type in your terminal "python core.py".

If you see any problems or ways for improvements in the code, please don't hesitate to raise an issue.

Have fun with the game!

Rubiksel