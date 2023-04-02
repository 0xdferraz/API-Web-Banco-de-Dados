import requests
import sys

def get(cpf):
    url = 'http://localhost:5000/usuarios/' + str(cpf)
    response = requests.get(url)

    if response.status_code == 200:
        if response.content.strip():
            data = response.json()
        return data
    else:
        return ('Erro na requisicao: ' + str(response.status_code))


def post(cpf, nome, data_nascimento):
    novo_usuario = {
    'cpf': cpf,
    'nome': nome,
    'data_nascimento': data_nascimento
    }

    url = 'http://localhost:5000/usuarios'

    response = requests.post(url, json=novo_usuario)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return ('Erro na requisicao: ' + str(response.status_code))

def main():
    try:
        if sys.argv[1] == "--post" or sys.argv[1] == "-p":
            cpf = sys.argv[2]
            nome = sys.argv[3]
            data_nascimento = sys.argv[4]

            solicitacao_post = post(cpf, nome, data_nascimento)
            print(solicitacao_post)

        elif sys.argv[1] == "--get" or sys.argv[1] == "-g":
            cpf = sys.argv[2]
            
            solicitacao_get = get(cpf)
            print(solicitacao_get)            

        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("""
            Trabalho Prático Banco de Dados - Parte 1 ( GITHUB_LINK )
            Implementação de Banco de Dados de Usuários, contendo CPF como chave primária, Nome e Data de Nascimento, e suas requisições POST e GET. 
            
            Uso (POST): python main.py --post ou -p <cpf> <nome> <data de nascimento>

            Uso (GET): python main.py --get ou -g <cpf>

            <cpf> : inteiro
            <nome> : string
            <data de nascimento> : string ("00/00/00")
            """)
        
        else:
            print("Algo deu errado, verifique os argumentos do Script. Para mais informações utilize o argumento --help ou -h")
            return False
        
    except:
        print("Algo deu errado, verifique os argumentos do Script. Para mais informações utilize o argumento --help ou -h")
        return False

main()