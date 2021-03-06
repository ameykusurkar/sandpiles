# sandpiles

## What is a sandpile?

A [sandpile](https://en.wikipedia.org/wiki/Abelian_sandpile_model) is a grid, with the value in each cell representing the number of 'grains' in that cell.
A cell can have at most 3 grains, so if it has more, it gives a grain to each of its 4 neighbours (this is called *toppling*).
We keep toppling until no cell has more than 3 grains.

## Fractal Designs

If a start with a grid with `n` grains in the middle cell, 0 in the other cells, and topple the sandpile until it is stable, it forms a fractal pattern.
We can then map number of grains to a colour and visualise the pattern. We get better results for larger `n`.

_An example can be found [here](https://github.com/ameykusurkar/sandpiles/blob/master/sandpile_images/sandpile1000000.png)_.
