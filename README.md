# RealTime-OCR [Version1]
## Python 3.9
## Author: Nathan Aday / nraday1221@gmail.com
https://github.com/nathanaday/RealTime-OCR

### DESCRIPTION

Perform text detection in a variety of languages with your computer webcam using Google Tesseract OCR and OpenCV. 
This script achieves a real-time OCR effect by incorporating multi-threading.

Requires Tesseract to be installed (see info below). Tesseract is free and easy to install on Mac, Windows, and Linux.

Note that the frame display can take some time to pop up. After running the file with command line arguments, please be patient for a little bit and report any crashes/bugs to me.


### DETAILS

An OpenCV video stream runs in a dedicated thread, so it's always reading live frames from the webcam and storing the most recent in memory as a class attribute. The video display can access these frames and show them in real-time. Meanwhile, pytesseract OCR has its own dedicated class, running in a dedicated thread, and it simply grabs the most recent frame from the video stream class, processes it, and returns the detected text when it is finished processing. Without any form of multi-threading or multiprocessing, a frame display loop would have to wait for the OCR text detection to complete analysis before showing a new frame, creating a large bottleneck for most implementations. Multi-threading improves the processes significantly by allowing the video stream to run in real-time while the OCR works in the background. Boxes and detected text are dispalyed as they are updated by the OCR thread. One limitation is that the OCR is still limited in processing speed and will not return a bounding box and detected text for every frame from the video stream, but for ordinary applications where the camera has several seconds to analyze stable text this lag is managable. 

This script is easily modifiable to work with other camera sources, image types, and image processing methods since it is an implementation of the OpenCV video stream.

### USE

This a command-line script. The only required argument is a full path to the Tesseract executable from the Tesseract install (see DEPENDENCIES below for more info)

`python Main.py -t '<full_path_to_your_tesseract_executable>' [-c ] [-v] [-sv] [-l] [-sl] [-s]`


optional arguments:

  -h, --help         command-line argument help message
  
  -c  , --crop       crop OCR area in pixels (two vals required): width height
  
  -v , --view_mode   view mode for OCR boxes display (default=1)
  
  -sv, --show_views  show the available view modes and descriptions
  
  -l , --language    code for tesseract language, use + to add multiple (ex: chi_sim+chi_tra)
  
  -sl, --show_langs  show list of tesseract (4.0+) supported langs
  
   -s, --src.        SRC video source for video capture

required named arguments:
  -t , --tess_path   path to the cmd root of tesseract install (see docs for further help)


#### Crop

The crop area allows OCR to be performed on a smaller frame and therefore improves speed. A box is automatically drawn around the crop so it's clear where to position text for detection.

#### View Mode

This script implements four view modes, which stylize the way text is detected. To specify a view mode, use -v <int mode> after the Main.py call

<img src="https://user-images.githubusercontent.com/79942554/114243131-ebebfc00-9940-11eb-808e-51179cd4139e.gif" width="700">

_(View mode 1: Draws boxes on text with >75 confidence level)_

<br />



<img src="https://user-images.githubusercontent.com/79942554/114243144-f1e1dd00-9940-11eb-88e7-a32572ebacc1.gif" width="700">

_(View mode 2: Draws red boxes on low-confidence text and green on high-confidence text)_

<br />



<img src="https://user-images.githubusercontent.com/79942554/114243169-fc9c7200-9940-11eb-9788-dc6894cb9db9.gif" width="700">

_(View mode 3: Color changes according to each word's confidence; brighter indicates higher confidence)_

<br />



<img src="https://user-images.githubusercontent.com/79942554/114243187-01f9bc80-9941-11eb-9384-3e2b983b2498.gif" width="700">

_View mode 4: Draws a box around detected text regardless of confidence_

<br />


If no view mode is specified, the OCR will run with mode 1.

To see the view options and their descriptions in the command line, evoke -sv or --show_views


#### SRC Video Source

In the case of multiple camera ports, the src for the desired video input can be specified with the -s command-line arguemnt. Without specification, the src defaults to 0, which for most users is a built-in webcam.

Using SRC source 0:

`python Main.py -t '<full_path_to_your_tesseract_executable>' -s 0`

Using SRC source 1:

`python Main.py -t '<full_path_to_your_tesseract_executable>' -s 1`

#### Language

Tesseract can detect a variety of langauges since version 4+. A language can be specified to the OCR by appending the Main.py call with "-l <language code>"

For example, to detect simplified Chinese use:

`python Main.py -t '<full_path_to_your_tesseract_executable>' -l chi_sim`

Multiple languages can be simultaneously detected by appending the codes with '+'. To detect both simplified chinese and traditional chinese, use:

`python Main.py -t '<full_path_to_your_tesseract_executable>' -l chi_sim+chi_tra`

A list of all language codes can be printed in the command line by evoking '-sl'.

`python Main.py -t '<full_path_to_your_tesseract_executable>' -sl`

Note, the printed list of available langauges comes from the tesseract supported languages, which should be included in an up-to-date install. However, evoking the lagnauge code at runtime will have no effect if the .traindata file for that language is nowhere in your Tesseract files.

If no language code is specified, the OCR defaults to English.

#### Image Capture and Quit

While running an OCR stream, push "c" to capture the current frame and save as a .jpeg to the working directory. A capture will also print the current detected text to the command line:


![OCR 2021-04-09 at 13:06:35-5](https://user-images.githubusercontent.com/79942554/114278245-b51af200-99e3-11eb-835c-cad26dd7295f.jpg)

`RealTime-OCR user$ REAL TIME OCR with pytesseract and CV2 “Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.”
OCR 2021-04-09 at 13:06:35-5.jpg`


![OCR 2021-04-09 at 12:59:54-11](https://user-images.githubusercontent.com/79942554/114278250-bba96980-99e3-11eb-85cf-0c27ca3d997a.jpg)

`RealTime-OCR user$ 实时 OCR 跟 pytesseract, CV2 优美 胜 于 丑陋 ， 显 明 胜 于 隐 含 。 简单 胜 于 复杂 ， 复 杂 胜 于 繁复 。 扁平 胜 于 ， 稀 胜 于 密集 。 可 读 性 会 起 作用 。
OCR 2021-04-09 at 12:59:54-10.jpg`



### DEPENDENCIES

This script requires:
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

[See the pytesseract docs for further help.](https://pypi.org/project/pytesseract/)


To install OpenCV for Python, use:

`pip install opencv-python`

[See the opencv-python docs for further help.](https://pypi.org/project/opencv-python/)


For numpy, use:

 `pip install numpy`
 
 [See the numpy docs for further help.](https://numpy.org/install/)
 
 
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

This script was written with customizability in mind. It's easy to add custom view modes, edit the pre-processing frames for the OCR, or customize the output displayed in the video capture. These changes can be made in OCR.py. To add custom command line arguments, see Main.py. 

OpenCV is an incredbily robust computer vision package. Because this script already imports CV2, the OCR core could be swapped for CV2's facial recognition features, boundary detection, etc. and still achieve the seamless video display from multi-threading.

Tesseract has two additional data sets that can be configured: a [fast dataset](https://github.com/tesseract-ocr/tessdata_fast), and a [best dataset](https://github.com/tesseract-ocr/tessdata_best).

The fast data will speed up the OCR process, but at the cost of accuracy.

THe best data is trained to produce more accurate detection, but at the cost of speed.


### SUPPORT

Questions and bugs can be posted on the project's [github page](https://github.com/nathanaday/RealTime-OCR) or emailed to nraday1221@gmail.com


