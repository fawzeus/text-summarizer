#load packages
import spacy 
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

#create list of word list
stopwords = list(STOP_WORDS)

# calculate Word Frequency
def calculate_word_frequency(docx):
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


def calculate_sentences_score(docx,word_frequencies):
    sentence_list = [ sentence for sentence in docx.sents ]
    sentence_scores = {}  
    for sent in sentence_list:  
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if len(sent.text.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = word_frequencies[word.text.lower()]
                        else:
                            sentence_scores[sent] += word_frequencies[word.text.lower()]
    return sentence_scores


def summerize(sentence_scores):
    select_length=int(len(sentence_scores.keys())*0.7)
    select_length=max(select_length,2)
    summarized_sentences = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    final_sentences = [ w.text for w in summarized_sentences ]
    summary = ' '.join(final_sentences)
    return summary


def readingTime(docx):
    total_words_tokens =  [ token.text for token in docx]
    estimatedtime  = len(total_words_tokens)/200
    return '{} mins of reading'.format(round(estimatedtime))

def reduced_by(text,summary):
    return 'reduced by {} %'.format(round((len(text)-len(summary))/len(text)*100))
