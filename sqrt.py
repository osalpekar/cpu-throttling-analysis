import time
import math
import random

start_time = time.time()

x = 33429454235345324654575647586

for i in range(10000000):
    y = math.sqrt(x)
    x += 143

print time.time() - start_time, 's'