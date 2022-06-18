from rest_framework.response import Response

from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

import json

class SQLEncoder:
    sql_props = {
        'table_name': '',
        'column': '*',
        'cond_attr': '',
        'cond_value': ''
    }

    def __init__(self, _request) -> None:
        # Tokenize the utterance for later
        self.utterance = word_tokenize(_request.data['utterance'])
        self.request = _request

    def encode_utterance(self):
        # first stopwords are removed
        self.utterance = self.remove_stopwords()

        self.identify_keywords()

        self.construct()

        # detokenize utterance and return sql
        self.utterance = TreebankWordDetokenizer().detokenize(self.utterance)
        return Response(self.request.data)

    def identify_keywords(self):
        with open('./api/nlidb_functions/tabledata.json', 'r') as f:
            data = json.load(f)
    
        # first get table name from json file
        for word in self.utterance:
            for x in data.values():
                for s in x['synonyms']:
                    if word == s:
                        table_name = x['synonyms'][0]
                        break
                
                for c in x['attributes']:
                    if word == c:
                        attr = c
                        break
    
    def clean_table_name(self, name) -> str:
        name = name.lower()
        if name[-1]  == 's':
            name = name[:-1]
        
        self.__query_semantics__['table_name'] = name
        return name

    def identify_WHERE(self):
        attr = self.sql_props['cond_attr'] 
        print('hi')
        if attr == 'admitted' or attr == 'working':
            return ' WHERE '+ attr + '=1'

        return ''

    def construct(self):
        column = self.sql_props['column']
        table_name = 'nlidb_' + self.sql_props['table_name']
        WHERE_clause = self.identify_WHERE()

        self.request.data['sql_query'] = f'SELECT {column} FROM {table_name}' + WHERE_clause

    