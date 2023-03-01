
#import necessary libraries 
from googletrans import Translator 
from gtts import gTTS 

import os
import PyPDF2
from gtts import gTTS
from PyPDF2 import PdfFileReader

# need to brew install translate locally

# #Selecting the book in epub format
# book_file = input("Enter the path to your epub book: ")

# #Selecting the language to translate the book
# language = input("Enter the language to translate the book into: ")


# #open the book file 
# book_file = open('~/Desktop/dirt_test.txt', 'r') 

# #read the content of the book 
# book_content = book_file.read() 

# #prompt the user to enter the target language 
# target_language = input('Enter target language: ') 

# #initialize the translator 
# translator = Translator() 

# #translate the book 
# translated_book = translator.translate(book_content, dest = target_language).text 

# #create a text to speech object 
# tts = gTTS(translated_book, lang = target_language) 

# #save the translated audio book 
# tts.save('translated_book.mp3') 

# #close the book file 
# book_file.close() 

################
import os
import PyPDF2
from gtts import gTTS
from PyPDF2 import PdfFileReader

def run(book_path=None, book_name=None, language=None):
    book_path, book_name, language = setup(book_path, book_name, language)
    convert_book(book_path, book_name)
    translate_and_create_audio_book(book_name, language)

def setup(book_path=None, book_name=None, language=None):
    #Selecting the book in epub format
    if book_path is None:
        book_path = input("Enter the path to your epub book: ")
    if book_name is None:
        book_name = input("Enter the name of your translated book: ")

    #Selecting the language to translate the book
    if language is None:
        language = input("Enter the language to translate the book into: ")
    return book_path, book_name, language

def convert_book(book_path=None, book_name=None):

    #Creating a PDF file from the epub book
    os.system('ebook-convert' + f"input_file={book_path}/{book_name}.epub" + f"output_file=~/Desktop/books/{book_name}.txt")


def translate_book(book_name, language):
    #Opening the PDF file
    pdf_file = open(f"ADE.txt", 'rb')
    book_content = pdf_file.read() 
    
    #initialize the translator 
    translator = Translator()
    for page in pdf_file:
        
    
    #translate the book 
    translated_book = translator.translate(book_content, dest = language).text 

    def create_audiobook(#create a text to speech object 
    tts = gTTS(translated_book, lang = language) 

    #Reading the PDF file
    # pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    #Creating the audio file
    audio_file = gTTS(text = pdf_file.read(), slow = False)

    #Saving the audio file
    audio_file.save(f"~/Desktop/{book_name}.mp3")

    #Playing the audio file
    os.system('start book_audio.mp3'))

# 
run("~/Desktop/", "ADE", 'french')
# translate_and_create_audio_book("ADE", 'french')

