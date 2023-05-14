
import cv2
import numpy as np
import pyautogui
import pytesseract

def printImg(x, y, w, h):
    img =  pyautogui.screenshot(
        region=(x, y, w, h))
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

def OCR(image):
    text : str = pytesseract.image_to_string(image)
    return text
