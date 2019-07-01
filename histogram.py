import numpy as np
import matplotlib.pyplot as plt
np.random.seed(19680801)
mu, sigma=100,15
x = mu + sigma*np.random.randn(10000)
n,bins,patches = plt.hist(x,50,density=1,facecolor='g',alpha=0.75)
plt.xlabel('my data',fontsize=14,color='red')
plt.ylabel('probability')
plt.title(r'$\sigma_i=15$')
plt.text(60,.025,r'$\mu=100,\ \sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()
