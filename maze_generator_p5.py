from p5 import *
from queue import LifoQueue
import numpy as np
import sys
import time
from Point import Point


grid = []
rows = 8
cols = 8
h = floor(height / rows)
w = floor(width / cols)
stack = LifoQueue()
        
def gridfilled(grid) -> bool:    
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j].visited == False:
                return False
    return True

def remove_wall(current: Point, neighbour: Point):
    
    #same y
    if current.i == neighbour.i:
        #current left
        if current.j < neighbour.j:
            current.right = False
            neighbour.left = False
        # current below neighbour
        elif current.j > neighbour.j:
            current.left = False
            neighbour.right = False
    #same x
    elif current.j == neighbour.j:
        # current above
        if current.i < neighbour.i:
            current.down  = False
            neighbour.up = False
        # current right
        elif current.i > neighbour.i:
            current.up = False
            neighbour.down = False
    return None
        

def setup():
    global grid 
    size(600, 600)
    grid =  [['' for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = Point(i, j)
    
    for i in range(rows):
        for j in range(cols):
            grid[i][j].neighbours = grid[i][j].create_neighbours(grid)
    
    start = grid[0][0]
    start.visited = True
    stack.put(start)
    
def draw():

    global grid 
    next = None
    background(51)
    # Choose the initial cell, mark it as visited and push it to the stack  
        # While the stack is not empty
        #   Pop a cell from the stack and make it a current cell
        #   If the current cell has any neighbours which have not been visited
        #       Push the current cell to the stack
        #       Choose one of the unvisited neighbours
        #       Remove the wall between the current cell and the chosen cell
        #       Mark the chosen cell as visited and push it to the stack
    
    if stack.qsize() == 0:
        noLoop()
        time.sleep(10)
        sys.exit()
    current = stack.get()
    unvisited = []
    for neighbour in current.neighbours:
        if not neighbour.visited:
            unvisited.append(neighbour)
    if len(unvisited) > 0:
        stack.put(current)
        next = np.random.choice(unvisited)
        remove_wall(current, next)
        next.visited = True
        stack.put(next)
            
    # draw the state
    
    #draw visited cells
    for i in range(rows):
        for j in range(cols):
            point = grid[i][j]
            if point.visited:
                fill(255, 0, 255, 100)
                noStroke()
                rect((w * point.j, h * point.i), w - 1 , h - 1 )
    
    #draw walls
    for i in range(rows):
        for j in range(cols):
            point = grid[i][j]
            point.show(w, h)
    
    #draw current 
    noStroke()
    fill(0, 0, 255)
    rect((w * current.j, h * current.i), w-1, h-1) 
    
    if next is not None:
        noStroke()
        fill(255, 0, 0)
        rect((w * next.j, h * next.i), w-1, h-1) 

if __name__ == '__main__':    
    run()


