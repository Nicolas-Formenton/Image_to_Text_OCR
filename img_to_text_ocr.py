import cv2
import pytesseract
import pyautogui
import keyboard
import time
import numpy as np
import pyperclip

def capture_screenshot(x1, y1, x2, y2):
    return pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))

def extract_text_from_image(screenshot):
    
    # Load the image
    image = np.array(screenshot)

    # If needed resizing to try better recognition, uncomment the line below
    image = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)

    # Apply thresholding to binarize the image
    _, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    text = ""

    # Use the pytesseract library to recognize the text
    ocr_config = '-l eng --oem 2 --psm 11'
    recognized_text = pytesseract.image_to_string(thresholded, config = ocr_config)

    text += recognized_text

    return text

print("Press 'q' to quit")
while True:
    if keyboard.is_pressed("q"):
        break
    print("Click first point to define screenshot area or press 'q' to quit...")
    time.sleep(2)
    x1, y1 = pyautogui.position()
    print(f"First point: ({x1}, {y1})")
    
    while True:
        if keyboard.is_pressed("q"):
            break
    print("Move the mouse to define second point or press 'q' to quit...")
    x2, y2 = pyautogui.position()
    print(f"Second point: ({x2}, {y2})")

    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

# Get the screenshot area based on the two points
area = (x1, y1, x2 - x1, y2 - y1)
img = pyautogui.screenshot(region=area)
img.show()

# Call the function to extract text from an image
extracted_text = extract_text_from_image(img)
pyperclip.copy(extracted_text)

# Print the extracted text
print("\nExtracted text:\n", extracted_text)