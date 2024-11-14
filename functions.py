2#create base grid
import Config
import random
from Config import Symbol

def printGrid(grid):
  for row in range(3):
    if row != 0:
      print(Config.LINE)
    
    for col in range(2):
      
      print(grid[row][col].value, end = "|")
    
    print(grid[row][2].value)
    
def playerPlay(grid):
  row = int(input("What row will you play in? "))
  col = int(input("What column will you play in? "))
  
  while grid[row][col] != Symbol.EMPTY:
    print("This location has already been played, pick another location! ")
    row = int(input("What row will you play in? "))
    col = int(input("What column will you play in? "))
    
  grid[row][col] = Symbol.X

def immediateWin(grid):
  
  #prioritizing the win for cols
  for i in range(len(grid)):
    if grid[i][0] == Symbol.O and grid[i][1] == Symbol.O:
      if grid[i][2] == Symbol.EMPTY:
        grid[i][2] = Symbol.O
        return True
      
  for i in range(len(grid)):
    if grid[i][2] == Symbol.O and grid[i][1] == Symbol.O:
      if grid[i][0] == Symbol.EMPTY:
        grid[i][0] = Symbol.O
        return True
      
  for i in range(len(grid)):
    if grid[i][0] == Symbol.O and grid[i][2] == Symbol.O:
      if grid[i][1] == Symbol.EMPTY:
        grid[i][1] = Symbol.O
        return True
      
  #prioritizing the wins for rows
  for i in range(len(grid)):
    if grid[0][i] == Symbol.O and grid[1][i] == Symbol.O:
      if grid[2][i] == Symbol.EMPTY:
        grid[2][i] = Symbol.O
        return True
          
  for i in range(len(grid)):
    if grid[2][i] == Symbol.O and grid[1][i] == Symbol.O:
      if grid[0][i] == Symbol.EMPTY:
        grid[0][i] = Symbol.O
        return True
      
  for i in range(len(grid)):
    if grid[0][i] == Symbol.O and grid[2][i] == Symbol.O:
      if grid[1][i] == Symbol.EMPTY:
        grid[1][i] = Symbol.O
        return True
      
  #prioritizing the wins for diagonals
  
  #first diagonal
  if grid[0][0] == Symbol.O and grid[1][1] == Symbol.O:
    if grid[2][2] == Symbol.EMPTY:
      grid[2][2] = Symbol.O
      return True
    
  if grid[0][0] == Symbol.O and grid[2][2] == Symbol.O:
    if grid[1][1] == Symbol.EMPTY:
      grid[1][1] = Symbol.O
      return True
  
  if grid[1][1] == Symbol.O and grid[2][2] == Symbol.O:
    if grid[0][0] == Symbol.EMPTY:
      grid[0][0] = Symbol.O
      return True
  
  #second diagonal    
  if grid[2][0] == Symbol.O and grid[1][1] == Symbol.O:
    if grid[0][2] == Symbol.EMPTY:
      grid[0][2] = Symbol.O
      return True
    
  if grid[1][1] == Symbol.O and grid[0][2] == Symbol.O:
    if grid[2][0] == Symbol.EMPTY:
      grid[2][0] = Symbol.O
      return True
  
  if grid[2][0] == Symbol.O and grid[0][2] == Symbol.O:
    if grid[1][1] == Symbol.EMPTY:
      grid[1][1] = Symbol.O
      return True
  return False
  
def blockImmediateWin(grid):
  # if two cols are x that are next to each other in the same row (first two loops)
  for i in range(len(grid)):
    if grid[i][0] == Symbol.X and grid[i][1] == Symbol.X:
      if grid[i][2] == Symbol.EMPTY:
        grid[i][2] = Symbol.O
        return True
        
          
  for i in range(len(grid)):
    if grid[i][2] == Symbol.X and grid[i][1] == Symbol.X:
      if grid[i][0] == Symbol.EMPTY:
        grid[i][0] = Symbol.O
        return True
      
  for i in range(len(grid)):
    if grid[i][0] == Symbol.X and grid[i][2] == Symbol.X:
      if grid[i][1] == Symbol.EMPTY:
        grid[i][1] = Symbol.O
        return True
  # if two rows are x that are next to each other in the same col (next two loops)        
  for i in range(len(grid)):
    if grid[0][i] == Symbol.X and grid[1][i] == Symbol.X:
      if grid[2][i] == Symbol.EMPTY:
        grid[2][i] = Symbol.O
        return True
          
  for i in range(len(grid)):
    if grid[2][i] == Symbol.X and grid[1][i] == Symbol.X:
      if grid[0][i] == Symbol.EMPTY:
        grid[0][i] = Symbol.O
        return True
  
  for i in range(len(grid)):
    if grid[0][i] == Symbol.X and grid[2][i] == Symbol.X:
      if grid[1][i] == Symbol.EMPTY:
        grid[1][i] = Symbol.O
        return True
  
  #first diagonal
  if grid[0][0] == Symbol.X and grid[1][1] == Symbol.X:
    if grid[2][2] == Symbol.EMPTY:
      grid[2][2] = Symbol.O
      return True
    
  if grid[0][0] == Symbol.X and grid[2][2] == Symbol.X:
    if grid[1][1] == Symbol.EMPTY:
      grid[1][1] = Symbol.O
      return True
  
  if grid[1][1] == Symbol.X and grid[2][2] == Symbol.X:
    if grid[0][0] == Symbol.EMPTY:
      grid[0][0] = Symbol.O
      return True
  
  #second diagonal    
  if grid[2][0] == Symbol.X and grid[1][1] == Symbol.X:
    if grid[0][2] == Symbol.EMPTY:
      grid[0][2] = Symbol.O
      return True
    
  if grid[1][1] == Symbol.X and grid[0][2] == Symbol.X:
    if grid[2][0] == Symbol.EMPTY:
      grid[2][0] = Symbol.O
      return True
  
  if grid[2][0] == Symbol.X and grid[0][2] == Symbol.X:
    if grid[1][1] == Symbol.EMPTY:
      grid[1][1] = Symbol.O
      return True
  
  return False

