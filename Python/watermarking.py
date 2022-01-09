
"""
Created on Sun Dec 12 13:56:25 2021

@author: satouani
"""


import cv2
import numpy as np

def transparentOverlay(src, overlay, x, y, scale=1):
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image

    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if y + i >= rows or x + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[y + i][x + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[y + i][x + j]
    return src


