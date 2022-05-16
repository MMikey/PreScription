
from os import lseek
from rest_framework.response import Response

from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

class ProcessRequest():
    def __init__(self, request):
        self.__request__ = request

        self.query_semantics = {'operator': '*',
                                'table_name': '',
                                'conditional': ''
                                }
        
            

    def process(self):
        # First discard all stopwords from the question
        self.remove_stopwords()

        # next get array of all keywords
        self.identify_keywords()

        self.construct_sql()

        return Response(self.__request__.data)


    def remove_stopwords(self):
        utterance = self.__request__.data['utterance']

        statement_tokens = word_tokenize(utterance)

        tokens_without_sw = [word for word in statement_tokens if not word in stopwords.words()]

        self.__request__.data['translated_statement'] = TreebankWordDetokenizer().detokenize(tokens_without_sw)
        
        handler500 = 'error'
    
    def identify_keywords(self):
        utterance = self.__request__.data['utterance']
        statement_tokens = word_tokenize(utterance)
        
        corpus_root  = './api/nlidb/keywords'

        filelists = PlaintextCorpusReader(corpus_root, '.*')

        filelists.fileids()

        table_names = filelists.words('table_names.txt')
        param_names = filelists.words('table_parameters.txt')

        tn_tokens = [word for word in statement_tokens if word in table_names]

        pn_tokens = [word for word in statement_tokens if word in param_names]

        self.query_semantics['table_name'] = TreebankWordDetokenizer().detokenize(tn_tokens)
        self.query_semantics['conditional'] = TreebankWordDetokenizer().detokenize(pn_tokens)


    def construct_sql(self):
        op = self.query_semantics['operator']
        tn = self.query_semantics['table_name']
        cp = self.query_semantics['conditional']

        self.__request__.data['sql_statement'] = f'SELECT {op} FROM {tn} WHERE {cp} = 1'

