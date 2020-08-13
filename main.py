location = [0, 0, 0]

# Updates the global value of location[]
def xyz(axis, delta = 0):
# axis is the plane of movement: 
#   0 = x = east/west 
#   1 = y = north/south
#   2 = z = up/down
# delta is the change: +1, -3, etc

  global location
  if axis == 99:
    location = [0, 0, 0]
    print("going home")
  else:
    location[axis] = location[axis] + delta
  print(location)


def go(direction):
  global location

  cases = {
    "north" or "n": lambda: xyz(1, +1),
    "south": lambda: xyz(1, -1),
    "east": lambda: xyz(0, +1),
    "west": lambda: xyz(0, -1),
    "up": lambda: xyz(2, +1),
    "down": lambda: xyz(2, -1),
    "home": lambda: xyz(99),
  }
  cases.get(direction, lambda: print("Um, I don't understand\n"))()

while True:
  direction = input("Which direction? ")
  go(direction)
