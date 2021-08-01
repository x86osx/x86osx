import numpy as np
import matplotlib.pyplot as plt

f = open ('iris.csv')

line = f.readline()
features = line.strip().split(',')[:4]

labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']

data = []
for line in f:
    l = line.strip().split(',')

    l[:4] = [float(i) for i in l[:4]]

    l[4] = labels.index(l[4])

    data.append(l)
f.close()

iris = np.array(data)

print(iris.shape)

columns = ['SepalLength','SepalWidth', 'PetalLength', 'PetalWidth']

plt.plot(iris[ : , :4])
plt.legend(columns)
plt.show()