from rest_framework.response import Response

from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

from .UtteranceEncoder import UtteranceEncoder

class KWEncoder(UtteranceEncoder):
    def __init__(self, request):
        UtteranceEncoder.__init__(self, request)

        self.__query_semantics__ = {'operator': '*',
                                'table_name': '',
                                'conditional': ''
                                }
        
    def process(self) -> Response:
    #
    # Main function of method 
    #
        UtteranceEncoder.remove_stopwords(self)

        self.identify_keywords()

        self.construct_sql()

        return Response(self.__request__.data)

    def identify_keywords(self) -> None:
    #
    # Extracts table name and table parameters from utterance
    #   
        corpus_root  = './api/nlidb/keywords'
        filelists = PlaintextCorpusReader(corpus_root, '.*')
        filelists.fileids()

        table_names = filelists.words('table_names.txt')
        param_names = filelists.words('table_parameters.txt')
        
        statement_tokens = word_tokenize(self.__request__.data['utterance'])

        tn_tokens = [word for word in statement_tokens if word in table_names]
        pn_tokens = [word for word in statement_tokens if word in param_names]

        self.__query_semantics__['table_name'] = TreebankWordDetokenizer().detokenize(tn_tokens)
        self.__query_semantics__['conditional'] = TreebankWordDetokenizer().detokenize(pn_tokens)


    def construct_sql(self) -> None:
        if (self.__query_semantics__['table_name'][-1] ==  's'):
            self.__query_semantics__['table_name'] = self.__query_semantics__['table_name'][:-1]
            
        op = self.__query_semantics__['operator']


        tn = 'nlidb_' + self.__query_semantics__['table_name'].lower()
        cp = self.__query_semantics__['conditional']

        self.__request__.data['sql_query'] = f'SELECT {op} FROM {tn} WHERE {cp} = 1'

