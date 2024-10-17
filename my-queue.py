# Implemnting a queue
from collections import deque

# People lining up
gift_queue = deque(["Ian", "Christine", "Francis"])
print(gift_queue)
gift_queue.append("Lameck")
print(gift_queue)
gift_queue.append("Loreen")
print(gift_queue)
gift_queue.append("Margaret")
print(gift_queue)
gift_queue.append("Mildred")
print(gift_queue)

# Start serving people
gift_queue.popleft()
print(gift_queue)

gift_queue.popleft()
print(gift_queue)

gift_queue.popleft()
print(gift_queue)

gift_queue.popleft()
print(gift_queue)