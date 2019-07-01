import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open("one.csv","r") as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    for row in plots :
        x.append((row[0]))
        y.append(float(row[1]))
plt.plot(x,y,label='loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('intresting graph')
plt.legend()
plt.show()
