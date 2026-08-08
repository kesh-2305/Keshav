"""marks = [45, 67, 89, 34, 76, 90, 55]
n = len(marks)

total = 0
 
for i in range(n):
    total += marks[i]
mean = total/n

print("mean of marks is ", mean)"""

import numpy as np
from statistics import mean , median, stdev
data = [45, 67, 89, 34, 76, 90, 55]
arr = np.array(data)
print("mean ", mean(arr))
print("median ", median(arr))
print("standard deviation ", stdev(arr))