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

Catálogo = []
item = {
     Nome: "O Compasso do Vento",
     Nome: "Sob o Luar de Safira",
     Nome: "Ecos de um Amor Distante",
     Nome: "Código Infinito",
     Nome: "Crônicas de uma Terra Esquecida",
     Nome: "Cartas para um Destino Incerto",
     Nome: "Operação: Namorado de Mentirinha",
     Nome: "Adultos (Mais ou Menos)",
     Nome: "O Clube dos Desajustados",
     Nome: "A Garota no Lago",
     Nome: "A Sociedade Literária e a Torta de Casca de Batata",
     Nome: "O Paciente Silencioso"  
 }

Encontrado = False

for item in Catálogo:
   if item["nome"].lower() == Nome.lower():
        print (Nome)
        Encontrado = True
        break

if not Encontrado:
    print ("Item não encontrado")