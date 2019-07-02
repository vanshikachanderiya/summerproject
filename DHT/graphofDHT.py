import matplotlib.pyplot as plt
import datetime
import sys
import csv
with open('data4.csv','r') as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    print(plots)
    for rows in plots :
        #x.append(tempreature)
        #y.append(humidity)
#plt.plot(x,y,label='loaded from file')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('interesting graph')
#plt.legend()
#plt.show()
