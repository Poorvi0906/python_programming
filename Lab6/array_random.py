import numpy as np 

t3 = np.random.randint(0,10,(4,5))
np.random.seed(10)
print(t3)
print("-------------")
print(np.sort(t3,axis=0))