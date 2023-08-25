import matplotlib.pyplot as plt
import numpy as np
info=['gold','silver','bronze','total']
India=[26,20,20,66]
plt.ylabel("Medal type")
plt.xlabel("Medal count")
plt.title("india's Medal Tally in commonwealth 2018")
X=range(len(info))
plt.barh(X,India,color=['gold','silver','brown','black'])
plt.show()