import pdfminer

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from io import StringIO

from pdfminer.high_level import extract_pages
from pdfminer.high_level import extract_text

import glob
import re
import os
import shutil

MAX_TITLE_LENGTH = 30

def print_pdfminer_version() :
    print(pdfminer.__version__)

def file_search():
    fileList = glob.glob("./src/*.pdf")
    if not fileList:
        print("pdf not exists")
    else :
        print(fileList)
        return fileList
    
print_pdfminer_version()

output_string = StringIO()
def main():
    
    
    for FILE_NAME in file_search():
        FILE_NAME_LIST = FILE_NAME.split('/')
        for file_name in FILE_NAME_LIST:
            print(file_name)
        FILE_NAME_OUTPUT = FILE_NAME.replace('src', 'output')
        shutil.copy(FILE_NAME, FILE_NAME_OUTPUT)
        
        text = extract_text(FILE_NAME,password = "",maxpages = 1)#page1 extract
        tmp = re.sub('\(cid:\d+\)', '',text)#remove (cid:*)
        tmp2 = tmp.lstrip('\n')#remove \n from left
        tmp3 = tmp2.splitlines()#split by \n
        tmp4 = tmp3[0][0:MAX_TITLE_LENGTH]
        title = tmp4.rstrip('\n')
        print("TITLE = " + title)
        
        PDFTitled = FILE_NAME_OUTPUT.replace(FILE_NAME_LIST[2],title+'.pdf')
        os.rename(FILE_NAME_OUTPUT,PDFTitled) 
        #rename
        
        
        
        
main()
    
print(output_string.getvalue())