import matplotlib.pyplot as plt
import numpy as np
import csv
from . import multiarray
from . import overrides
from . import cbook, rcsetup
from . import core


x=[]
y=[]

with open('ultradata.csv','r') as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
plt.plot(x,y,marker='o')        
plt.xlabel('x')
plt.ylabel('y')
plt.title('epic graph')
plt.legend()
plt.show()
