# Estrutura: { "Nome do Filme": {"likes": 0, "dislikes": 0, "genero": "..."} }
catalogo = {
    "Matrix": {"genero": "Ficção", "likes": 0, "dislikes": 0},
    "Shrek": {"genero": "Animação", "likes": 0, "dislikes": 0},
    "O Chamado": {"genero": "Terror", "likes": 0, "dislikes": 0}
}

#def exibir_catalogo():
 #   print("\n--- MEU CATÁLOGO ---")
   # for filme, dados in catalogo.items():
    #    print(f"🎬 {filme:12} | Gênero: {dados['genero']:10} | 👍 {dados['likes']} | 👎 {dados['dislikes']}")
    #print("--------------------")

#while True:
    #exibir_catalogo()
   # nome = input("\nDigite o nome do filme para avaliar (ou 'sair'): ").title()

   #if nome.lower() == 'sair':
       # break

   # if nome in catalogo:
       # voto = input("Digite [L] para Like ou [D] para Dislike: ").upper()
        
       # if voto == 'L':
         #   catalogo[nome]["likes"] += 1
         #   print(f"Marcado! Você curtiu {nome}.")
      #  elif voto == 'D':
        #    catalogo[nome]["dislikes"] += 1
         #   print(f"Que pena! Você deu dislike em {nome}.")
      #  else:
      #      print("Opção inválida!")
  #  else:
      #  print("Filme não encontrado no catálogo. Verifique a ortografia.")

#print("Programa finalizado.")

while True:
    print("1-adicionar usuario")
    print("2-buscar filme")
    print("0-sair")
    m = int(input())
    if m == 1:
        print("sou o menu 1") 
    elif m == 2:
        print("sou o menu 2")
    elif m == 0:
        print("adeus mundo cruel")
        break





print ("Seja Bem-Vindo ao MyDisney")

Nome = input("Digite seu nome: ")
Email = input("Digite seu email: ")
Senha = input("Crie uma senha: ")

Cadastro = []
Usuário = {
    Nome : "Nome", 
    Email : "Email",
    Senha : "Senha"  
}

Cadastro.append(Usuário)
print("O usuário foi Cadastrado!")

Login = input("Nome de usuário ou email: ")
Senha = input("Senha de sua escolha: ")

print (Login)
print (Senha)

print ("Estamos contentes de recebe-lo aqui! Desejamos uma que você tenha uma ótima experiência!")

Busca = input("Busque aqui: ")
print(Busca)

Catálogo = [
    "O Compasso do Vento",
     "Sob o Luar de Safira",
      "Ecos de um Amor Distante",
     "Código Infinito",
     "Crônicas de uma Terra Esquecida",
     "Cartas para um Destino Incerto",
     "Operação: Namorado de Mentirinha",
      "Adultos (Mais ou Menos)",
      "O Clube dos Desajustados",
     "A Garota no Lago",
     "A Sociedade Literária e a Torta de Casca de Batata",
     "O Paciente Silencioso"  
]

Encontrado = False

if Busca in Catálogo:
    Encontrado = True

if not Encontrado:
    print ("Item não encontrado")

