from conexao import MongoConnection


class Produto():
    def __init__(self):
        self.conexao = MongoConnection()

    def read(self, query=None, projection=None):
        return self.conexao.db_read(query, projection)

    def save(self, json):
        self.conexao.db_save(json)

    def update(self, nome, edit):
        '''
        :param nome: nome a ser editado no BD, transforma em um JSON para a query
        :param edit: campo total pós-edição, transforma em um JSON para o field
        '''
        self.conexao.db_update({"nome":nome}, {"$set":edit})

    def remove(self, nome):
        '''
        :param nome: nome a ser excluído no BD, transforma em um JSON para a query
        '''
        self.conexao.db_remove({"nome":nome})
