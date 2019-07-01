import numpy as np
import matplotlib.pyplot as plt
slices = [7,2,2,13]
activities =['sleeping','eating','working','playing']
index = np.arange(len(activities))
def plot_barh_x():
    index = np.arange(len(activities))
    plt.bar(index,slices)
    plt.xlabel('x',fontsize=5)
    plt.ylabel('y',fontsize=5,rotation=30)
    plt.title('intresting graph')
    plt.show()
