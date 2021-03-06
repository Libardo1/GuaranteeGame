#######################
# Guarantee Game: 2 Signallers
# Version 1.1
# Uses Python 2.7.6
# Christopher Gandrud
# 21 July 2014
# MIT License
#######################

# Import packages
import random
import scipy as sp
import numpy as np
import math
import pandas

# Initialize Lists
XrealL= []
alphaL = []
GuaranteeL = []
UpmL = []
Us1L = []
Us2L = []
Signaler1L = []
Signaler2L = []

#### Create proportion of recoverable assets to all assets ####
# True value
alphaRange = np.random.uniform(0.65, 0.95, 1000)

# Set Signaller 1 wants lower amount than Signaller 2
S1Range = [-0.05, -0.15]
S2Range = [0.05, 0.15]

for alpha in alphaRange:
	for S1 in S1Range:
		for S2 in S2Range:

			# Expected value
			gammaHat = sp.mean(np.random.uniform(0.65, 0.95, 100000))

			# Find if alpha falls within
			# [gammaHat + 2*Signaler1, gammaHat + 2*Signaler2]
			Lower = gammaHat + (2 * S1)
			Upper = gammaHat + (2 * S2)

			if  Lower < alpha < Upper:
				guarantee = gammaHat
			else:
				guarantee = alpha

			# Find utilities
			Xreal = guarantee - alpha
			Upm = -(math.pow((0 - Xreal), 2))
			Us1 = -(math.pow((S1 - Xreal), 2))
			Us2 = -(math.pow((S2 - Xreal), 2))

			# Append to lists
			XrealL.append(Xreal)
			alphaL.append(alpha)
			GuaranteeL.append(guarantee)
			UpmL.append(Upm)
			Us1L.append(Us1)
			Us2L.append(Us2)
			Signaler1L.append(S1)
			Signaler2L.append(S2)

d = {
	'Xreal' : XrealL,
	'Alpha' : alphaL,
	'Guarantee' : GuaranteeL,
	'Upm' : UpmL,
	'Us1' : Us1L,
	'Us2' : Us2L,
	'Signaler1' : Signaler1L,
	'Signaler2' : Signaler2L
	}

# Create data frame
OutputData = pandas.DataFrame(d)

OutputData.to_csv('/git_repositories/GuaranteeGame/SimulatedData/SimData09_2014.csv')
