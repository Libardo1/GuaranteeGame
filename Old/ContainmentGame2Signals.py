#######################
# Containment Game: 2 Signallers
# Version 1
# Uses Python 2.7.2
# Christopher Gandrud
# 5 December 2012
#######################

# Import packages
import random
import scipy as sp
import numpy as np
import math
import pandas

# Initialize Lists
OmegaL = []
GuaranteeL = []
UpmL = []
Us1L = []
Us2L = []
Signaler1L = []
Signaler2L = []

#### Create proportion of recoverable assets to all assets ####
# True value
OmegaRange = np.random.uniform(-0.074, 0.85, 1000) 

# Set Signaller 1 wants lower amount than Signaller 2
S1Range = [-0.05, -0.15]
S2Range = [0.05, 0.15]

for omega in OmegaRange:
	for S1 in S1Range:
		for S2 in S2Range:

			# Expected value 
			gammaHat = sp.mean(np.random.uniform(-0.074, 0.85, 100000)) 

			# Find if omega falls within 
			# [gammaHat + 2*Signaler1, gammaHat + 2*Signaler1]
			Lower = gammaHat + (2 * S1)
			Upper = gammaHat + (2 * S2) 

			if  Lower < omega < Upper and omega >= 0:
				guarantee = gammaHat
			elif omega < 0:
				guarantee = 0
			else:
				guarantee = omega

			# Find utilities

			Xreal = guarantee - omega

			Upm = -(math.pow((0 - Xreal), 2))

			Us1 = -(math.pow((S1 - Xreal), 2))
			Us2 = -(math.pow((S2 - Xreal), 2))

			# Append to lists

			OmegaL.append(omega)
			GuaranteeL.append(guarantee)
			UpmL.append(Upm)
			Us1L.append(Us1)
			Us2L.append(Us2)
			Signaler1L.append(S1)
			Signaler2L.append(S2)

d = {'Omega' : OmegaL,
	'Guarantee' : GuaranteeL,
	'Upm' : UpmL,
	'Us1' : Us1L,
	'Us2' : Us2L,
	'Signaler1' : Signaler1L,
	'Signaler2' : Signaler2L
	}

# Create data frame
OutputData = pandas.DataFrame(d)

OutputData.to_csv('/git_repositories/ContainmentGame/SimulatedData/SimData.csv')


