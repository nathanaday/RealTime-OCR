import argparse
import os

import OCR
import Linguist


def main():
    """
    Handles command line arguments and begins the real-time OCR by calling ocr_stream().
    A path to the Tesseract cmd root is required, but all other params are optional.

    Example command-line use: python3 Main.py -t /usr/local/Cellar/tesseract/4.1.1/bin/tesseract

    optional arguments:
      -h, --help         show this help message and exit
      -c  , --crop       crop OCR area in pixels (two vals required): width height
      -v , --view_mode   view mode for OCR boxes display (default=1)
      -sv, --show_views  show the available view modes and descriptions
      -l , --language    code for tesseract language, use + to add multiple (ex: chi_sim+chi_tra)
      -sl, --show_langs  show list of tesseract (4.0+) supported langs

    required named arguments:
      -t , --tess_path   path to the cmd root of tesseract install (see docs for further help)
    """
    parser = argparse.ArgumentParser()

    # Required:
    requiredNamed = parser.add_argument_group('required named arguments')

    requiredNamed.add_argument('-t', '--tess_path',
                               help="path to the cmd root of tesseract install (see docs for further help)",
                               metavar='', required=True)

    # Optional:
    parser.add_argument('-c', '--crop', help="crop OCR area in pixels (two vals required): width height",
                        nargs=2, type=int, metavar='')

    parser.add_argument('-v', '--view_mode', help="view mode for OCR boxes display (default=1)",
                        default=1, type=int, metavar='')
    parser.add_argument('-sv', '--show_views', help="show the available view modes and descriptions",
                        action="store_true")

    parser.add_argument("-l", "--language",
                        help="code for tesseract language, use + to add multiple (ex: chi_sim+chi_tra)",
                        metavar='', default=None)
    parser.add_argument("-sl", "--show_langs", help="show list of tesseract (4.0+) supported langs",
                        action="store_true")
    parser.add_argument("-s", "--src", help="SRC video source for video capture",
                        default=0, type=int)

    args = parser.parse_args()

    if args.show_langs:
        Linguist.show_codes()

    if args.show_views:
        print(OCR.views.__doc__)

    tess_path = os.path.normpath(args.tess_path)
    # This is where OCR is started...
    OCR.tesseract_location(tess_path)
    OCR.ocr_stream(view_mode=args.view_mode, source=args.src, crop=args.crop, language=args.language)


if __name__ == '__main__':
    # To run in IDE (instead of commamnd line), comment out main() and uncomment the block below:
    main()

    # tess_path =  r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Windows example
    # tess_path = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'  # MAC example
    # view_mode = 1
    # source = 0
    # crop = [100, 100]
    # language = "en"
    # OCR.ocr_stream(view_mode=view_mode, source=source, crop=crop, language=language)
