import sys
import cv2
import numpy as np


ASCII_SYMBOLS = [
    "#",   # darkest
    "&",
    "@",
    "%",
    "*",
    "+",
    "-",
    ";",
    ",",
    "."    # brightest
]
THRESHOLDS = [0, 25, 50, 75, 100, 125, 150, 175, 200, 250]

len_symbols = len(ASCII_SYMBOLS)

def print_ascii_art(array):
    for row in array:
        for value in row:
            print(ASCII_SYMBOLS[int(value % len_symbols)], end="")
        print("")

def generate_ascii(img):
    height, width = img.shape
    new_height = height // 16
    new_width = width // 6

    resized_img = cv2.resize(img, (new_width, new_height))
    #cv2.imshow('Resized img', resized_img)
    #cv2.waitKey(0)
    thresholded_img = np.zeros(resized_img.shape)

    for i, THRESHOLD in enumerate(THRESHOLDS):
        thresholded_img[resized_img > THRESHOLD] = i
    return thresholded_img


if __name__ == "__main__":
    path = './assets/korean-flag.jpg'
    img = cv2.imread(path, 0)
    ascii_art = generate_ascii(img)
    print_ascii_art(ascii_art)

