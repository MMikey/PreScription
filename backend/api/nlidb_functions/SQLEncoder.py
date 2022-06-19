from rest_framework.response import Response

from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

import json

class SQLEncoder:
    

    def __init__(self, _request) -> None:
        self.sql_props = {
        'table_name': '',
        'column': '*',
        'cond_attr': '',
        'cond_value': ''
    }
        # Tokenize the utterance for later
        self.utterance = word_tokenize(_request.data['utterance'])
        self.request = _request

    def encode_utterance(self):
        # first stopwords are removed
        self.utterance = self.remove_stopwords()

        self.identify_keywords()

        self.construct()

        return Response(self.request.data)

    def remove_stopwords(self):
        tokens_without_sw = [word for word in self.utterance if not word in stopwords.words()]
        return tokens_without_sw

    
    def identify_keywords(self):
        with open('./api/nlidb_functions/tabledata.json', 'r') as f:
            data = json.load(f)
    
        # first get table name from json file
        for word in self.utterance:
            for x in data.values():
                for s in x['synonyms']:
                    if word == s:
                        self.sql_props['table_name'] = x['synonyms'][0]
                        break
                
                for c in x['attributes']:
                    if word == c:
                        self.sql_props['cond_attr'] = c
                        break
    
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

    