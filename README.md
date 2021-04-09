# RealTime-OCR [Version1]
## Python 3.9
## Author: Nathan Aday / nraday1221@gmail.com
https://github.com/nathanaday/RealTime-OCR

### DESCRIPTION

Perform text detection in a variety of languages with your computer webcam using Google Tesseract OCR and OpenCV. 
This script achieves a real-time OCR effect by incorporating multi-threading.

<img src="https://user-images.githubusercontent.com/79942554/114243078-d37be180-9940-11eb-849c-29b606646bb8.jpg" width="500">

### USE

This a command-line script. The only required argument is a full path to the Tesseract executable from the Tesseract install (see DEPENDENCIES below for more info)

`python Main.py -t '<full_path_to_your_tesseract_executable>' [-c ] [-v] [-sv] [-l] [-sl]`


optional arguments:

  -h, --help         command-line argument help message
  
  -c  , --crop       crop OCR area in pixels (two vals required): width height
  
  -v , --view_mode   view mode for OCR boxes display (default=1)
  
  -sv, --show_views  show the available view modes and descriptions
  
  -l , --language    code for tesseract language, use + to add multiple (ex: chi_sim+chi_tra)
  
  -sl, --show_langs  show list of tesseract (4.0+) supported langs

required named arguments:
  -t , --tess_path   path to the cmd root of tesseract install (see docs for further help)


#### Crop

The crop area allows OCR to be performed on a smaller frame and therefore improves speed. A box is automatically drawn around the crop so it's clear where to position text for detection.

#### View Mode

This script implements four view modes, which stylize the way text is detected. To specify a view mode, use -v <int mode> after the Main.py call

- View mode 1: Draws boxes on text with >75 confidence level

<img src="https://user-images.githubusercontent.com/79942554/114243131-ebebfc00-9940-11eb-808e-51179cd4139e.gif" width="700">


- View mode 2: Draws red boxes on low-confidence text and green on high-confidence text

<img src="https://user-images.githubusercontent.com/79942554/114243144-f1e1dd00-9940-11eb-88e7-a32572ebacc1.gif" width="700">


- View mode 3: Color changes according to each word's confidence; brighter indicates higher confidence

<img src="https://user-images.githubusercontent.com/79942554/114243169-fc9c7200-9940-11eb-9788-dc6894cb9db9.gif" width="700">


- View mode 4: Draws a box around detected text regardless of confidence

<img src="https://user-images.githubusercontent.com/79942554/114243187-01f9bc80-9941-11eb-9384-3e2b983b2498.gif" width="700">


If no view mode is specified, the OCR will run with mode 1.

To see the view options and their descriptions in the command line, evoke -sv or --show_views


#### Language

The OCR can detect a variety of langauges since version 4+. A language can be specified by appending the Main.py call with "-l <language code>"

For example, to detect simplified Chinese, use:

`python Main.py -t '<full_path_to_your_tesseract_executable>' -l chi_sim`

Multiple languages can be simultaneously detected by appending the codes with '+'

To detect both simplified chinese and traditional chinese, use:

`python Main.py -t '<full_path_to_your_tesseract_executable>' -l chi_sim+chi_tra`

A list of all the languages codes can be printed in the command line by evoking '-sl'.

`python Main.py -t '<full_path_to_your_tesseract_executable>' -sl`

Note, the printed list of available langauges comes from the tesseract supported languages, which should be included in an up-to-date install, but evoking the lagnauge code will have no effect if the .traindata file for that language is nowhere in the data files.

If no language code is specified, the OCR defaults to English.




### DEPENDENCIES

This script requires 
- a Tesseract install
- the python wrapper for Teseract (pytesseract)
- OpenCV for python (CV2)
- Numpy

Instruction on how to install Tesseract on your OS are located here:

https://tesseract-ocr.github.io/tessdoc/Installation.html

To use the script, you will need the path to the exec file included in the Tesseract install, so note the install's location.

`Example (on a Homebrew install): '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'`


To install the Python wrapper for Tesseract, use:

`pip install pytesseract`

(See the pytesseract docs for further help.)[https://pypi.org/project/pytesseract/]


To install OpenCV for Python, use:

`pip install opencv-python`

(See the opencv-python docs for further help.)[https://pypi.org/project/opencv-python/]


For numpy, use:

 `pip install numpy`
 
 (See the numpy docs for further help.)[https://numpy.org/install/]
 
 
 Tesseract should come with .traindata files that supports a wide variety of foreign languages. In any case, the repo for language files can be found here:
 
 https://github.com/tesseract-ocr/tessdata
 


### PROGRAM CONTENTS

Main.py
- Command-line argparser and call to the OCR stream

OCR.py
- All classes and functions for multi-threaded text detection and webcam display

Linguist.py
- A few functions for handling the language codes and converting them to full language names (reads from Tesseract_Langs.txt)

Tesseract_Langs.txt
- Text file for every supported language code and the language's full name

README.md

requirements.txt


### RESOURCES AND EXTENDED USE
...

### SUPPORT
...
