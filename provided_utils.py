import pandas as pd
import sys
import os


import numpy as np
from tqdm.notebook import tqdm
import matplotlib.pyplot as plt
import matplotlib.patches as patches
# %matplotlib notebook
import torch
import os
from PIL import Image


def print_image_orignal (image_number, x_train, y_train):
    # Colormap for plotted bounding boxes 
    cmap = {0: "r", "Pedestrian": "g", "Cyclist": "b", "Van": "yellow", "Truck": "black"}

    # we deleted labels other than cars

    # Get boxes & classes for specific image
    im_number = image_number
    boxes = y_train["boxes"]
    classes = y_train["classes"]
    print(x_train.dtype)

    # Plot image
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.imshow(x_train[im_number, ...])
    ax.axis("off")
    plt.title(f"Image {im_number}")

    # Plot colored bounding boxes
    for bbox, cls in zip(boxes, classes):
        try:
            cl = cmap[cls]
        except:
            cl = cmap["Misc"]
        # Add rectangle (x,y), width, heigth
        height = bbox[2] - bbox[0]
        width = bbox[3] - bbox[1]
        rect = patches.Rectangle((bbox[1], bbox[0]), width, height, linewidth=1, edgecolor=cl, facecolor="none")
        ax.add_patch(rect)

    plt.show()
    plt.close(fig)

        # plt.text(
        #     bbox[1],
        #     bbox[0],
        #     s= int(cls),
        #     color="white",
        #     verticalalignment="top",
        #     bbox={"color": cmap[int(cls)], "pad": 0},
        # )