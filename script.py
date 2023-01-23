#!/usr/bin/python

import sys
import pandas as pd
import matplotlib.pyplot as plt

print("Number of arguments: %i arguments" % len(sys.argv))
print("Argument List:" + str(sys.argv))

data = pd.read_csv("meteo.csv", delimiter=",")
precipitation = data.iloc[:, 1]

plt.plot(precipitation)
plt.xlabel('Observation')
plt.ylabel('Precipitation')
plt.show()
