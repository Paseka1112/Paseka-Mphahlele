import random
import numpy as np

NTests = 200
mu = 0.0
var = 1.0
err = 0.0
NPs = 1000
for i in range(NTests):
    x = np.random.normal(mu, var, NPs)
err += (x.mean()-mu)**2
print("MSE: ", err/NTests)
