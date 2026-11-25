ARQUIVO = "usuarios.txt"
SEPARADOR = ";"

def carregar_usuario (): #a base do "read"//ler ou listar 
    usuarios = []
    try:
        with open(ARQUIVO, 'r', 'utf-8') as arquivo_lido:
          for linhas in arquivo_lido: #percorre o arquivo uma linha por vez; a cada 'linha' guarda texto da linha atual
               linhas = linha.strip()
               if linhas == "":
                continue #se a linha tiver vazia, passa pra proxima sem retornar ela    
               separando = linha.strip(SEPARADOR) #vai separar cada informação obtida por um ;
               if len(linhas) !=3:
                continue
               usuarios.append({

               "id": int(separando[0]),
               "nome": (separando[1]),
               "telefone":(separando[2])
               })
    except FileNotFoundError:
       pass
    except ValueError:
       print("Erro: o arquivo contém um ID inválido.")
    
             
