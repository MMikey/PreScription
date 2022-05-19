import json

def DatabaseExtractor():
    def __init__(self, models:list) -> None:
        self.__models__ = models
        self.__table_data__ = {}

        self.get_tbl_names()
        self.get_tbl_params()
        self.save_to_file()

    def save_to_file(self):
        open('table_data.json', 'x')
        with open('table_data.json', 'w') as fp:
            json.dump(self.__table_data__, fp)

    def get_tbl_params(self):
        i = 0
        for x in self.__table_data__:
            self.__table_data__[x] = self.__models__[i].__meta.get_fields()
            i += 1

    def get_tbl_names(self):
        for model in self.__models__:
            self.__table_data[model.__meta.db_table] = []

    