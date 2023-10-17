import numpy as np
Z = []

for x in range(0,1001):
    for y in range(0,1001):
        prob=[x/1000, y/1000]
        for i in range(2,101):
            n=1-(2*prob[i-1]+prob[i-2])/3
            prob.append(n)
        Z.append(prob[100])
print(len(Z))
k=0
for i in Z:
    if i==0.5:
        k=k+1
print(k)