import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

# OPTIONAL: Save our plot to a PNG file
# plt.savefig('./plot-output.png')

# Show our graph
plt.show()
