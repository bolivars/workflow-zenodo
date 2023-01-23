#!/usr/bin/python

import sys
import pandas as pd
import matplotlib.pyplot as plt

print("Number of arguments: %i arguments" % len(sys.arg))
print("Argument List:" + str(sys.argv))

data = pd.read_csv(sys.argv[1], delimiter=";")
time = range(1, len(data("y")))
data.plot(x = time, y="y")
plt.xlabel('Time')
plt.ylabel('Precipitation')
plt.show()