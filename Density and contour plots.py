import matplotlib.pyplot as plt
plt.style.use(&#39;seaborn-white&#39;)
import numpy as np
Visualizing a Three-Dimensional Function
def f(x, y):
return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z, colors=&#39;black&#39;);
