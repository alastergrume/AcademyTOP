# from collections import Counter
# import socket
# import time

# def f():
#     time.sleep(0.001)
#     # Return IP address.
#     return socket.gethostbyname("localhost")

# ip_addresses = [f() for _ in range(10000)]
# print(Counter(ip_addresses))

# Define the square task.

import ray

ray.init()

@ray.remote
def square(x):
    return x * x

# Launch four parallel square tasks.
futures = [square.remote(i) for i in range(4)]

# Retrieve results.
print(ray.get(futures))
# -> [0, 1, 4, 9]