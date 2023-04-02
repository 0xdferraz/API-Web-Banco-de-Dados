import json
from flask import Flask, request

class BANCO_DE_DADOS():
    def __init__(self, arq_json):
        self.bd_json = arq_json
        self.bd_conteudo = None
    
    def ler_bd(self):
        try:
            # Lendo arquivo JSON do Banco de Dados
            with open(self.bd_json, 'r') as arq_json:
                dados = arq_json.read()
                self.bd_conteudo = json.loads(dados)
        except:
            # Criando arquivo JSON caso não exista
            with open(self.bd_json, 'w') as arq_json:
                self.bd_conteudo = {"usuarios": []}
        return True

    def post(self, novo_usuario):
        # Verificando se usuário já existe no Banco de Dados
        for usuario in self.bd_conteudo["usuarios"]:
            if novo_usuario['cpf'] == usuario['cpf']:
                return {'Mensagem': "Usuario ja cadastrado no Banco de Dados"}
            
        # Adicionando o usuário caso não esteja cadastrado
        with open(self.bd_json, 'w') as arq_json:
            self.bd_conteudo["usuarios"].append(novo_usuario)
            json.dump(self.bd_conteudo, arq_json)
            return {'Mensagem': "Usuario adicionado com Sucesso!"}
    
    def get(self, cpf):
        for usuario in self.bd_conteudo["usuarios"]:
            if cpf == usuario['cpf']:
                return json.dumps({'Usuario': usuario})
            
        return {'Erro': "Usuario nao cadastrado no Banco de Dados"}



def main():
    app = Flask(__name__)
    BD = BANCO_DE_DADOS('banco_de_dados.json')
    BD.ler_bd()

    @app.route('/usuarios', methods=['POST'])
    def post_usuario():
        novo_usuario = request.json
        return BD.post(novo_usuario)

    @app.route('/usuarios/<cpf>', methods=['GET'])
    def get_usuario(cpf):
        return BD.get(cpf)

    app.run(debug=True)

main()