# import the existing word and sentence tokenizing
# libraries
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import nltk
from nltk.corpus import stopwords

def get_tokens(text):
    tokens = [t for t in text.split()]
    clean_tokens = tokens[:]
    sr = stopwords.words('english')
    for token in tokens:
        if token in stopwords.words('english'):
            clean_tokens.remove(token)

        if token in string.punctuation:
            clean_tokens.remove(token)

    return clean_tokens