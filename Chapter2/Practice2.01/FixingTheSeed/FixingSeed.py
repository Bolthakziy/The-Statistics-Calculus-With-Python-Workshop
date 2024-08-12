import numpy as np

print(np.random.random(7))
print(np.random.random(7))
print()
print("Above two lists are different.")
print()
print()

np.random.seed(5)
print(np.random.random(7))
np.random.seed(5)
print(np.random.random(7))
print()
print("Above two lists are same.")
print("Because the seed is fixed!!!")
print()
print()
