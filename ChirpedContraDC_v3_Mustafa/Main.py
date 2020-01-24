from Modules import *
from ChirpedContraDC_v3 import *

# Chirp
w1 = [.55e-6, .56e-6]
w2 = [.43e-6, .44e-6]
p = [324e-9, 326e-9]
wr = [1530e-9, 1600e-9] # wvl range to plot

device = ChirpedContraDC(N=2500, a=10, w1=w1, w2=w2, period=p, wvl_range=wr, resolution=100, N_seg=100)
device.simulate()
device.displayResults()