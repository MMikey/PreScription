from rest_framework.response import Response

from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer


class UtteranceEncoder:

    def __init__(self, request) -> None:
        self.__request__ = request
        self.__statement_tokens__ = word_tokenize(self.__request__.data['utterance'])

    def remove_stopwords(self):
        tokens_without_sw = [word for word in self.__statement_tokens__ if not word in stopwords.words()]

        self.__statement_tokens__ = TreebankWordDetokenizer().detokenize(tokens_without_sw)

        handler500 = 'error'
    