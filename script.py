#!/usr/bin/python

import sys
import pandas as pd
import matplotlib.pyplot as plt

print("Number of arguments: %i arguments" % len(sys.arg))
print("Argument List:" + str(sys.argv))

data = pd.read_csv(sys.argv[1], delimiter=";")

precipitation = data["y"]

plt.plot(precipitation)
plt.xlabel('Observation')
plt.ylabel('Precipitation')
plt.show()
