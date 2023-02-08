import matplotlib.pyplot as plt
import random


N = 8424
L = 8 + 4 + 2 + 4
probabilities = []
y=[]


count = 0
for i in range(1, N+1)
    if random.radint(1,L)==2:
        count+= 1
     probabilities = count/i
    probabilities.append(probabilities)
    y.append(i)
    print(probabilities)
plt.plot(probabilities,y)
plt.xlabel("Probability of getting 2")
plt.ylabel("Number of Tosses")
plt.title('Probability v/s number of tosses')
plt.show()
