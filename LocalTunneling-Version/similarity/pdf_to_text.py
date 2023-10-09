from PyPDF2 import PdfReader
import re

def remove_special_characters(input_string):
    pattern = r'[^a-zA-Z0-9\s]'
    
    cleaned_string = re.sub(pattern, '', input_string)
    
    return cleaned_string


def text_extractor(filename, file_path):
    ext_pdf= '.pdf'
    reader = PdfReader(file_path + "/" + filename + ext_pdf)

    file = open(filename+'.txt', 'w')

    for i in range(0, len(reader.pages)):

        page = reader.pages[i]
        text = page.extract_text()
        
        cleaned_string = remove_special_characters(text)

        file.write(cleaned_string)
    return "File at Location: " + file_path + '\\' +filename + ".txt"
