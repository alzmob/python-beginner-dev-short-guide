import scipy
from matplotlib import pyplot as plt
import numpy as np
#get face image of panda from misc package
panda = scipy.misc.face()
#plot or show image of face
plt.imshow( panda )
plt.show()