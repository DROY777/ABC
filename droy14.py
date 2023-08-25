import matplotlib.pyplot as plt
import numpy as np
means =[20,35,30,35,27]
stds=[2,3,4,1,2]
indx=np.arange(len(means))
plt.bar(indx,means,color='cyan',label='means')
plt.bar(indx+0.25,stds,color='olive',label='stds')
plt.legend()
plt.show()
