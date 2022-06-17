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
        utterance = self.remove_stopwords()

        utterance = self.identify_keywords()

        # detokenize utterance and return sql
        utterance = TreebankWordDetokenizer().detokenize(utterance)
        self.request.data['sql_query'] = utterance
        return Response(self.request.data)

    def identify_keywords(self):
        with open('./api/nlidb_functions/tabledata.json', 'r') as f:
            data = json.load(f)
        

        print(data.keys())
        # first get table name from json file
        table_name = [word for word in self.utterance if word in data.keys()]
        self.sql_props['table_name'] = table_name

        # then get column name to be used as conditional
        json_data = data
        attr = [word for word in self.utterance if word in json_data.values()]
        self.sql_props['cond_attr'] = attr


    def remove_stopwords(self):
        tokens_without_sw = [word for word in self.utterance \
            if not word in stopwords.words('english')]

        return tokens_without_sw

    def construct(self):
        pass

    