import requests
import json

def lista_de_filmes(titulo):
    lista = []
    for i in range(1, 101):
        try:
            print('Pesquisando em pagina:', i)
            url = "http://www.omdbapi.com/?i=tt3896198&apikey=3366d4f6&s=" + titulo + '&type=movie&page=' + str(i)
            req = requests.get(url)
            resposta = json.loads(req.text)
            if resposta['Response'] == 'True':
                for filme in resposta['Search']:
                    tit = filme['Title']
                    ano = filme['Year']
                    string = tit + ' (' + ano + ')'
                    lista.append(string)
            else:
                print('Fim das paginas')
                break
        except:
            print('Conexao falhou')
    return lista      
        
sair = False

while not sair:
    op = input("Escreva o nome do filme ou digite SAIR para fechar: ")

    if op == "sair": 
        sair = True
    else: 
        lista_filmes = lista_de_filmes(op)
        print("Filmes encontrados: ", len(lista_filmes))
        for filme in lista_filmes:
            print(filme)
