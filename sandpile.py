import numpy as np
from collections import defaultdict
from operator import itemgetter
import sys

class Sandpile:
    CELL_LIMIT = 3

    def __init__(self, num_grains):
        # Use dict instead of 2D array so grid can grow infinitely
        self.grid = defaultdict(int)
        self.grid[(0, 0)] = num_grains

    def topple(self):
        try:
            # Find a cell larger than CELL_LIMIT, and distribute to neighbours
            (i, j) = next(filter(lambda k: self.grid[k] > self.CELL_LIMIT, self.grid))
            self.grid[(i, j)] -= self.CELL_LIMIT + 1
            self.increment_neighbours(i, j)
        except StopIteration:
            return

    def increment_neighbours(self, i, j):
        neighbours = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        for x, y in neighbours:
            self.grid[(i+x, j+y)] += 1

    def stable(self):
        return all(x <= self.CELL_LIMIT for x in self.grid.values())

    # Convert dict into 2D array
    def getgrid(self):
        min_x = min(self.grid.keys(), key=itemgetter(0))[0]
        min_y = min(self.grid.keys(), key=itemgetter(1))[1]
        max_x = max(self.grid.keys(), key=itemgetter(0))[0]
        max_y = max(self.grid.keys(), key=itemgetter(1))[1]
        matrix = np.zeros((max_x - min_x + 1, max_y - min_y + 1), dtype=int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i, j] = self.grid[(i + min_x, j + min_y)]
        return matrix


num_grains = 100
try:
    num_grains = int(sys.argv[1])
except Exception:
    pass

print("Using {} grain(s)".format(num_grains))

sp = Sandpile(num_grains)

while not sp.stable():
    sp.topple()

print(sp.getgrid())

#colours = [(41, 128, 185), (22, 160, 133), (142, 68, 173), (52, 73, 94)]
#from PIL import Image
#height = 512
#data = np.zeros((height, height, 3), dtype=np.uint8)
#data[10, 10] = [255, 0, 0]
#img = Image.fromarray(data, 'RGB')
#img.show()
