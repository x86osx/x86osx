import numpy as np
import matplotlib.pyplot as plt

f = open ('iris.csv')

line = f.readline()
features = line.strip().split(',')[:4]

data = []
for line in f:
    l = line.strip().split(',')
    l[0] = float(l[0]) #sepal_length
    l[1] = float(l[1]) #sepal_width
    l[2] = float(l[2]) #petal_length
    l[3] = float(l[3]) #petal_width

    if l[4] == 'Iris-setosa' : l[4] = 0
    elif l[4] == 'Iris-versicolor' : l[4] = 1
    else : l[4] = 2 #Iris-virginica

    data.append(l)
f.close()

iris = np.array(data)

print(iris.shape)

columns = ['SepalLength','SepalWidth', 'PetalLength', 'PetalWidth']

plt.plot(iris[ : , :4])
plt.legend(columns)
plt.show()