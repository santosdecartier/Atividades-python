ARQUIVO = "usuarios.txt"
SEPARADOR = ";"

def criar_usuario (): #função base do "Create" do crud
 try:
     nome = input("Nome: ")
     telefone = input("Telefone: ")
     with open(ARQUIVO, 'a', encoding="utf-8") as arquivo_escrito: #abre o arquivo de texto e 'a' vai acrescentar a informação à linha ali contida
          arquivo_escrito.write(nome + SEPARADOR + telefone + "\n") #a informação da linha será escrita desse modo
          print("\nContato salvo.\n")
 except OSError:
    print ("Erro ao salvar o arquivo.")

#agora que dá pra guardar, vamos ver o que foi guardado
def listar_usuarios (): #função base do "Read" do crud
     try:
         with open(ARQUIVO, 'r', encoding="utf-8") as arquivo_lido: #abre o arquivo pra leitura
             linhas = arquivo_lido.readlines() #lê o arquivo inteiro e devolve uma lista com uma linha por item, tipo [bruna;99817\n]
     except FileNotFoundError:
         print("Nenhum usuário foi cadastrado.")
         return
     if len(linhas) == 0:
         print("Nenhum usuário foi cadastrado.")
         return
     for linha_percorrida in linhas: #agora vou separar bonitinho, pra que não fique  [bruna;99817\n]//percorre a lista, uma linha por vez
         parte_separada = linha_percorrida.strip().split(SEPARADOR) #retira o \n e o ";", fazendo com que fique ["bruna", "99817"]
         print("\n" + parte_separada[0] + "-" + parte_separada[1] + "\n")



