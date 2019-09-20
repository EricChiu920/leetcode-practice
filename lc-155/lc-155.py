class MinStack:
  def __init__(self):
    self.stack = []
    self.mins = []

  def push(self, x: int) -> None:
    self.stack.append(x)
    if len(self.mins) is 0 or x <= self.mins[-1]:
      self.mins.append(x)

    return None

  def pop(self) -> None:
    if len(self.stack) is not 0:
      ele = self.stack.pop()
      if ele is self.mins[-1]:
        self.mins.pop()

    return None

  def top(self) -> int:
    if len(self.stack) is not 0:
      return self.stack[-1]

  def getMin(self) -> int:
    if len(self.mins) is not 0:
      return self.mins[-1]

# Keep track of mins in a list