def gridEmpty(grid):
  for i in range(len(grid)):
    for j in range(len(grid)):
      if grid[i][j] != Symbol.EMPTY:
        return False
  return True
  
def playOppositeCorner(grid):
  if grid[0][0] == Symbol.O and grid[2][2] == Symbol.EMPTY:
    grid[2][2] = Symbol.O
    return True
    
  if grid[2][2] == Symbol.O and grid[0][0] == Symbol.EMPTY:
    grid[0][0] = Symbol.O
    
    return True
    
  if grid[2][0] == Symbol.O and grid[0][2] == Symbol.EMPTY:
    grid[0][2] = Symbol.O 
    return True
    
  if grid[0][2] == Symbol.O and grid[2][0] == Symbol.EMPTY:
    grid[2][0] = Symbol.O 
    return True
  return False
  
    
def playFork(grid):
  
  if gridEmpty(grid):
    
    playCorner(grid)
    return True
    
  if grid[1][1] == Symbol.X and (grid[0][0] == Symbol.O or grid[2][2] == Symbol.O or grid[2][0] == Symbol.O or grid[0][2] == Symbol.O):
   
    playOppositeCorner(grid)
    return True
        
    
  if grid[0][0] == Symbol.O and grid[2][2] == Symbol.O and grid[1][1] == Symbol.X:
  
    playSides(grid)
    return True
    
  if grid[2][0] == Symbol.O and grid[0][2] == Symbol.O and grid[1][1] == Symbol.X:
    
    playSides(grid)
    return True
  return False
  
  
def blockFork(grid):
  if grid[0][0] == Symbol.X and grid[2][2] == Symbol.X and grid[1][1] == Symbol.O:
    playSides(grid)
    return True
    
  if grid[2][0] == Symbol.X and grid[0][2] == Symbol.X and grid[1][1] == Symbol.O:
    playSides(grid)
    return True
  return False

  
def playCenter(grid):
  if grid[1][1] == Symbol.EMPTY:
    grid[1][1] = Symbol.O
    return True
  return False
  
def playCorner(grid):
  if grid[0][0] == Symbol.EMPTY:
    grid[0][0] = Symbol.O
    return True
    
  if grid[2][2] == Symbol.EMPTY:
    grid[2][2] = Symbol.O
    return True
  
  if grid[0][2] == Symbol.EMPTY:
    grid[0][2] = Symbol.O
    return True
    
  if grid[2][0] == Symbol.EMPTY:
    grid[2][0] = Symbol.O
    return True
  return False
  
def playSides(grid):
  if grid[0][1] == Symbol.EMPTY and grid[2][1] == Symbol.EMPTY:
    grid[0][1] = Symbol.O
    return True
  
  if grid[1][0] == Symbol.EMPTY and grid[1][2] == Symbol.EMPTY:
    grid[1][0] = Symbol.O
    return True
  return False  
  

def AIPlay(grid):
  
  if immediateWin(grid):
    return
  
  if blockImmediateWin(grid):
    return
  
  status = playFork(grid)
  
  if status:
    return
  
  if blockFork(grid):
    return
  
  if playCenter(grid):
    return
  
  if playCorner(grid):
    return
  
  if playSides(grid):
    return
  
  row = random.randint(0,2)
  col = random.randint(0,2)
  
    
  while grid[row][col] != Symbol.EMPTY:
    row = random.randint(0,2)
    col = random.randint(0,2)
  grid[row][col] = Symbol.O 
    
    
  
    
    
    
def decider(grid):
  
  for i in range(len(grid)):
    if grid[i][0] == grid[i][1] and grid[i][0] == grid[i][2]:
      if grid[i][0] == Symbol.X:
        
        return 1
      if grid[i][0] == Symbol.O:
        
        return 2
        
      
  for i in range(len(grid)):
    if grid[0][i] == grid[1][i] and grid[0][i] == grid[2][i]:
      
      if grid[0][i] == Symbol.X:
        
        return 1
      if grid[0][i] == Symbol.O:
        
        return 3
        
      
  if grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2]:
      if grid[0][0] == Symbol.X:
        
        return 1
        
      if grid[0][0] == Symbol.O:
        
        return 2
        
  if grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0]:
      if grid[0][2] == Symbol.X:
       
        return 1
        
      if grid[0][2] == Symbol.O:
        
        return 2
    