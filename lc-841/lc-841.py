from collections import deque

class Solution:
  def canVisitAllRooms(self, rooms) -> bool:
    table = [False] * len(rooms)
    table[0] = True
    counter = 1
    queue = deque(rooms[0])
    
    while len(queue) > 0:
      key = queue.popleft()
      if table[key] is False:
        table[key] = True
        counter += 1
        for new_key in rooms[key]:
          queue.appendleft(new_key)

    for room in table:
      if room is False: return False
    
    return counter == len(rooms)