import math
sine=[]
for x in range(0,51):
    sine.append(math.cos(((2*math.pi)/50)*x))
plt.plot(sine,color='red')
plt.show()
