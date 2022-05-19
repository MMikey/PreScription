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

    def clean_parameters(self):
        if (self.__query_semantics__['table_name']):
            pass

    def clean_table_name(self, name) -> str:
        name = name.lower()
        if name[-1]  == 's':
            name = name[:-1]
        
        self.__query_semantics__['table_name'] = name
        return name


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

        tbl_name = TreebankWordDetokenizer().detokenize(tn_tokens)
        self.__query_semantics__['conditional'] = TreebankWordDetokenizer().detokenize(pn_tokens)

        self.clean_table_name(tbl_name)


    def construct_sql(self) -> None:
        name = self.clean_table_name(self.__query_semantics__['table_name'])
            
        op = self.__query_semantics__['operator']
        tn = 'nlidb_' + name
        cp = self.__query_semantics__['conditional']

        self.__request__.data['sql_query'] = f'SELECT {op} FROM {tn} WHERE {cp} = 1'

