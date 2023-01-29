import matplotlib.pyplot as plt

x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
y1 = [19, 18, 20, 23, 22, 24]
y2 = [17, 15, 18, 19, 18, 21]

plt.plot(x, y1, '-', x, y2, '--')
plt.legend(['Temp', 'Feel', 'y3', 'y4'])
plt.title('Warsaw, Poland')
plt.ylabel('Temp')
plt.xlabel('Days')

#plt.show()

plt.subplot(2, 1, 1)

x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
y1 = [19, 18, 20, 23, 22, 24]

plt.plot(x, y1, '-')
plt.legend(['Temp', 'y2', 'y3', 'y4'])
plt.title('Temp Warsaw, Poland')
plt.ylabel('Temp')
plt.xlabel('Days')

plt.subplot(2, 1, 2)

x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
y2 = [17, 15, 18, 19, 18, 21]

plt.plot(x, y2, '--', color=('red'))
plt.legend(['Feel', 'Feel', 'y3', 'y4'])
plt.title('Feels Warsaw, Poland')
plt.ylabel('Temp')
plt.xlabel('Days')

#plt.show()


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
wind = [82, 35, 74, 68, 63, 50]

plt.bar(days, wind)
plt.title('Warsaw, Poland')
plt.xlabel('Days')
plt.ylabel('Wind speed')

#plt.show()

vals = [2.7, 4.4, 3.4, 2.1, 2.9, 2]
labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
ex = [0, 0, 0, 0, 0, 0.5]
fig, ax = plt.subplots()
ax.pie(vals, explode = ex, labels=labels)
ax.axis('equal')

plt.show()