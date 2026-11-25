arquivo_usuarios = "usuarios.txt" #aqui que os nomes ficarão salvos
separador = ";" #separa os campos em cada linha do arquivo

def carregar_usuarios (): #função que lidará com os usuários
    usuarios = [] #vai criar uma lista vazia que recebe um dicionário por usuário lido
    try:
            with open(arquivo_usuarios, 'r') as arquivo_lido: 
                for linha in arquivo_lido: #percorre o arquivo uma linha por vez
                    linha = linha.strip() #remove os espaços, deixando a linha da lista desse modo: [1;ana;ana@gmail.com;24]
                    if not linha:
                        continue #se a linha estiver vazia após o .strip(), parte pra próxima
                    partes = linha.split(separador) #ao invés de cada informação recebida durante o while True ocupar uma linha cada, essa função vai fazer com que eles fiquem na mesma linha, separados por ";"
                    if len(partes) !=4: #se a linha nãop constar todos os 4 itens principais, pula a linha
                         continue
                    usuarios.append({
                         "id": int(partes[0]),
                         "nome": partes[1],
                         "email": partes[2],
                         "idade": partes[3]
                    })
    except FileNotFoundError:
         pass #caso o try falhar por causa do arquivo não existir, ele "pass"; ou seja, o código cai aqui e não acontece nada, apenas devolve uma lista vazia.
    return usuarios #retorna a lista pra quem chamou a função, recebendo: [1;ana;ana@gmail.com;24]

def salvar_usuarios (): #pegar cada usuário da lista criada antes e escrever uma linha no arquivo
     with open (arquivo_usuarios, 'w') as arquivo_novo:
          for identacao in arquivo_novo:
               linha = f"{identacao['id']}{separador}{identacao['nome']}{separador}{identacao['email']}{separador}{identacao['idade']}\n"
               arquivo_novo.write(linha)