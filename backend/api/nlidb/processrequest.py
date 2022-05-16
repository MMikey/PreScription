from rest_framework.response import Response

from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

class ProcessRequest():
    def __init__(self, request):
        self.__request__ = request

    def process(self):
        # First discard all stopwords from the question
        self.remove_stopwords()

        # next get array of all keywords

        return Response(self.__request__.data)


    def remove_stopwords(self):
        nl_statement = self.__request__.data['nl_question']
        statement_tokens = word_tokenize(nl_statement)

        tokens_without_sw = [word for word in statement_tokens if not word in stopwords.words()]

        self.__request__.data['translated_statement'] = TreebankWordDetokenizer().detokenize(tokens_without_sw)
        
        handler500 = 'error'
    
    def identify_keywords(self):
        nl_statement = self.__request__.data['nl_question']
        statement_tokens = word_tokenize(nl_statement)
        
        corpus_root  = './keywords'

        filelists = PlaintextCorpusReader(corpus_root, '.*')

        filelists.fileids()

        table_names = filelists.words('keywords.txt')

        kw_tokens = [word for word in statement_tokens if word in table_names]

        self.__request__.data['translated_statement'] = TreebankWordDetokenizer().detokenize(kw_tokens)
