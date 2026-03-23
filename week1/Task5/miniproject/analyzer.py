import streamlit as st
import re

class TextAnalyzer:
    #Class to handle text processing and analysis logic
    
    def __init__(self, raw_text):
        # Initializing the object with the text data
        self.raw_text = raw_text

    def get_word_count(self):
        #Returns the total number of words
        return len(self.raw_text.split())

    def get_char_count(self):
        #Returns the total number of characters - including spaces
        return len(self.raw_text)

    def get_sentence_count(self):
        #Returns total sentences based on punctuation
        # Handles . ! and ? as sentence terminators
        sentences = re.split(r'[۔!?]+', self.raw_text)
        return len([s for s in sentences if s.strip()])

    def get_frequent_words(self, top_n=5):
        #Returns the most frequent words in the text
        words = self.raw_text.lower().split()
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Sort by frequency and return top N
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:top_n]