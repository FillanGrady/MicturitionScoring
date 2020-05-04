import pyautogui
import keyboard
import pytesseract
import os
import cv2
from PIL import Image
import numpy as np


def key_press(f):
    print("hi")
    image = pyautogui.screenshot(region=(300, 300, 200, 200))
    image.show()
    gray = cv2.cvtColor(np.float32(image), cv2.COLOR_BGR2GRAY)
    # check to see if we should apply thresholding to preprocess the
    # image

    gray = cv2.medianBlur(gray, 3)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    f.write("%s,%s%s" % (text, "0", os.linesep))


if __name__ == "__main__":
    output_csv = r"/home/fillan/Downloads/Output.csv"
    with open(output_csv, "w") as f:
        keyboard.add_hotkey('k', key_press, args=f)
        keyboard.wait('esc')