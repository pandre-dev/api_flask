from conexao import MongoConnection


class Produto():
    def __init__(self):
        self.conexao = MongoConnection()

    def read(self, query=None, projection=None):
        return self.conexao.db_read(query, projection)

    def save(self, json):
        self.conexao.db_save(json)

    def update(self, query, field):
        self.conexao.db_update(query, field)

    def remove(self, query):
        self.conexao.db_remove(query)
