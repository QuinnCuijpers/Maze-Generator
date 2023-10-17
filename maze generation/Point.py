from p5 import *

class Point():
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.visited = False
        self.neighbours = []
        
        #wall locations
        self.up = True
        self.down = True
        self.left = True
        self.right = True
        
    def create_neighbours(self, grid):
        
        neighbours = []
        i = self.i
        j = self.j
        rows = len(grid)
        cols = len(grid[0])
        
        if  j < cols - 1:
            #down
            neighbours.append(grid[i][j+1])
        if j > 0:
            #up
            neighbours.append(grid[i][j-1])
        if  i < rows - 1:
            #right
            neighbours.append(grid[i+1][j])
        if i > 0:
            #left
            neighbours.append(grid[i-1][j])

        return neighbours
    
    def show(self, w, h):
        
        stroke(255)
        stroke_weight(5)
        y = self.i * h
        x = self.j * w 
        
        if self.up:
            line(x, y, x + w, y)
        if self.down:
            line(x + w, y + h, x, y + h)
        if self.left:
            line(x, y + h, x, y)
        if self.right:
            line(x + w, y, x + w, y + h)