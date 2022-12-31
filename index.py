import requests
import json

def requisicao(titulo):
    try:
        req = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=3366d4f6" + titulo)
        album = json.loads(req.text)
        return album
    except:
        print("Erro de conexão com a API")
        return None

def printar_detalhes(filme):
    print("Ano: ", filme["Year"])




sair = False


while not sair:
    op = input("Escreva o nome do filme ou digite SAIR para fechar: ")

    if op == "sair": 
        sair = True
    else: 
        filme = requisicao(op)
        if filme["Response"] == False:
            print("Filme não encontrado")
        else:
            printar_detalhes(op)  








