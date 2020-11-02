import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def heatmap(matrix):

    fig, ax = plt.subplots()
    im = ax.imshow(matrix)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
            rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            text = ax.text(j, i, matrix[i, j],
                        ha="center", va="center", color="w")

    fig.tight_layout()
    plt.show()