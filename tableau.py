
import random

class Tableau(object):
  # values = List of all cells of the tableau concatenated, top row first
  # row_lengths = List of row lengths
  def __init__(values, row_lengths):
    self.values = values
    self.row_lengths = row_lengths

  def __str__(self):
    row_strings = []
    total = []
    for length in self.row_lengths:
      cells = self.values[total:total + length]
      row_strings.append(''.join('[%s]' % (val,) for val in cells))
    return '\n'.join(row_strings)

  def is_standard(self):
    return False

def is_corner(index, row_lengths):
  total = 0
  for length in row_lengths:
    total += length
    if total == index:
      return True
  return False

def hook_number(index, row_lengths):
  row, col = coordinates(index, row_lengths)

  cells_to_right = row_lengths[row] - col
  cells_below = len(row_lengths) - row

  return cells_to_right + cells_below - 1

def coordinates(index, row_lengths):
  row = 0
  for length in row_lengths:
    if index < length:
      return (row, index)
    index -= length
  return None

def index_for_coordinates(row, col, row_lengths):
  return sum(row_lengths[:row]) + col

def pick_biggest_cell(row_lengths):
  # Pick random cell
  n = sum(row_lengths)
  cell = random.randint(0, n - 1)

  while not is_corner(cell, row_lengths):
    print "Cell is", cell, 'with rows', row_lengths
    # Do a hook walk
    # Current cell is index 0
    # Cells to right are 1, 2, ...
    # Cells below are ..., h -1, h
    delta = random.randint(1, hook_number(cell, row_lengths) - 1)
    row, col = coordinates(cell, row_lengths)

    # Walk to right
    if delta < row_lengths[row] - col:
      new_row, new_col = row, col + delta
    # Walk down
    else:
      rows_walked = delta - (row_lengths[row] - col)
      new_row, new_col = row + rows_walked, col

    cell = index_for_coordinates(new_row, new_col, row_lengths)

  # Duplicate the row lengths to avoid mutation
  picked_row, _ = coordinates(cell, row_lengths)
  new_row_lengths = list(row_lengths)

  # Compute reduced row lengths
  rows = len(new_row_lengths)
  new_row_lengths[picked_row] -= 1
  if new_row_lengths[rows - 1] == 0:
    # Picked last element of last row
    # Need to chop off last row
    new_row_lengths = new_row_lengths[:rows - 1]

  return pick_biggest_cell(new_row_lengths) + [cell]

def random_standard_tableau(row_lengths):
  value_locations = pick_biggest_cell(row_lengths)
  cells = []
  for val, cell in enumerate(value_locations):
    cells.insert(cell, val + 1)

  return Tableau(cells, row_lengths)

if __name__ == '__main__':
  print random_standard_tableau([4, 2, 1])
