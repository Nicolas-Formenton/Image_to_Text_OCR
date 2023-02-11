# Image to Text OCR

### Project Overview
This project is a script that captures a screenshot of a selected area and extracts the text from the image using optical character recognition (OCR) with the help of the Tesseract library and the OpenCV computer vision library.

- ``` Obs: There's a simple version of this code, the 'img_text_recognizer.ipynb' and the only thing you have to do is add an input file on the folder an name it `image.png` ```

##### Libraries and versions used
Library         | Version | Installation Command
--------------- | ------- | --------------------
Python          | 3.x     | -
OpenCV-Python   | 4.x     | pip install opencv-python
pytesseract     | 0.3.7   | pip install pytesseract
pyautogui       | 0.9.50  | pip install pyautogui
numpy           | 1.19.x  | pip install numpy
keyboard        | 0.13.5  | pip install keyboard

### Project description
It captures a screenshot of a selected area and converts it to grayscale. 
It then applies thresholding to binarize the image and applies median blur to remove noise from the image. 
The image is then passed through the Tesseract OCR engine to extract the text. 
The extracted text is printed out in the terminal or command prompt and automatically copied to the user's clipboard.

### Running the script
1. Clone the repository to your local machine
    ```bash
    git clone https://github.com/Nicolas-Formenton/Text_to_Image_OCR.git
    ```
2. Change into the directory of the cloned repository
    ```bash 
    cd img_to_text_ocr.py
    ```
3. Install the required libraries
    ```py
    python -m pip install -r requirements.txt
    ```
4. Run the script
    ```py
    python img_to_text_ocr.py
    ```
5. Select the area of your screen to extract text from by having your cursor pointer on two spots. 
    - After the first spot being given, point your mouse cursor to the second spot and then press `q` to continue.

6. The extracted text will be displayed in the terminal and automatically copied to your clipboard.

7. Press `q` to quit the program.

8. If you wanna build the python script into an executable file, you can do these two steps when inside the folder:
    ```bash
    pip install pyinstaller
    pyinstaller --onefile .\img_to_text_ocr.py
    ```

### Code Explanation
The code is written in Python and uses the following libraries:

Library         | Usage   |
--------------- | ------- | 
OpenCV          | Used for image processing tasks, such as converting the image to grayscale and applying thresholding.| 
PyTesseract     | Used for optical character recognition (OCR) and extracting text from images.   |
PyAutoGui       | Used for taking screenshots and getting the mouse click positions. |
NumPy           |Used to convert the screenshot to a NumPy array. |
Keyboard        | Used to check if the q key is pressed.  |


#### Configurations to the OCR that can be made
1. Change the language
    - `-l = 'language'`
2. Change the PSM (Page Segmentation Mode)
    - `--psm n`
        | n | Explanation |
        | - | ----------- |
        | 1 | Orientation and script detection (OSD) only. |
        | 2 | Automatic page segmentation with OSD. |
        | 3 | Fully automatic page segmentation, but no OSD or OCR |
        | 4 | Assume a single column of text of variable sizes. |
        | 5 | Assume a single uniform block of vertically aligned text. |
        | 6 | Assume a single uniform block of text. |
        | 7 | Treat the image as a single text line. |
        | 8 | Treat the image as a single word. |
        | 9 | Treat the image as a single word in a circle. |
        | 10 | Treat the image as a single character. |
        | 11 | Sparse text. Find as much text as possible in no particular order. |
        | 12 | Sparse text with OSD. |
        | 13 | Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific. |

 
3. Change the OEM (Optical Character Recognition Engine Mode)
    - `oem = n`
        | n | Mode |
        | - | ---- |
        | 0 | Legacy engine only. |
        | 1 | Neural nets LSTM engine only. |
        | 2 | Legacy + LSTM engines. |
        | 3 | Default, based on what is available. |



Obs: In this particular project, I'm using English language, so I've downloaded a trained data from Tesseract's repo so I can use 'oem = 2'. Here's their repo with trained datas that you can add to your own tesseract instalation folder: https://github.com/tesseract-ocr/tessdata.


###### Future Work
###### - This script could be converted into a browser extension, for example a Chrome extension, with the help of React or JavaScript. The extracted text could then be added to the browser's clipboard for easy copying and pasting.