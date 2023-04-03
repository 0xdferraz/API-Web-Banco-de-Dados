import requests
import sys

def get(cpf, url):
    url = url + '/' + str(cpf)
    response = requests.get(url)

    if response.status_code == 200:
        if response.content.strip():
            data = response.json()
        return data
    else:
        return ('Erro na requisicao: ' + str(response.status_code))


def post(cpf, nome, data_nascimento, url):
    novo_usuario = {
    'cpf': cpf,
    'nome': nome,
    'data_nascimento': data_nascimento
    }

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

            try:
                if sys.argv[5] == "--ip" or sys.argv[5] == "-i":
                    url = 'http://' + sys.argv[6] + ':5000/usuarios'
                
            except:
                url = 'http://localhost:5000/usuarios'

            solicitacao_post = post(cpf, nome, data_nascimento, url)
            print(solicitacao_post)

        elif sys.argv[1] == "--get" or sys.argv[1] == "-g":

            cpf = sys.argv[2]

            try:
                if sys.argv[3] == "--ip" or sys.argv[3] == "-i":
                    url = 'http://' + sys.argv[4] + ':5000/usuarios'
            except:
                url = 'http://localhost:5000/usuarios'
            
            solicitacao_get = get(cpf, url)
            print(solicitacao_get)

        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("""
            Trabalho Prático Banco de Dados - Parte 1 ( https://github.com/0xdferraz/API-Web-Banco-de-Dados )

            Implementação de Banco de Dados de Usuários, contendo CPF como chave primária, Nome e Data de Nascimento, e suas requisições POST e GET. 
            
            Uso POST:
                localhost: python main.py --post ou -p <cpf> <nome> <data de nascimento>

                AWS: python main.py --post ou -p <cpf> <nome> <data de nascimento> --ip ou -i <ip da instancia EC2>

            
            Uso GET:
                localhost: python main.py --get ou -g <cpf>

                AWS: python main.py python main.py --get ou -g <cpf> --ip ou -i <ip da instancia EC2>

            Tipos de Dados:
                <cpf> : inteiro
                <nome> : string
                <data de nascimento> : string ("00/00/00")
                <ip> : string ("0.0.0.0")
            """)
        
        else:
            print("Algo deu errado, verifique os argumentos do Script. Para mais informações utilize o argumento --help ou -h")
            return False
        
    except Exception as e:
        print(e)
        print("Algo deu errado, verifique os argumentos do Script. Para mais informações utilize o argumento --help ou -h")
        return False

main()