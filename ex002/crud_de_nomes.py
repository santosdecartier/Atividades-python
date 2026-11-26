ARQUIVO = "nomes.txt"

def ler_nomes():
    try:
        with open(ARQUIVO, 'r', encoding="utf-8") as arquivo:
            nomes = arquivo.read().splitlines() 
            return nomes
    except FileNotFoundError:
        print("Nenhum nome registrado.")
        pass

def salvar_nomes(nomes):
        with open(ARQUIVO, 'w', encoding="utf-8") as linha_de_nome:
            for nome in nomes:
                linha_de_nome.write(nome + "\n")

def encontrar_nome (nomes): #encontrar nome/indice
    if nome in nomes:
        return nomes.index(nome) #se o nome estiver na lista, o index devolve a posição dele
    return -1 #significa "nome não encontrado"

def cadastrar_nome():
    nome = input("Nome que deseja cadastrar: ")

    if not nome:
        print("Nome inválido. Nada cadastrado.")
        return

    else:
        with open(ARQUIVO, 'a', encoding="utf-8") as arquivo:
            arquivo.write(nome + "\n")
        print (f"nome '{nome}' cadastrado com sucesso.")

def listar_nome(): 
    
