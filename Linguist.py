import csv
import os


def supported_langs_file():
    if os.path.exists("Tesseract_Langs.txt"):
        return "Tesseract_Langs.txt"  # Text file containing every supported language code with full name
    else:
        print("The expected supported languages file is not in the directory. "
              "Tesseract_Langs.txt is available in the github repo")
        return None


def get_language_from_code(code):
    """
    Get the full-language name from an ISO 639-2/T code (tesseract-supported language code)

    Text file containing language codes is generated from tesseract's supported languages document:
    https://github.com/tesseract-ocr/tessdoc/blob/master/Data-Files-in-different-versions.md

    :return: Returns full language name if the code is matched, or returns the code in the case of no-match
    """
    file = supported_langs_file()

    l_dict = {}
    with open(file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for el in reader:
            key = el[0]
            name = el[1]
            l_dict[key] = name

    try:
        return l_dict[code]
    except KeyError:  # If no language name matches the code, just return the code
        return code


def show_codes():
    """
    Print a list of all tesseract-supported language codes next to the full language name
    """
    file = supported_langs_file()

    with open(file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        print("{:<20s}{:<40s}".format("CODE", "LANGUAGE"))
        for el in reader:
            print("{:<20s}{:<40s}".format(el[0], el[1]))


def language_string(language):
    """
    Generate a string containing a full language name given its code as used in the ocr process

    :param language: ISO 639-2/T code (tesseract-supported)
    :return: Full language name
    """
    if language is not None:  # If the user has specified a language, or multiple languages
        name_list = []
        codes = language.split('+')  # Multiple languages have the format "lang1+lang2+lang3"
        for language in codes:
            name = get_language_from_code(language)
            name_list.append(name)
        lang_name = ', '.join(name_list)

    else:  # Tesseract default
        lang_name = 'English'

    return lang_name
