import numpy as np
data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(data)
print(data.ndim)
print(data.shape)
print(data.size)
print(data[0, 0])
print(data[1, 2])
print(data[0])
print(data[:, 1])
data[0, 1] = 999
print(data)
data[1] = [1, 2, 3]
print(data)
print(data[0:2])
print(data[0:2, 1:3])
print(data + 10)
print(data * 2)
print(np.sum(data))
print(np.mean(data))
print(np.min(data))
print(np.max(data))
print(np.sum(data, axis=0))
print(np.sum(data, axis=1))