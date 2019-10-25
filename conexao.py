import pymongo
import jsonify

class MongoConnection():
    def __init__(self):
        try:
            self.client = pymongo.MongoClient("localhost", 27017)
            self.estoque = self.client["estoque"]
            self.produto = self.estoque["produto"]
            # Login padrão do MongoDB, database 'estoque' e collection 'produto'
        except Exception as e:
            print(f"Erro ao estabelecer conexão: {e}")

    def db_read(self, query=None, projection=None):
        try:
            leitura = str("")
            for prd in self.produto.find(query, projection):
                for key, value in prd.items():
                    leitura += "\n" + str(key) + ": " + str(value)
                leitura += "\n"
        except Exception as e:
            print(f"Erro ao ler registro: {e}")
        finally:
            return leitura

    def db_save(self, json):
        try:
            self.produto.insert_one(json)
        except Exception as e:
            print(f"db_save - Erro ao salvar registro: {e} \n {json}")

    def db_update(self, query, field):
        try:
            self.produto.update(query, field)
        except Exception as e:
            print(f"Erro ao atualizar registro: {e} \n {json}")

    def db_remove(self, query):
        try:
            self.produto.remove(query)
        except Exception as e:
            print(f"Erro ao excluir registro: {e} \n {json}")
