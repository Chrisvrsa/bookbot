# A with block opens a file in python. its a file object.
# use .read() to read the file contents into a string.
# path must be relative to the text file
import string

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def convert_text(book_text):
    array_of_words = book_text.split()
    return len(array_of_words)

def text_converter(book_text):
    lowercase_text = book_text.lower()
    word_count_dictionary = {}

    for character in lowercase_text:
        #if the character is in the dictionary, increment the value at that key (character) by one. 
        if character in word_count_dictionary:
            word_count_dictionary[character] += 1
            
        else:
            #if the character is not in the dictionary, create a new entry with the value of one.
            word_count_dictionary[character] = 1

    return word_count_dictionary



