import matplotlib.pyplot as plt

figure = plt.figure()

ax = figure.add_subplot(1, 1, 1)
x = [0,1,2,3,4]
y = [4,1,3,5,2]

ax.plot(x, y)

plt.show()