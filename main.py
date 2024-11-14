# main.py

import Config
import functions
from Config import Symbol
import random 

#if firstTurn == 1:
#randomize who goes first player or ai
firstTurn = random.randint(1,2)



#basegrid

grid = [
  [Symbol.EMPTY, Symbol.EMPTY, Symbol.EMPTY],
  [Symbol.EMPTY, Symbol.EMPTY, Symbol.EMPTY],
  [Symbol.EMPTY, Symbol.EMPTY, Symbol.EMPTY] 
]



playCount = 0
if firstTurn == 1:
  functions.AIPlay(grid)
  playCount+=1
  
functions.printGrid(grid)

while True:
  
  functions.playerPlay(grid)
  playCount+=1
  result = functions.decider(grid)
  if result == 1:
    functions.printGrid(grid)
    print()
    print("Wow! You won! ")
    break
  if playCount == 9:
    print("It's a tie!")
    break
  # Ai Plays
  functions.AIPlay(grid)
  functions.printGrid(grid)
  print()
  playCount+=1
  result = functions.decider(grid)
  if result == 2:
    print("You lose! (row) ")
    break
  if result == 3:
    print("You lose! (col)")
    break
  if playCount == 9:
    print("It's a tie!")
    break

