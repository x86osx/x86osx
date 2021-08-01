import numpy as np
import matplotlib.pyplot as plt

labels=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

iris = np.loadtxt('iris.csv', skiprows=1, delimiter=',',
                 converters={4: lambda s: labels.index(s.decode())})

columns = ['SepalLength','SepalWidth', 'PetalLength', 'PetalWidth']

plt.plot(iris[:, :4])
plt.legend(columns)
plt.show()