import numpy as np


data = np.load("/Users/rishi/MoodySound/dataset/train/I_Had_To_Do_It_0s_matrix.npy")

print(data.size)

count = 0
for row in data:
    c = 0
    for column in row:
        c+= 1
    count += 1

print(count)
print(c)

