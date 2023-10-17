prob=[0, 0]

for i in range(2,80):
    n=1-(2*prob[i-1]+prob[i-2])/3
    prob.append(n)

print(prob)