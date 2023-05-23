import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([0, 2, 5, 32, 64, 127, 255], 
[482, 483, 483, 498, 828, 1630, 3255])
ax.scatter([0, 2, 5, 32, 64, 127, 255], 
[482, 483, 483, 498, 828, 1630, 3255])
plt.show()