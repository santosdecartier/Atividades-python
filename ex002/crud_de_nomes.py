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
