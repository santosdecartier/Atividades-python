ARQUIVO = "contatos.txt"
SEPARADOR = ";"

def criar_contato (): #função base do "Create" do crud
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
             linhas = arquivo_lido.readlines() #lê o arquivo inteiro e devolve uma lista com uma linha por item, tipo ["bruna;99817\n", "ana;3248\n"]
     except FileNotFoundError:
         print("Nenhum contato foi cadastrado.")
         return
     if len(linhas) == 0:
         print("Nenhum contato foi cadastrado.")
         return
     for linha_percorrida in linhas: #agora vou separar bonitinho, pra que não fique  [bruna;99817\n]//percorre a lista, uma linha por vez
         parte_separada = linha_percorrida.strip().split(SEPARADOR) #retira o \n e o ";", fazendo com que fique ["bruna", "99817"]
         print("\n" + parte_separada[0] + "-" + parte_separada[1] + "\n")
      
def atualizar_contato (): #função base do "Update" do crud
     procurar_contato = input("Digite o contato que deseja mudar: ")
     try:
         with open(ARQUIVO, "r", encoding="utf-8") as arquivo_lido:
             linhas_lidas = arquivo_lido.readlines() #devolve uma lista com uma linha por item, tipo ["amanda;9876", "bruna;8764"]
     except FileNotFoundError:
         print("Nenhum contato foi cadastrado.")
         return

     contato_encontrado = False #é uma "bandeira" que começa como falsa e só vira verdadeira se acharmos o contato

     for posicao_contato in range (len(linhas_lidas)):
         partes_procuradas = linhas_lidas[posicao_contato].strip().split(SEPARADOR)
         if partes_procuradas[0] == procurar_contato:
             novo_telefone = input("Novo telefone: ")
             linhas_lidas[posicao_contato] = partes_procuradas[0] + ";" + novo_telefone + "\n" #troca o item antigo por um novo
             contato_encontrado = True
             break
         if not contato_encontrado:
             print("Contato não encontrado.")
             return
     try:
         with open(ARQUIVO, 'w', encoding="utf-8") as arquivo_lido: #vai trocar o contato antigo pelo novo
          arquivo_lido.readlines(linhas_lidas)
          print ("Contato atualizado.")
     except OSError:
         print("Erro ao salvar o arquivo.")


