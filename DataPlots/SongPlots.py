'''
Generate plots of song data for presentation
'''

import json
import matplotlib.pyplot as plt

# read song data
with open("data.json") as f:
    data = json.load(f)


# generate tempo plot
tempo_vals = [song["tempo"] for song in data]

plt.hist(tempo_vals, edgecolor = "grey", color = "pink")
plt.title("Tempo Values for Top 500 Songs of 2022", fontsize = 20)
plt.xlabel("Tempo (bpm)", fontsize = 14)
plt.ylabel("Number of Songs", fontsize = 14)
plt.show()



# generate energy level plot
energy_vals = [song["energy"] for song in data]

plt.hist(energy_vals, edgecolor = "grey", color = "pink")
plt.title("Energy Values for Top 500 Songs of 2022", fontsize = 20)
plt.xlabel("Energy Level (0 to 1)", fontsize = 14)
plt.ylabel("Number of Songs", fontsize = 14)
plt.show()