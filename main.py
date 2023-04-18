from astropy.io import ascii
import matplotlib.pyplot as plt
import numpy as np
data = ascii.read('spectrum.csv')

# print(data['col1'])
highest_value = 0
for i, entry in enumerate(data):
    if entry[1] > highest_value:
        highest_value = entry[1]
        pos = i
shifted_freq = data[pos][0]
c = 300000000
rest_freq = 1420.405751768
source_v = (c*rest_freq/shifted_freq)-c
print(source_v)

plt.plot(data['col1'],data['col2'])
plt.title('title name')
plt.xlabel('Frequency')
plt.ylabel('Relative Power')
plt.show()
