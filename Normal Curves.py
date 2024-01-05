import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

#Plot between -20 and 20 with .001 steps
x_axis = np.arange(-20,20,0.01)

#Calculating mean and SDT
mean = statistics.mean(x_axis)
sd = statistics.stdev(x_axis)

plt.plot(x_axis,norm.pdf(x_axis,mean,sd))
plt.show()
