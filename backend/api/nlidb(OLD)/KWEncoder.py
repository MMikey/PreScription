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
                                'conditional': '',
                                'value': ''
                                }

        self.__sql_templates__ = {
            'template_one': 'SELECT {} FROM {} WHERE {} = 1',
            'template_two': 'SELECT {} FROM {} WHERE {} LIKE {}',
            'template_three': 'SELECT COUNT({}) FROM {}',
            'default': 'SELECT {} FROM {}',
        }
        
    def process(self) -> Response:
    #
    # Main function of method 
    #
        UtteranceEncoder.remove_stopwords(self)

        self.identify_keywords()

        self.construct_sql()

        return Response(self.__request__.data)

    def clean_table_name(self, name) -> str:
        name = name.lower()
        if name[-1]  == 's':
            name = name[:-1]
        
        return 'nlidb_' + name


    def identify_keywords(self) -> None:
    #
    # Extracts table name and table parameters from utterance
    #   
        # Loops through corpus of db keywords to store as list
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

        self.__query_semantics__['table_name'] = self.clean_table_name(tbl_name)

    def identify_conditional_values(self):
        pass

    def select_template(self):
        tn = self.__query_semantics__['table_name']
        cp = self.__query_semantics__['conditional']

        if tn == 'nlidb_patient':
                if cp == 'admitted':
                    return self.__sql_templates__['template_one']
        elif tn == 'nlidb_staff':
                if cp == 'is_working':
                    return self.__sql_templates__['template_one']
                else: 
                    return self.__sql_templates__['template_three']
        elif tn == 'nlidb_appointment':
                pass
        elif tn == 'nlidb_treatment':
                if cp == 'name':
                    return self.__sql_templates__['template_two']

        return self.__sql_templates__['default']

        

    def construct_sql(self) -> None:    
        op = self.__query_semantics__['operator']
        tn = self.__query_semantics__['table_name']
        cp = self.__query_semantics__['conditional']
        value = self.__query_semantics__['value']

        template = self.select_template()

        print(template)
        self.__request__.data['sql_query'] = template.format(op,tn,cp)

