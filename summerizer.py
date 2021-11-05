#load packages
import spacy 
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation


#create list of word list
stopwords = list(STOP_WORDS)

# calculate Word Frequency
def calculate_word_frequency(docx):
    nlp = spacy.load('en')
    word_frequencies = {}
    for word in docx:
        if word.text not in stopwords:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    return word_frequencies

#normalize word frequency
def normalize(word_frequencies):
    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)


def calculate_sentences_score(docx):
    sentence_list = [ sentence for sentence in docx.sents ]
