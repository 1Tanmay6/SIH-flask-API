from flask import Flask, request, jsonify
from similarity import pdf_to_text
from pysimilar import compare

def percentages(filename, file_path):
    
    if filename and file_path:
        pdf_to_text.text_extractor(filename, file_path)
        array_files = ['similarity/similarity_content/pcu-copy.txt', 'similarity/similarity_content/shounak.txt', 'similarity/similarity_content/tanmay.txt', 'similarity/similarity_content/wiki_2.txt', 'similarity/similarity_content/wiki_3.txt', 'similarity/similarity_content/wiki.txt']
        percentages = {
            'list': []
        }
        
        for file in array_files:
            temp_data = {
                'name': '',
                'percentage': 0
            }
            temp_data['name'] = file
            temp_data['percentage'] = round(float(compare(filename + '.txt', file, isfile=True) * 100), 2)
            percentages['list'].append(temp_data)

        return percentages 
    
    return 'Missing filename or file_path parameters.'
