import numpy as np
import chaoskit as ck
from fun import sampler,response
from matplotlib import pyplot as plt

# %% Initialisation

order = 7
nbrPts = int(5e3)

# %% Polynomial Chaos

point = sampler(nbrPts)
poly = ck.gschmidt(order,point)
resp = response(point)

coef = ck.colloc(resp,poly,point)
model = ck.Expansion(coef,poly)

ck.save(model,'model')
mean,var = [model.mean,model.var]

# %% Figures

varMc = np.load('var.npy')
meanMc = np.load('mean.npy')

plt.figure(1)
for i in range(mean.shape[0]):
    plt.plot(mean[i],'C0')
    plt.plot(meanMc[i],'C1--')

plt.legend(['ChaosKIT','Monte Carlo'])
plt.ylabel('Mean')
plt.show()

plt.figure(2)
for i in range(var.shape[0]):
    plt.plot(var[i],'C0')
    plt.plot(varMc[i],'C1--')

plt.legend(['ChaosKIT','Monte Carlo'])
plt.ylabel('Variance')
plt.show()