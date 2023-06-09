"""test."""
import numpy as np

print("hello world")


a = np.arange(6)
a2 = a[np.newaxis, :]
print(a2.shape)
