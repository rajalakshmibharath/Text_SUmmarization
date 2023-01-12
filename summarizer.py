import spacy

from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest

def summarization(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    words = [word.text for word in doc]
    stopwords = STOP_WORDS
    punctuations = punctuation
    word_frequency = {}

    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuations:
                if word.text.lower() not in word_frequency.keys():
                    word_frequency[word.text.lower()]= 1
                else:
                    word_frequency[word.text.lower()] +=1

    max_frequency = max(word_frequency.values())
    
    for word in word_frequency.keys():
        word_frequency[word]= word_frequency[word]/max_frequency

    sent_token = [sent for sent in doc.sents]

    
    sent_frequency= {}

    for sent in doc.sents:
        for word in sent:
            if word.text.lower() in word_frequency.keys():
                if sent not in sent_frequency.keys():
                    sent_frequency[sent] = word_frequency[word.text.lower()]
                else:
                    sent_frequency[sent] += word_frequency[word.text.lower()]

    max_sentence = int(len(sent_token)*0.3)
    summary = nlargest(max_sentence,sent_frequency, sent_frequency.get)
    fs = [i.text for i in summary]
    summary = ''.join(fs)

    return summary,doc, len(summary), len(text)
